import os
from dataclasses import dataclass
from types import SimpleNamespace

from dotenv import load_dotenv
from openai import OpenAI

from .cache import get, put

load_dotenv()


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)


@dataclass
class OpenAIProvider:
    model: str

    def complete(self, prompt: str):
        cached = get(self.model, prompt)
        if cached is not None:
            return SimpleNamespace(text=cached.get("text", str(cached)))

        client = get_client()
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )

        text = response.choices[0].message.content
        payload = {"text": text}
        put(self.model, prompt, payload)
        return SimpleNamespace(text=text)

