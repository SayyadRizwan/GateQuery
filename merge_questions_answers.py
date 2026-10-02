from pathlib import Path
import json


QUESTIONS_FILE = Path("data/questions/questions.json")
ANSWERS_FILE = Path("data/questions/answers.json")
OUTPUT_FILE = Path("data/questions/final_questions.json")


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    print("=" * 70)
    print("MERGING QUESTIONS AND ANSWERS")
    print("=" * 70)

    # Load both datasets
    questions = load_json(QUESTIONS_FILE)
    answers = load_json(ANSWERS_FILE)

    print(f"\nQuestions loaded: {len(questions)}")
    print(f"Answers loaded:  {len(answers)}")

    # Create lookup dictionary for answers
    answer_lookup = {}

    for answer in answers:

        key = (
            answer["year"],
            answer["paper"],
            answer["question_number"]
        )

        answer_lookup[key] = answer

    final_questions = []

    matched = 0
    missing = 0

    for question in questions:

        key = (
            question["year"],
            question["paper"],
            question["question_number"]
        )

        answer_data = answer_lookup.get(key)

        if answer_data:

            question["answer"] = answer_data["answer"]
            question["answer_source"] = answer_data["source_file"]

            matched += 1

        else:

            question["answer"] = None
            question["answer_source"] = None

            missing += 1

        final_questions.append(question)

    # Save final dataset
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            final_questions,
            f,
            indent=2,
            ensure_ascii=False
        )

    print("\n" + "=" * 70)
    print("MERGE COMPLETE")
    print("=" * 70)

    print(f"\nMatched answers : {matched}")
    print(f"Missing answers: {missing}")
    print(f"Total questions: {len(final_questions)}")

    print(
        f"\nSaved → {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()