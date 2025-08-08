# judge.py
from call_model import call_model

def judge_story(story: str) -> str:
    prompt = f"""
You are a careful children's-literature editor (ages 5–10). Review the story and give:
1) One-sentence verdict on age-appropriateness.
2) Three concrete improvement suggestions (language, pacing, clarity, moral).
3) Safety checks (violence/scariness/unsafe advice): list any issues.
Keep total under 150 words.

Story:
{story}
"""
    return call_model(prompt, max_tokens=300, temperature=0.3)

def revise_story(story: str, feedback: str) -> str:
    prompt = f"""
You are a friendly children's storyteller (ages 5–10).
Revise the story using the editor's feedback below.
Keep the language simple and warm, with a clear beginning–middle–end,
and include a gentle lesson. Target length 350–500 words.

Original story:
{story}

Editor feedback:
{feedback}
"""
    return call_model(prompt, max_tokens=700, temperature=0.7)
