from pathlib import Path
from pypdf import PdfReader


# Folder containing answer-key PDFs
ANSWER_DIR = Path("data/answer_keys")

# Folder where extracted answer-key text will be saved
OUTPUT_DIR = Path("data/raw_answer_keys")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def extract_pdf_text(pdf_path):

    print(f"\nReading → {pdf_path.name}")

    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        text = page.extract_text()

        if text:

            pages.append(
                f"\n\n===== PAGE {page_number} =====\n\n"
                + text
            )

    return "".join(pages)


def main():

    print("=" * 70)
    print("GATE ANSWER KEY EXTRACTION")
    print("=" * 70)

    # Find all answer-key PDFs
    pdf_files = list(
        ANSWER_DIR.glob("*.pdf")
    )

    print(
        f"\nAnswer-key PDFs found: {len(pdf_files)}"
    )

    # Extract every PDF
    for pdf_path in pdf_files:

        try:

            text = extract_pdf_text(
                pdf_path
            )

            # Output filename
            output_file = (
                OUTPUT_DIR /
                f"{pdf_path.stem}.txt"
            )

            # Save extracted text
            output_file.write_text(
                text,
                encoding="utf-8"
            )

            print(
                f"Saved → {output_file}"
            )

        except Exception as e:

            print(
                f"ERROR → {pdf_path.name}"
            )

            print(e)

    print("\n" + "=" * 70)
    print("ANSWER EXTRACTION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()