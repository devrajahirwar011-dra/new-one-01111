import os

import openai

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAIBrain:
    """A simple wrapper to send text to OpenAI and receive AI responses."""

    def __init__(self) -> None:
        self.api_key = openai.api_key
        if not self.api_key:
            print("Warning: OPENAI_API_KEY is not set. OpenAI responses will be disabled until .env is configured.")

    def generate_response(self, user_text: str) -> str:
        """Send a terminal message to OpenAI and return the assistant's reply."""
        if not self.api_key:
            return (
                "I cannot connect to OpenAI because OPENAI_API_KEY is not configured. "
                "Please add your key to the .env file."
            )

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a friendly AI assistant named Nova. "
                    "Answer clearly and help the user with any question."
                ),
            },
            {"role": "user", "content": user_text},
        ]

        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=250,
        )

        return response.choices[0].message.content.strip()
