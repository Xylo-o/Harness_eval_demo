import hashlib, json, pathlib

CACHE_DIR = pathlib.Path(".cache")

def _key(model: str, prompt: str) -> str:
    return hashlib.sha256(f"{model} || {prompt}".encode("utf-8")).hexdigest()

def get(model:str, prompt: str):
    p = CACHE_DIR / f"{_key(model, prompt)}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None

def put(model: str, prompt: str, response: dict) -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    p = CACHE_DIR / f"{_key(model, prompt)}.json"
    p.write_text(json.dumps(response, ensure_ascii=False), encoding="utf-8")
