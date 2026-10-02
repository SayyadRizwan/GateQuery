import json

FILE = "data/questions/questions.json"

with open(FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)

seen = set()
cleaned = []

for q in questions:
    key = (
        q.get("year"),
        q.get("paper"),
        q.get("question_number")
    )

    if key not in seen:
        seen.add(key)
        cleaned.append(q)

removed = len(questions) - len(cleaned)

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=2, ensure_ascii=False)

print("=" * 70)
print("DUPLICATE CLEANUP COMPLETE")
print("=" * 70)
print(f"Original questions : {len(questions)}")
print(f"Removed duplicates : {removed}")
print(f"Final questions    : {len(cleaned)}")
print(f"Saved → {FILE}")