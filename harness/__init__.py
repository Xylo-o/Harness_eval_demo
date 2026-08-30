from dataclasses import dataclass

@dataclass
class TestCase:
    id: str
    prompt: str
    scorers: list

@dataclass
class Suite:
    name: str
    cases: str
