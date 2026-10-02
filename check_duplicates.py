from pathlib import Path
import json
from collections import Counter


QUESTIONS_FILE = Path("data/questions/questions.json")
ANSWERS_FILE = Path("data/questions/answers.json")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    questions = load_json(QUESTIONS_FILE)
    answers = load_json(ANSWERS_FILE)

    print("=" * 70)
    print("CHECKING QUESTION / ANSWER KEYS")
    print("=" * 70)

    # --------------------------------------------------
    # Check duplicate question keys
    # --------------------------------------------------

    question_keys = []

    for q in questions:

        key = (
            q.get("year"),
            q.get("paper"),
            q.get("question_number")
        )

        question_keys.append(key)

    duplicates_questions = {
        key: count
        for key, count in Counter(question_keys).items()
        if count > 1
    }

    print("\nDuplicate question keys:")

    if duplicates_questions:
        for key, count in duplicates_questions.items():
            print(f"  {key} → {count} times")
    else:
        print("  None")

    # --------------------------------------------------
    # Check duplicate answer keys
    # --------------------------------------------------

    answer_keys = []

    for a in answers:

        key = (
            a.get("year"),
            a.get("paper"),
            a.get("question_number")
        )

        answer_keys.append(key)

    duplicates_answers = {
        key: count
        for key, count in Counter(answer_keys).items()
        if count > 1
    }

    print("\nDuplicate answer keys:")

    if duplicates_answers:
        for key, count in duplicates_answers.items():
            print(f"  {key} → {count} times")
    else:
        print("  None")

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(f"Total questions: {len(questions)}")
    print(f"Total answers:   {len(answers)}")

    print(
        f"Unique question keys: {len(set(question_keys))}"
    )

    print(
        f"Unique answer keys:   {len(set(answer_keys))}"
    )


if __name__ == "__main__":
    main()