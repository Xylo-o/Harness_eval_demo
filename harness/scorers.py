
def score_contains(response: str, config: dict):
    ok = config["value"].lower() in response.lower()
    return ok, {"looked_for": config["value"]}

def score_max_words(response: str, config: dict):
    max_words = int(config["value"])
    ok = len(response.strip().split()) <= max_words
    return ok, {"looked_if_exceeded": max_words}

SCORERS = {
    "contains": score_contains,
    "max_words": score_max_words
}