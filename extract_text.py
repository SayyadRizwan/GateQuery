from pathlib import Path
from pypdf import PdfReader


# ============================================================
# CONFIGURATION
# ============================================================

PAPER_DIR = Path("data/papers")
OUTPUT_DIR = Path("data/raw_text")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# EXTRACT TEXT FROM ONE PDF
# ============================================================

def extract_pdf_text(pdf_path):

    print(f"\nReading → {pdf_path.name}")

    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text:

            pages.append(
                f"\n\n===== PAGE {page_number} =====\n\n"
                + text
            )

    return "".join(pages)


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("GATE CS PDF TEXT EXTRACTION")
    print("=" * 70)

    pdf_files = list(
        PAPER_DIR.glob("*.pdf")
    )

    print(
        f"\nPDF files found: {len(pdf_files)}"
    )

    for pdf_path in pdf_files:

        try:

            text = extract_pdf_text(
                pdf_path
            )

            output_file = (
                OUTPUT_DIR /
                f"{pdf_path.stem}.txt"
            )

            output_file.write_text(
                text,
                encoding="utf-8"
            )

            print(
                f"Saved → {output_file}"
            )

            print(
                f"Characters extracted: {len(text):,}"
            )

        except Exception as e:

            print(
                f"ERROR → {pdf_path.name}"
            )

            print(e)

    print("\n" + "=" * 70)

    print(
        f"Extracted text saved in: {OUTPUT_DIR}"
    )

    print("=" * 70)


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()