import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def get_expected_values(case: dict) -> list:
    values = []
    for scorer in case.get("scorers", []):
        if "value" in scorer and scorer.get("value") is not None:
            values.append(scorer["value"])
        if "values" in scorer and scorer.get("values") is not None:
            vals = scorer["values"]
            if isinstance(vals, list):
                values.extend(vals)
            else:
                values.append(vals)
    return values


def scorer_passes(actual_text: str, scorer: dict) -> bool:
    t = scorer.get("type")
    txt = actual_text or ""
    if t == "contains":
        vals = scorer.get("values") or ([scorer.get("value")] if "value" in scorer else [])
        for v in vals:
            if v is None:
                continue
            if str(v).strip().lower() in txt.lower():
                return True
        return False

    if t == "max_words":
        try:
            limit = int(scorer.get("value"))
        except Exception:
            return False
        return len(txt.split()) <= limit

    if t == "json_valid":
        try:
            json.loads(txt)
            return True
        except Exception:
            return False

    if t == "json_field":
        field = scorer.get("field")
        if not field:
            return False
        try:
            parsed = json.loads(txt)
        except Exception:
            return False
        if "value" in scorer:
            expected = scorer.get("value")
            actual_val = parsed.get(field)
            return str(actual_val).strip().lower() == str(expected).strip().lower()
        if "values" in scorer:
            expected_vals = scorer.get("values") or []
            actual_val = parsed.get(field)
            for ev in expected_vals:
                if str(actual_val).strip().lower() == str(ev).strip().lower():
                    return True
            return False

    return False


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)


def load_suite(path: str | Path) -> dict:
    suite_path = Path(path)

    with open(suite_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    client = get_client()

    for case in data["cases"]:
        prompt = case["prompt"]
        case_id = case.get("id", "<no-id>")
        print(f"Running case {case_id!r} scorers={case.get('scorers')}")

        scorers = case.get("scorers", [])
        if not scorers:
            print("(no scorers; skipping)")
            continue

        response = client.responses.create(model="gpt-5.4-mini", input=prompt)
        actual = response.output_text.strip()
        print("Response:", actual)

        # Evaluate all scorers: case passes only if all scorers pass
        results = [scorer_passes(actual, s) for s in scorers]
        for s, r in zip(scorers, results):
            print(f" - scorer {s.get('type')!r} -> {r}")

        passed = all(results) if results else False
        if passed:
            print(f"{GREEN}PASS{RESET}")
        else:
            print(f"{RED}FAIL{RESET}")

    return data


if __name__ == "__main__":
    load_suite("suites/basic.yaml")








