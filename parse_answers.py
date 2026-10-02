from pathlib import Path
import re
import json


INPUT_DIR = Path("data/raw_answer_keys")
OUTPUT_FILE = Path("data/questions/answers.json")


def parse_answer_file(file_path):

    print(f"Reading → {file_path.name}")

    text = file_path.read_text(
        encoding="utf-8"
    )

    answers = []

    # Match lines such as:
    # 11 1 MCQ CS A 1
    # 23 1 MSQ CS B,C,D 1
    pattern = re.compile(
        r"^\s*(\d+)\s+"
        r"(\d+)\s+"
        r"(MCQ|MSQ|NAT)\s+"
        r"(\w+)\s+"
        r"(.+?)\s+"
        r"(\d+(?:\.\d+)?)\s*$",
        re.MULTILINE
    )

    for match in pattern.finditer(text):

        question_number = int(match.group(1))
        session = int(match.group(2))
        question_type = match.group(3)
        subject = match.group(4)
        answer = match.group(5).strip()
        marks = float(match.group(6))

        answers.append({
            "question_number": question_number,
            "session": session,
            "question_type": question_type,
            "subject": subject,
            "answer": answer,
            "marks": marks
        })

    return answers


def main():

    print("=" * 70)
    print("GATE ANSWER KEY PARSER")
    print("=" * 70)

    all_answers = []

    files = list(INPUT_DIR.glob("*.txt"))

    print(f"\nAnswer-key files found: {len(files)}")

    for file_path in files:

        try:

            answers = parse_answer_file(file_path)

            # Extract year from filename
            year_match = re.search(
                r"20\d{2}",
                file_path.name
            )

            year = (
                int(year_match.group())
                if year_match
                else None
            )

            # Extract session/paper information
            session_match = re.search(
                r"CS(1|2)",
                file_path.name
            )

            paper = (
                f"CS{session_match.group(1)}"
                if session_match
                else "CS"
            )

            for answer in answers:

                answer["year"] = year
                answer["paper"] = paper
                answer["source_file"] = file_path.name

                all_answers.append(answer)

            print(
                f"Parsed → {file_path.name}: "
                f"{len(answers)} answers"
            )

        except Exception as e:

            print(
                f"ERROR → {file_path.name}"
            )

            print(e)

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
            all_answers,
            f,
            indent=2,
            ensure_ascii=False
        )

    print("\n" + "=" * 70)
    print("ANSWER PARSING COMPLETE")
    print("=" * 70)

    print(
        f"\nTotal answers extracted: "
        f"{len(all_answers)}"
    )

    print(
        f"Saved → {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()