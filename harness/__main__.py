import json
from pathlib import Path
from .runner import runner

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


if __name__ == "__main__":
    runner()
    print(f"Program finished")


