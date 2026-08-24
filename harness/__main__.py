import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.responses.create(model="gpt-5.4-mini", max_output_tokens=200, input="What's the capital of Poland? Answer in one word")
correct_response = "Warsaw"

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

if (response.output_text.strip().lower() == correct_response.lower()):
    print(f"{GREEN}PASS{RESET}")
else:
    print(f"{RED}FAIL{RESET}")

