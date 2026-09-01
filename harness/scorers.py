GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def score_contains(response: str, config: dict):
    ok = config["value"].lower() in response.lower()
    return ok, {"looked_for": config["value"]}

def score_contains_any(response: str, config: dict):
    values = config.get("values", [])
    ok = any(str(value).lower() in response.lower() for value in values)
    return ok, {"looked_for_any": [str(value) for value in values]}


def score_max_words(response: str, config: dict):
    max_words = int(config["value"])
    ok = len(response.strip().split()) <= max_words
    return ok, {"looked_if_exceeded": max_words}

SCORERS = {
    "contains": score_contains,
    "contains_any": score_contains_any,
    "max_words": score_max_words
}