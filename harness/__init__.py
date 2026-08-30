from dataclasses import dataclass

@dataclass
class OpenAI_54_mini:
    model: str

class TestCase:
    id: str
    prompt: str
    scorers: list

class Suite:
    name: str
    cases: str
