import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from harness.__main__ import get_expected_values


def test_get_expected_values_skips_scorers_without_value():
    case = {
        "prompt": "Return just JSON with fields name and age for Jan",
        "scorers": [
            {"type": "json_valid"},
            {"type": "json_field", "field": "name", "value": "Jan"},
        ],
    }

    assert get_expected_values(case) == ["Jan"]
