# Hippocratic AI Coding Assignment
Welcome to the [Hippocratic AI](https://www.hippocraticai.com) coding assignment

## Instructions
The attached code is a simple python script skeleton. Your goal is to take any simple bedtime story request and use prompting to tell a story appropriate for ages 5 to 10.
- Incorporate a LLM judge to improve the quality of the story
- Provide a block diagram of the system you create that illustrates the flow of the prompts and the interaction between judge, storyteller, user, and any other components you add
- Do not change the openAI model that is being used. 
- Please use your own openAI key, but do not include it in your final submission.
- Otherwise, you may change any code you like or add any files

---

## Rules
- This assignment is open-ended
- You may use any resources you like with the following restrictions
   - They must be resources that would be available to you if you worked here (so no other humans, no closed AIs, no unlicensed code, etc.)
   - Allowed resources include but not limited to Stack overflow, random blogs, chatGPT et al
   - You have to be able to explain how the code works, even if chatGPT wrote it
- DO NOT PUSH THE API KEY TO GITHUB. OpenAI will automatically delete it

---

## What does "tell a story" mean?
It should be appropriate for ages 5-10. Other than that it's up to you. Here are some ideas to help get the brain-juices flowing!
- Use story arcs to tell better stories
- Allow the user to provide feedback or request changes
- Categorize the request and use a tailored generation strategy for each category

---

## How will I be evaluated
Good question. We want to know the following:
- The efficacy of the system you design to create a good story
- Are you comfortable using and writing a python script
- What kinds of prompting strategies and agent design strategies do you use
- Are the stories your tool creates good?
- Can you understand and deconstruct a problem
- Can you operate in an open-ended environment
- Can you surprise us

---

## Other FAQs
- How long should I spend on this? 
No more than 2-3 hours
- Can I change what the input is? 
Sure
- How long should the story be?
You decide

# Hippocratic AI – Bedtime Story with LLM Judge

A small Python tool that takes any kids’ bedtime story request and:
1) generates a story for ages **5–10**
2) has an **LLM judge** critique it
3) optionally revises the story using the judge’s feedback.

**Model:** `gpt-3.5-turbo` (per assignment: *do not change the model*).

---

## Quick start

### 1) Python & dependencies
~~~bash
# create & activate venv (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# install deps
pip install -r requirements.txt
~~~

### 2) Set your OpenAI API key (do NOT commit it)
~~~bash
# Windows PowerShell
$env:OPENAI_API_KEY="sk-xxxxxxxx"

# macOS/Linux
export OPENAI_API_KEY="sk-xxxxxxxx"
~~~

### 3) Run
~~~bash
python main.py                   # prints only the final story
python main.py --show-all        # also prints the initial story + judge feedback
python main.py --show-all --save # also saves outputs to text files
~~~

---

## Project structure
~~~
.
├── main.py               # orchestration (generate → judge → revise)
├── call_model.py         # OpenAI call wrapper (retries + friendly errors)
├── story_generator.py    # Storyteller prompts
├── judge.py              # Judge + Reviser prompts
├── requirements.txt
└── README.md
~~~

---

## Block diagram
~~~mermaid
flowchart LR
  U[User prompt] --> S[Storyteller\n(ChatCompletion:gpt-3.5-turbo)]
  S -->|initial story| J[LLM Judge\n(ChatCompletion)]
  J -->|feedback| R[Reviser\n(ChatCompletion)]
  U -- optional tweaks --> R
  R --> O[Final story shown/saved]
~~~

---

## How it works

- **Storyteller (`story_generator.generate_story`)**  
  Prompt enforces: simple language, clear beginning–middle–end, gentle moral, 250–350 words.

- **LLM Judge (`judge.judge_story`)**  
  Returns a short, structured critique:
  - Verdict (age-appropriateness for 5–10)
  - Three actionable fixes (language / pacing / clarity / moral)
  - Safety notes (flag scary/unsafe advice)

- **Reviser (`judge.revise_story`)**  
  Applies the judge’s feedback to produce the **final improved story**.

- **API wrapper (`call_model.call_model`)**  
  Reads `OPENAI_API_KEY` from env, uses `gpt-3.5-turbo`, adds simple retries and friendly error messages (quota, auth, connection).

---

## Prompting strategy highlights

- Constrain length & tone: 250–350 words, warm and safe language, clear moral.  
- Concise judge: fixed output format (verdict + 3 fixes + safety) → predictable cost and targeted edits.  
- Revision uses feedback verbatim to reduce drift and ensure measurable improvement.

---

## CLI options

- `--show-all` – also print the initial draft and the judge’s feedback.  
- `--save` – save `story_final.txt` (and, when `--show-all`, `story_initial.txt` / `judge_feedback.txt`).

---

## Troubleshooting

- **`[Error] OPENAI_API_KEY not set.`** – set the env var as shown above.  
- **Quota/billing error (429 or quota exceeded)** – API credits are separate from ChatGPT Plus. Add a payment method and ensure Usage limits > $0.  
- **`ModuleNotFoundError: openai`** – run `pip install -r requirements.txt` inside your virtual environment.  
- **Multiple Python installations on Windows** – create/activate venv with `python -m venv .venv`, confirm `python -V` is 3.11+ before installing/running.

---

## Requirements
~~~text
openai==0.28.1
~~~
> This version still supports `openai.ChatCompletion.create`, matching the provided skeleton code.

---

## Notes

- Do **not** commit your API key or your local `.venv/`.  
- Keep the model as `gpt-3.5-turbo` to comply with the assignment.
