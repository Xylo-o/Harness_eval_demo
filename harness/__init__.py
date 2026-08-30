from dataclasses import dataclass

@dataclass
class OpenAI_54_mini:
    model: str

@dataclass
class TestCase:
    id: str
    prompt: str
    scorers: list

@dataclass
class Suite:
    name: str
    cases: str
