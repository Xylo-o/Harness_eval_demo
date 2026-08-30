from harness.suite import TestCase
from harness.scorers import SCORERS

def runner(case: TestCase):
    for case in suite.cases:
        response = provider.complete(case.prompt)
        for cfg in case.scorers:
            passed, detail = SCORERS[cfg["type"]](response.text, cfg)
            results.append((case.id, cfg["type"], passed, detail))