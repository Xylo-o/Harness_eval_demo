from .providers import OpenAIProvider
from .scorers import SCORERS
from .suite import load_suite


def runner(model: str = "gpt-5.4-mini"):
    provider = OpenAIProvider(model=model)
    suite = load_suite("suites/basic.yaml")
    results = []
    for case in suite.cases:
        response = provider.complete(case.prompt)
        for cfg in case.scorers:
            passed, detail = SCORERS[cfg["type"]](response.text, cfg)
            results.append((case.id, cfg["type"], passed, detail))
    return results