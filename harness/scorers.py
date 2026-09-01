import json

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

def score_valid_json(response: str, config: dict):
    try:
        json.loads(response)
        return True, {}
    except json.JSONDecodeError as e:
        return False, {"error": str(e)}

SCORERS = {
    "contains": score_contains,
    "contains_any": score_contains_any,
    "max_words": score_max_words,
    "valid_json": score_valid_json
}