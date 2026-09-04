from dataclasses import dataclass
from .providers import OpenAIProvider
from .scorers import SCORERS

@dataclass
class CaseResult:
    case_key: str
    response: str
    latency_ms: int
    tokens_in: int
    tokens_out: int
    error: str


def runner(suite: str, model: str):
    provider = OpenAIProvider(model=model)
    results = []
    scores = []
    error = False
    for case in suite.cases:
        try:
            response = provider.complete(case.prompt)
        except Exception:
            error = True
        scores.append((case.id,))
        for cfg in case.scorers:
            passed, detail = SCORERS[cfg["type"]](response.text, cfg)
        results.append(CaseResult(case_key=case.id, response=response.text, latency_ms=response.latency_ms, tokens_in=response.tokens_in, tokens_out=response.tokens_out, error=error))                   
    return results
