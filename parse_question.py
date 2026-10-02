from pathlib import Path
import json
import re


INPUT_DIR = Path("data/raw_text")
OUTPUT_FILE = Path("data/questions/questions.json")

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


def extract_year(filename):
    match = re.search(r"20\d{2}", filename)

    if match:
        return int(match.group())

    return None


def detect_paper(filename):
    filename_upper = filename.upper()

    if "CS1" in filename_upper:
        return "CS1"

    if "CS2" in filename_upper:
        return "CS2"

    return "CS"


def detect_session(text):
    """
    Try to detect the session from the paper text.
    """

    patterns = [
        r"SESSION\s*[:\-]?\s*(\d+)",
        r"SESSION\s+(\d+)",
        r"SHIFT\s*[:\-]?\s*(\d+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return int(match.group(1))

    # Papers without an explicit session
    return 1


def detect_marks(text_before_question):

    match = re.search(
        r"Q\.\d+\s*[–-]\s*Q\.\d+.*?"
        r"Carry\s+(ONE|TWO)\s+mark",
        text_before_question,
        re.IGNORECASE |
        re.DOTALL
    )

    if match:

        if match.group(1).upper() == "ONE":
            return 1

        if match.group(1).upper() == "TWO":
            return 2

    return None


def detect_question_type(question_text):

    upper_text = question_text.upper()

    if (
        "SELECT ALL THAT APPLY" in upper_text
        or "MULTIPLE CORRECT" in upper_text
    ):
        return "MSQ"

    if re.search(
        r"\(A\).*?\(B\).*?\(C\).*?\(D\)",
        question_text,
        re.DOTALL
    ):
        return "MCQ"

    return "NAT"


def extract_options(question_text):

    options = {}

    pattern = re.compile(
        r"\(([A-D])\)\s*(.*?)(?=\([A-D]\)|$)",
        re.DOTALL
    )

    matches = pattern.findall(question_text)

    for letter, text in matches:

        options[letter] = (
            text.strip()
        )

    return options


def clean_text(text):

    # Remove page markers
    text = re.sub(
        r"===== PAGE \d+ =====",
        " ",
        text
    )

    # Normalize whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def parse_file(file_path):

    print(f"Reading → {file_path.name}")

    text = file_path.read_text(
        encoding="utf-8"
    )

    year = extract_year(
        file_path.name
    )

    paper = detect_paper(
        file_path.name
    )

    session = detect_session(
        text
    )

    # Find every question boundary
    question_matches = list(
        re.finditer(
          r"(?m)^\s*Q\.\s*(\d+)\b(?!\s*[–-]\s*Q\.)",
            text
        )
    )

    questions = []

    for index, match in enumerate(
        question_matches
    ):

        question_number = int(
            match.group(1)
        )

        start = match.start()

        if index + 1 < len(
            question_matches
        ):

            end = question_matches[
                index + 1
            ].start()

        else:

            end = len(text)

        question_block = text[
            start:end
        ]

        # Get text before this question
        previous_text = text[
            max(0, start - 1000):start
        ]

        marks = detect_marks(
            previous_text
        )

        question_type = detect_question_type(
            question_block
        )

        options = extract_options(
            question_block
        )

        # Remove Q.number from text
        question_text = re.sub(
            r"^\s*Q\.\d+\s*",
            "",
            question_block
        )

        question_text = clean_text(
            question_text
        )

        questions.append({

            "question_number":
                question_number,

            "session":
                session,

            "year":
                year,

            "paper":
                paper,

            "marks":
                marks,

            "question_type":
                question_type,

            "question_text":
                question_text,

            "options":
                options,

            "source_file":
                file_path.name
        })

    return questions


def main():

    print("=" * 70)
    print("GATE QUESTION PARSER")
    print("=" * 70)

    files = list(
        INPUT_DIR.glob("*.txt")
    )

    print(
        f"\nText files found: {len(files)}"
    )

    all_questions = []

    for file_path in files:

        try:

            questions = parse_file(
                file_path
            )

            all_questions.extend(
                questions
            )

            print(
                f"Parsed → {len(questions)} questions"
            )

        except Exception as e:

            print(
                f"ERROR → {file_path.name}"
            )

            print(e)

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            all_questions,
            f,
            indent=2,
            ensure_ascii=False
        )

    print("\n" + "=" * 70)
    print("QUESTION PARSING COMPLETE")
    print("=" * 70)

    print(
        f"\nTotal questions: "
        f"{len(all_questions)}"
    )

    print(
        f"Saved → {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()