import argparse
import sys

from harness.suite import load_suite
from harness.runner import runner
from harness.table import print_table


def main():
    parser = argparse.ArgumentParser(prog="harness")

    parser.add_argument("--suite", required=True, help="Suite filepath")
    parser.add_argument("--model", default="gpt-5.4-mini", help="Model to be tested")
    parser.add_argument("--no-cache", action="store_true", help="No cache storing")
    parser.add_argument("--timeout", type=int, help="Timeout time")

    args = parser.parse_args()

    suite = load_suite(args.suite)
    results = runner(suite, model=args.model)
    print_table(results)

    tests_passed = True

    for case_id, scorer_type, passed, detail in results:
        if not passed:
            tests_passed = False

    sys.exit(0 if tests_passed else 1)

