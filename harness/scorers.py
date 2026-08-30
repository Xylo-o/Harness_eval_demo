
def score_contains(response: str, config: dict):
    ok = config["value"].lower() in response.lower()
    return ok, {"looked_for": config["value"]}

SCORERS = {
    "contains": score_contains
}