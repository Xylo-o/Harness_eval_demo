import argparse

parser = argparse.ArgumentParser(prog="harness")

parser.add_argument("--suite", required=True, help="Suite filepath")
parser.add_argument("--model", default="gpt-5.4-mini", help="Model to be tested")
parser.add_argument("--no-cache", help="No cache storing")
parser.add_argument("--timeout", type=int, help="Timeout time")

args = parser.parse_args()

