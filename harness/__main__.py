import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from dataclasses import dataclass
import json

load_dotenv()

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

@dataclass
class TestCase:
    id: str
    prompt: str
    scorers: list

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)

def load_suite(path: str):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    cases = []

    client = get_client()
    for raw in data["cases"]:
        case = TestCase(id=cases["id"], prompt=cases["prompt"], scorers=cases["scorers"])
        if (case.scorers == "value"):
            cases.append(case)
        elif (case.scorers == "values"):
            cases.extend(case)

        response = client.responses.create(model="gpt-5.4-mini", input=case.prompt)
    return cases

def compare_results(response: str, scorer: dict) -> list:
    passed = cases["case"][id]["scorers"] == response.output_text.strip()
    if passed:
        print(f"{GREEN}PASS{RESET}")
    else:
        print(f"{RED}FAIL{RESET}")



if __name__ == "__main__":
    load_suite("suites/basic.yaml")








