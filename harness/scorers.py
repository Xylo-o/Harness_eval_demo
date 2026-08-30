

def score_contains(response: str, scorers: dict):
    ok = scorers["value"].lower() in response.lower()
    return ok, {"looked_for": scorers["value"]}

SCORERS = {
    "contains": score_contains
}