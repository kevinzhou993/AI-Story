# call_model.py
import os, time, openai
from openai.error import RateLimitError, APIConnectionError, Timeout, APIError, AuthenticationError

def call_model(prompt: str, max_tokens=600, temperature=0.7, retries=3) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        return "[Error] OPENAI_API_KEY not set."

    for attempt in range(retries):
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
                stream=False,
            )
            return resp.choices[0].message["content"]
        except (RateLimitError, APIConnectionError, Timeout, APIError) as e:
            if attempt == retries - 1:
                return f"[Error] API issue: {e}"
            time.sleep(2 ** attempt)
        except AuthenticationError:
            return "[Error] Invalid API key."
