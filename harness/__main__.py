import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def get_expected_values(case: dict) -> list:
    values = []
    for scorer in case.get("scorers", []):
        if "value" in scorer and scorer.get("value") is not None:
            values.append(scorer["value"])
    return values


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
        expected_values = get_expected_values(case)
        if not expected_values:
            continue
        response = client.responses.create(model="gpt-5.4-mini", max_output_tokens=200, input=prompt)
        actual = response.output_text.strip().lower()
        passed = any(str(expected).strip().lower() == actual for expected in expected_values)
        if passed:
            print(f"{GREEN}PASS{RESET}")
        else:
            print(f"{RED}FAIL{RESET}")

    return data


if __name__ == "__main__":
    load_suite("suites/basic.yaml")








