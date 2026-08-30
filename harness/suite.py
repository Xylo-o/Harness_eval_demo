import yaml
from dataclasses import dataclass

@dataclass
class TestCase:
    id: str
    prompt: str
    scorers: list

class Suite:
    name: str
    cases: str

def load_suite(path: str):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    cases = Suite(name=data["name"], cases=[])
    for raw in data["cases"]:
        case = TestCase(id=raw["id"], prompt=raw["prompt"], scorers=raw["scorers"])
        cases.append(case)
    return cases
