import csv
import re
import requests
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup


# ============================================================
# CONFIGURATION
# ============================================================

SOURCE_URL = "https://gate2026.iitg.ac.in/download.html"

DATA_DIR = Path("data")
PAPER_DIR = DATA_DIR / "papers"
ANSWER_DIR = DATA_DIR / "answer_keys"
MANIFEST_FILE = DATA_DIR / "manifest.csv"

PAPER_DIR.mkdir(parents=True, exist_ok=True)
ANSWER_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# ============================================================
# GET OFFICIAL GATE PAGE
# ============================================================

def get_page():

    print("Opening official GATE download page...")

    response = requests.get(
        SOURCE_URL,
        headers=HEADERS,
        timeout=60
    )

    response.raise_for_status()

    return response.text


# ============================================================
# EXTRACT LINKS
# ============================================================

def extract_links(html):

    soup = BeautifulSoup(html, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):

        text = a.get_text(" ", strip=True)

        url = urljoin(
            SOURCE_URL,
            a["href"]
        )

        links.append({
            "text": text,
            "url": url
        })

    return links


# ============================================================
# CHECK CS LINK
# ============================================================

def is_cs_link(text, url):

    combined = (
        text + " " + url
    ).lower()

    if "computer science" in combined:
        return True

    filename = url.split("/")[-1].lower()

    patterns = [
        r"^cs",
        r"^cs_",
        r"_cs",
        r"cs20"
    ]

    for pattern in patterns:

        if re.search(pattern, filename):
            return True

    return False


# ============================================================
# EXTRACT YEAR
# ============================================================

def extract_year(url):

    match = re.search(
        r"20(0[7-9]|1\d|2[0-5])",
        url
    )

    if match:
        return int(match.group())

    return None


# ============================================================
# DETECT PAPER SESSION
# ============================================================

def detect_session(text, url):

    combined = (
        text + " " + url
    ).lower()

    if "cs1" in combined:
        return "CS1"

    if "cs2" in combined:
        return "CS2"

    return "CS"


# ============================================================
# IDENTIFY FILE TYPE
# ============================================================

def classify_file(text, url):

    combined = (
        text + " " + url
    ).lower()

    answer_words = [
        "answer",
        "answer_key",
        "ans_gate",
        "finalanswer",
        "keys",
        "merged"
    ]

    for word in answer_words:

        if word in combined:
            return "answer_key"

    return "question_paper"


# ============================================================
# CREATE CLEAN FILENAME
# ============================================================

def create_filename(year, session, file_type):

    if session == "CS":
        filename = f"GATE_CS_{year}"
    else:
        filename = f"GATE_CS_{year}_{session}"

    if file_type == "answer_key":
        filename += "_ANSWER"

    return filename + ".pdf"


# ============================================================
# DOWNLOAD FILE
# ============================================================

def download_file(url, output_path):

    if output_path.exists():

        print(
            f"Already exists → {output_path}"
        )

        return True

    try:

        print(
            f"Downloading → {url}"
        )

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=60
        )

        response.raise_for_status()

        content = response.content

        if len(content) < 1000:

            print(
                "File is too small. Skipping."
            )

            return False

        output_path.write_bytes(content)

        print(
            f"Saved → {output_path}"
        )

        return True

    except Exception as e:

        print(
            f"Download failed: {e}"
        )

        return False


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("GATE CS DATA COLLECTION")
    print("=" * 70)

    html = get_page()

    links = extract_links(html)

    print(
        f"\nTotal links found: {len(links)}"
    )

    manifest = []

    seen = set()

    for link in links:

        text = link["text"]
        url = link["url"]

        # Get year
        year = extract_year(url)

        if year is None:
            continue

        # We are currently collecting 2019-2025
        if year < 2019 or year > 2025:
            continue

        # Check CS
        if not is_cs_link(text, url):
            continue

        # Avoid duplicate URLs
        if url in seen:
            continue

        seen.add(url)

        # Determine type
        file_type = classify_file(
            text,
            url
        )

        # Determine session
        session = detect_session(
            text,
            url
        )

        # Create filename
        filename = create_filename(
            year,
            session,
            file_type
        )

        # Select directory
        if file_type == "answer_key":
            output_path = ANSWER_DIR / filename
        else:
            output_path = PAPER_DIR / filename

        # Download
        success = download_file(
            url,
            output_path
        )

        if not success:
            continue

        # Save metadata
        manifest.append({

            "year": year,

            "paper": session,

            "type": file_type,

            "source_url": url,

            "local_file": str(output_path)

        })

    # ========================================================
    # SAVE MANIFEST
    # ========================================================

    with open(
        MANIFEST_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "year",
                "paper",
                "type",
                "source_url",
                "local_file"
            ]
        )

        writer.writeheader()

        writer.writerows(manifest)

    # ========================================================
    # SUMMARY
    # ========================================================

    papers = [
        item for item in manifest
        if item["type"] == "question_paper"
    ]

    answers = [
        item for item in manifest
        if item["type"] == "answer_key"
    ]

    print("\n" + "=" * 70)

    print(
        f"Question papers collected : {len(papers)}"
    )

    print(
        f"Answer keys collected     : {len(answers)}"
    )

    print(
        f"Total files               : {len(manifest)}"
    )

    print(
        f"Manifest                  : {MANIFEST_FILE}"
    )

    print("=" * 70)


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()