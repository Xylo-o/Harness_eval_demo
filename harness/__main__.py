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
    for raw in data["cases"]:
        case = TestCase(id=raw["id"], prompt=raw["prompt"], scorers=raw["scorers"])
        cases.append(case)
    return cases

def score_contains(response: str, scorers: dict):
    ok = scorers["value"].lower() in response.lower()
    return ok, {"looked_for": scorers["value"]}

SCORERS = {
    "contains": score_contains
}



if __name__ == "__main__":
    load_suite("suites/basic.yaml")








