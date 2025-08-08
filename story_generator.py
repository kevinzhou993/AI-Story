# story_generator.py
from call_model import call_model

def generate_story(user_prompt: str) -> str:
    story_prompt = f"""
You are a friendly bedtime storyteller for children aged 5 to 10.
Write a short bedtime story based on this request:

"{user_prompt}"

Requirements:
- Use simple and engaging language suitable for ages 5-10.
- Include a clear beginning, middle, and end.
- Incorporate a gentle moral or fun lesson.
- Keep it around 300–500 words.
"""
    return call_model(story_prompt, max_tokens=600, temperature=0.7)
