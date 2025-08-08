import argparse
from story_generator import generate_story
from judge import judge_story, revise_story

"""
If I had 2 more hours, I would:
1) Add a tiny topic classifier (animals/adventure/magic/school) to route the user prompt to a tailored story template.
2) Add an interactive “tweak loop” so the user can say “shorter/funnier/change the hero” and get an immediate revision.
3) Run a lightweight safety pass before output (e.g., flag scary/unsafe advice and nudge the text to be gentler).
4) Add exports (save as PDF and optional TTS to MP3) so the story can be printed or listened to at bedtime.
5) Improve engineering: simple caching and logging, a --seed flag for reproducibility, and a couple of unit tests for prompt formatting.
"""

example_requests = "A story about a girl named Alice and her best friend Bob, who happens to be a cat."

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-all", action="store_true", help="also print draft & judge feedback")
    parser.add_argument("--save", action="store_true", help="save outputs to text files")
    args = parser.parse_args()

    user_input = input("What kind of story do you want to hear? ")
    initial = generate_story(user_input)
    feedback = judge_story(initial)
    final_story = revise_story(initial, feedback)

    if args.show_all:
        print("\n--- Initial Story ---\n", initial)
        print("\n--- Judge Feedback ---\n", feedback)

    print("\n--- Final Story ---\n", final_story)

    if args.save:
        with open("story_final.txt", "w", encoding="utf-8") as f: f.write(final_story)
        if args.show_all:
            with open("story_initial.txt", "w", encoding="utf-8") as f: f.write(initial)
            with open("judge_feedback.txt", "w", encoding="utf-8") as f: f.write(feedback)

if __name__ == "__main__":
    main()