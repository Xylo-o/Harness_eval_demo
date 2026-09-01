from .providers import OpenAIProvider
from .scorers import SCORERS


def runner(suite: str, model: str):
    provider = OpenAIProvider(model=model)
    results = []
    for case in suite.cases:
        response = provider.complete(case.prompt)
        for cfg in case.scorers:
            passed, detail = SCORERS[cfg["type"]](response.text, cfg)
            results.append((case.id, cfg["type"], passed, detail))
    return results