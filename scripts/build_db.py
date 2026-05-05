#!/usr/bin/env python3
"""
build_db.py – Create / update the LernTreppe question database from seed files.

Run from repo root:  python3 scripts/build_db.py

Each seed file in scripts/seeds/*_seed.py must export:
  EXERCISE    dict  – exercise metadata
  QUESTIONS   list  – question dicts
  NEW_KNOWLEDGE list – (optional) new knowledge-index nodes
"""

import glob, importlib.util, json, os, sqlite3, sys

DB_PATH = "data/questions.db"
os.makedirs("data", exist_ok=True)

# ── Schema ────────────────────────────────────────────────────────────────────

SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS exercises (
    id           TEXT PRIMARY KEY,
    subject      TEXT NOT NULL,
    grade        INTEGER NOT NULL,
    title        TEXT,
    topic        TEXT,
    publisher    TEXT,
    source_pdf   TEXT NOT NULL,
    answer_pdf   TEXT,
    total_points REAL,
    created_at   TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS questions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise_id     TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
    question_number INTEGER NOT NULL,
    question_type   TEXT,
    question_text   TEXT NOT NULL,
    answer_text     TEXT,
    answer_steps    TEXT,
    max_points      REAL,
    has_image       INTEGER NOT NULL DEFAULT 0,
    image_path      TEXT,
    UNIQUE(exercise_id, question_number)
);

CREATE TABLE IF NOT EXISTS question_knowledge (
    question_id  INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    knowledge_id TEXT NOT NULL,
    PRIMARY KEY (question_id, knowledge_id)
);

CREATE TABLE IF NOT EXISTS attempts (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id      TEXT NOT NULL,
    question_id  INTEGER NOT NULL REFERENCES questions(id),
    is_correct   INTEGER,
    answer_given TEXT,
    attempted_at TEXT DEFAULT (datetime('now'))
);
"""

# ── Load seed ─────────────────────────────────────────────────────────────────

def load_seed(path):
    spec = importlib.util.spec_from_file_location("seed", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

# ── Insert exercise ───────────────────────────────────────────────────────────

def insert_exercise(con, ex, questions):
    cur = con.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO exercises
            (id, subject, grade, title, topic, publisher, source_pdf, answer_pdf, total_points)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (ex["id"], ex["subject"], ex["grade"], ex.get("title"), ex.get("topic"),
          ex.get("publisher"), ex["source_pdf"], ex.get("answer_pdf"), ex.get("total_points")))

    # Delete existing questions so we can re-insert cleanly
    cur.execute("DELETE FROM questions WHERE exercise_id=?", (ex["id"],))

    for q in questions:
        cur.execute("""
            INSERT INTO questions
                (exercise_id, question_number, question_type, question_text,
                 answer_text, answer_steps, max_points, has_image, image_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            ex["id"], q["n"], q.get("type"), q["text"],
            q.get("answer"),
            json.dumps(q.get("steps", []), ensure_ascii=False),
            q.get("points"), 1 if q.get("has_image") else 0,
            q.get("image"),
        ))
        qid = cur.lastrowid
        for kid in q.get("knowledge", []):
            cur.execute(
                "INSERT OR IGNORE INTO question_knowledge (question_id, knowledge_id) VALUES (?,?)",
                (qid, kid)
            )

# ── Main ──────────────────────────────────────────────────────────────────────

def build():
    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)

    seed_files = sorted(glob.glob("scripts/seeds/*_seed.py"))
    if not seed_files:
        print("No seed files found in scripts/seeds/", file=sys.stderr)
        sys.exit(1)

    total_q = 0
    for path in seed_files:
        m = load_seed(path)
        insert_exercise(con, m.EXERCISE, m.QUESTIONS)
        total_q += len(m.QUESTIONS)
        print(f"  ✓ {m.EXERCISE['id']:6s}  {len(m.QUESTIONS):>2} questions")

    con.commit()

    rows = con.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    exs  = con.execute("SELECT COUNT(*) FROM exercises").fetchone()[0]
    kn   = con.execute("SELECT COUNT(*) FROM question_knowledge").fetchone()[0]
    con.close()

    print(f"\nDatabase: {exs} exercises, {rows} questions, {kn} knowledge links → {DB_PATH}")


if __name__ == "__main__":
    build()
