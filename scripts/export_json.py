#!/usr/bin/env python3
"""Export questions.db to data/db.json for the static frontend."""

import json, sqlite3, os

DB_PATH  = "data/questions.db"
OUT_PATH = "data/db.json"

con = sqlite3.connect(DB_PATH)
con.row_factory = sqlite3.Row

exercises = []
for ex in con.execute("SELECT * FROM exercises ORDER BY subject, grade, id"):
    questions = []
    for q in con.execute(
        "SELECT * FROM questions WHERE exercise_id=? ORDER BY question_number",
        (ex["id"],)
    ):
        kids = [r[0] for r in con.execute(
            "SELECT knowledge_id FROM question_knowledge WHERE question_id=? ORDER BY knowledge_id",
            (q["id"],)
        )]
        questions.append({
            "id":              q["id"],
            "question_number": q["question_number"],
            "question_type":   q["question_type"],
            "question_text":   q["question_text"],
            "answer_text":     q["answer_text"],
            "answer_steps":    json.loads(q["answer_steps"] or "[]"),
            "max_points":      q["max_points"],
            "has_image":       bool(q["has_image"]),
            "image_path":      q["image_path"],
            "knowledge":       kids,
        })

    exercises.append({
        "id":           ex["id"],
        "subject":      ex["subject"],
        "grade":        ex["grade"],
        "title":        ex["title"],
        "topic":        ex["topic"],
        "publisher":    ex["publisher"],
        "source_pdf":   ex["source_pdf"],
        "total_points": ex["total_points"],
        "questions":    questions,
    })

con.close()

os.makedirs("data", exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump({"exercises": exercises}, f, ensure_ascii=False, indent=2)

print(f"✓ Exported {len(exercises)} exercise(s) → {OUT_PATH}")
