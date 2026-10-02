import json
from pathlib import Path

INPUT_FILE = Path("data/questions/final_questions.json")
OUTPUT_FILE = Path("data/questions/rag_documents.json")

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)

documents = []

for q in questions:
    options = q.get("options", {})

    options_text = ""
    if options:
        options_text = "\n".join(
            f"{key}. {value}" for key, value in options.items()
        )

    answer = q.get("answer")
    answer_text = answer if answer else "Not available"

    document = f"""GATE {q.get('year')} Computer Science Previous Year Question
Paper: {q.get('paper')}
Question Number: {q.get('question_number')}
Question Type: {q.get('question_type')}
Marks: {q.get('marks')}

Question:
{q.get('question_text', '')}
"""

    if options_text:
        document += f"""
Options:
{options_text}
"""

    document += f"""
Answer:
{answer_text}
"""

    documents.append({
        "id": f"{q.get('year')}_{q.get('paper')}_Q{q.get('question_number')}",
        "text": document.strip(),
        "metadata": {
            "year": q.get("year"),
            "paper": q.get("paper"),
            "question_number": q.get("question_number"),
            "question_type": q.get("question_type"),
            "marks": q.get("marks"),
            "answer": answer,
            "source_file": q.get("source_file")
        }
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2, ensure_ascii=False)

print("=" * 70)
print("RAG DOCUMENT PREPARATION COMPLETE")
print("=" * 70)
print(f"Questions processed : {len(questions)}")
print(f"Documents created   : {len(documents)}")
print(f"Saved → {OUTPUT_FILE}")
