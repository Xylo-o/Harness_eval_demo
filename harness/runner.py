from .scorers import SCORERS
from .providers import get_client
from .suite import load_suite

provider = get_client()
suite = load_suite("suites/basic.yaml")

def runner():
    results = []
    for case in suite.cases:
        response = provider.complete(case.prompt)
        for cfg in case.scorers:
            passed, detail = SCORERS[cfg["type"]](response.text, cfg)
            results.append((case.id, cfg["type"], passed, detail))
    return results