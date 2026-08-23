from sqlalchemy import JSON
from sqlalchemy.dialects.postgresql import JSONB
import json

JSONType = JSON().with_variant(JSONB(), "postresql")

def read(path: str) -> dict:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return ("File not found")
    except json.JSONDecodeError:
        return ("Error in JSON data")
    except PermissionError:
        return ("No read permission")
    except IsADirectoryError:
        return ("The path is a directory, not a file")
    except TypeError:
        return ("Wrong data type")
    except Exception:
        return ("Error")
    print("Read finished")