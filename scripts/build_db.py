#!/usr/bin/env python3
"""
build_db.py – Create and seed the LernTreppe question database.

Run from the repo root:  python3 scripts/build_db.py
"""

import json
import sqlite3
import os

DB_PATH = "data/questions.db"
os.makedirs("data", exist_ok=True)

# ── Schema ────────────────────────────────────────────────────────────────────

SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

-- One row per PDF exercise set (original + answer sheet pair)
CREATE TABLE IF NOT EXISTS exercises (
    id          TEXT PRIMARY KEY,   -- e.g. "0021"
    subject     TEXT NOT NULL,      -- "Deutsch" | "Mathe" | "HSU"
    grade       INTEGER NOT NULL,   -- 1..4
    title       TEXT,               -- header title from PDF
    topic       TEXT,               -- topic line from PDF
    publisher   TEXT,               -- e.g. "CATLUX"
    source_pdf  TEXT NOT NULL,      -- filename of exercise PDF
    answer_pdf  TEXT,               -- filename of answer-key PDF
    total_points REAL,
    created_at  TEXT DEFAULT (datetime('now'))
);

-- One row per question within an exercise
CREATE TABLE IF NOT EXISTS questions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise_id     TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
    question_number INTEGER NOT NULL,           -- 1-based within exercise
    question_type   TEXT,                       -- free-form label
    question_text   TEXT NOT NULL,
    answer_text     TEXT,                       -- short final answer
    answer_steps    TEXT,                       -- JSON array of solution steps
    max_points      REAL,
    has_image       INTEGER NOT NULL DEFAULT 0, -- 0|1
    image_path      TEXT,                       -- relative path under data/img/
    UNIQUE(exercise_id, question_number)
);

-- Many-to-many: question ↔ knowledge-index node
CREATE TABLE IF NOT EXISTS question_knowledge (
    question_id  INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    knowledge_id TEXT NOT NULL,   -- ID from knowledge-index.json
    PRIMARY KEY (question_id, knowledge_id)
);

-- Future: per-user attempt history (skeleton for now)
CREATE TABLE IF NOT EXISTS attempts (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id      TEXT NOT NULL,
    question_id  INTEGER NOT NULL REFERENCES questions(id),
    is_correct   INTEGER,         -- NULL=skipped, 0=wrong, 1=correct
    answer_given TEXT,
    attempted_at TEXT DEFAULT (datetime('now'))
);
"""

# ── Seed data ─────────────────────────────────────────────────────────────────

EXERCISE = {
    "id":          "0021",
    "subject":     "Mathe",
    "grade":       4,
    "title":       "Lernzielkontrolle – Grundschule Klasse 4 Mathematik",
    "topic":       "Zahlenraum bis 10 000: schriftliche Addition, schriftliche Subtraktion, schriftliche Multiplikation, halbschriftliche Division, Sachaufgaben",
    "publisher":   "CATLUX",
    "source_pdf":  "0021.pdf",
    "answer_pdf":  "0021 (1).pdf",
    "total_points": 41,
}

QUESTIONS = [
    {
        "n": 1,
        "type": "Vorgänger und Nachfolger",
        "text": (
            "Trage die Nachbarzahlen ein!\n"
            "Vorgänger  [___]  3100  [___]  Nachfolger\n"
            "Vorgänger  [___]  7779  [___]  Nachfolger\n"
            "Vorgänger  [___]  4000  [___]  Nachfolger"
        ),
        "answer": (
            "3099 | 3100 | 3101\n"
            "7778 | 7779 | 7780\n"
            "3999 | 4000 | 4001"
        ),
        "steps": [],
        "points": 3,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.vorgaenger_nachfolger",
            "mathe.klasse4.zahlen1000000.stellenwerte",
        ],
    },
    {
        "n": 2,
        "type": "Zahlenvergleich",
        "text": (
            "Setze ein: >, < oder =\n"
            "1305 ___ 1350\n"
            "4149 ___ 4419\n"
            "9998 ___ 9989\n"
            "2438 ___ 2438"
        ),
        "answer": "< | < | > | =",
        "steps": [],
        "points": 2,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.vergleichen",
        ],
    },
    {
        "n": 3,
        "type": "Zahlenfolge",
        "text": (
            "Setze die Zahlenfolgen fort!\n"
            "3750  3810  3870  3930  ___  ___  ___\n"
            "8690  8660  8620  8570  ___  ___  ___"
        ),
        "answer": (
            "3990  4050  4110  (Differenz jeweils +60)\n"
            "8510  8440  8360  (Differenz wächst: −30, −40, −50, −60, −70, −80)"
        ),
        "steps": [
            "Reihe 1: Differenz = +60 → 3930+60=3990, 3990+60=4050, 4050+60=4110",
            "Reihe 2: Differenzen nehmen um 10 zu: −30,−40,−50,−60,−70,−80 → 8570−60=8510, 8510−70=8440, 8440−80=8360",
        ],
        "points": 3,
        "knowledge": [
            "mathe.klasse4.zahlen1000000.zahlenfolgen",
        ],
    },
    {
        "n": 4,
        "type": "Schriftliche Addition und Subtraktion",
        "text": (
            "Rechne schriftlich!\n"
            "  2498 + 3098 =\n"
            "  4065 + 5783 =\n"
            "  8764 − 5578 =\n"
            "  6908 − 5086 ="
        ),
        "answer": "5596 | 9848 | 3186 | 1822",
        "steps": [
            "2498 + 3098 = 5596",
            "4065 + 5783 = 9848",
            "8764 − 5578 = 3186",
            "6908 − 5086 = 1822",
        ],
        "points": 4,
        "knowledge": [
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
        ],
    },
    {
        "n": 5,
        "type": "Sachaufgabe (Subtraktion)",
        "text": (
            "Familie Schmidt fährt mit ihrem neuen Auto in den Urlaub. "
            "Vor der Abfahrt zeigt der Tachometerstand 4769 km. "
            "Als sie wieder zu Hause sind, zeigt der Tachometerstand 6045 km.\n"
            "Wie viel Kilometer ist Familie Schmidt gefahren?"
        ),
        "answer": "Sie sind 1276 km gefahren.",
        "steps": [
            "Rechnung: 6045 km − 4769 km = 1276 km",
            "Antwort: Sie sind 1276 km gefahren.",
        ],
        "points": 3,
        "knowledge": [
            "mathe.klasse4.schriftlich.subtraktion",
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 6,
        "type": "Halbschriftliche Division",
        "text": (
            "Rechne halbschriftlich.\n"
            "246 : 3 =\n"
            "765 : 8 ="
        ),
        "answer": "246 : 3 = 82 | 765 : 8 = 95 R 5",
        "steps": [
            "246 : 3: 210:3=70, 36:3=12 → 70+12=82",
            "765 : 8: 720:8=90, 45:8=5 R5 → 95 R5",
        ],
        "points": 4,
        "knowledge": [
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
    {
        "n": 7,
        "type": "Schriftliche Multiplikation",
        "text": (
            "Multipliziere schriftlich. Vergiss den Überschlag nicht!\n"
            "467 · 5  Ü: ___\n"
            "273 · 22  Ü: ___"
        ),
        "answer": "467 · 5 = 2335 (Ü: 500·5=2500) | 273 · 22 = 6006 (Ü: 300·20=6000)",
        "steps": [
            "467 · 5: Überschlag 500·5=2500 → Ergebnis 2335",
            "273 · 22: 273·2=546, 273·20=5460 → 546+5460=6006; Überschlag 300·20=6000",
        ],
        "points": 4,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
        ],
    },
    {
        "n": 8,
        "type": "Umkehraufgabe",
        "text": (
            "Ich teile meine Zahl durch 12 und zähle dann 48 hinzu. "
            "Das Ergebnis lautet 670.\n"
            "Wie heißt meine Zahl?"
        ),
        "answer": "Die Zahl heißt 7464.",
        "steps": [
            "670 − 48 = 622",
            "622 · 12 = 7464",
            "Antwort: Die Zahl heißt 7464.",
        ],
        "points": 2,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.umkehraufgaben",
            "mathe.klasse4.schriftlich.multiplikation",
        ],
    },
    {
        "n": 9,
        "type": "Umkehraufgabe",
        "text": (
            "Wenn ich von meiner Zahl 378 abziehe und das Ergebnis durch 9 teile, "
            "erhalte ich 8.\n"
            "Wie heißt die Zahl?"
        ),
        "answer": "Die Zahl heißt 450.",
        "steps": [
            "8 · 9 = 72",
            "378 + 72 = 450",
            "Antwort: Die Zahl heißt 450.",
        ],
        "points": 2,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.umkehraufgaben",
            "mathe.klasse4.schriftlich.division_halbschriftlich",
        ],
    },
    {
        "n": 10,
        "type": "Sachaufgabe (Multiplikation)",
        "text": (
            'Eine Geschirrspülmaschine der Marke „SuperX“ verbraucht bei einem '
            "Spülgang 23 Liter Wasser.\n"
            "Wie viel Liter Wasser verbraucht ein Haushalt in einem Jahr, "
            "wenn die Maschine jeden Tag läuft?"
        ),
        "answer": "Ein Haushalt verbraucht im Jahr 8395 Liter.",
        "steps": [
            "365 Tage · 23 L = 8395 L",
            "Antwort: Ein Haushalt verbraucht im Jahr 8395 Liter.",
        ],
        "points": 2,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.sachaufgaben.mehrstufig",
        ],
    },
    {
        "n": 11,
        "type": "Multiplikation (Vielfaches)",
        "text": "Berechne das Siebenfache von 345!",
        "answer": "2415",
        "steps": ["345 · 7 = 2415"],
        "points": 2,
        "knowledge": [
            "mathe.klasse4.schriftlich.multiplikation",
        ],
    },
    {
        "n": 12,
        "type": "Zahlenstrahl",
        "text": (
            "Trage die fehlenden Zahlen ein und verbinde die Zahlen unten "
            "mit dem Zahlenstrahl!\n"
            "(Zahlenstrahl von 6600 bis 7200; gegeben: 6650, 7040, 7170)"
        ),
        "answer": "Fehlende Zahlen: 6700, 6860, 7220",
        "steps": [
            "Die leeren Kästchen oben am Zahlenstrahl zeigen: 6700, 6860, 7220",
            "Unten vorgegeben: 6650 → Pfeil auf 6650; 7040 → Pfeil auf 7040; 7170 → Pfeil auf 7170",
        ],
        "points": 3,
        "has_image": True,
        "image": "0021_q12_zahlenstrahl.png",
        "knowledge": [
            "mathe.klasse4.zahlen1000000.zahlenstrahl",
        ],
    },
    {
        "n": 13,
        "type": "Zahlenrätsel",
        "text": (
            "Zahlenrätsel: Addiere zur größtmöglichen vierstelligen Zahl "
            "aus den Ziffern 4, 6, 5 und 2 die kleinstmögliche vierstellige "
            "Zahl aus den Ziffern 9, 2, 7 und 3. Wie heißt die Summe?"
        ),
        "answer": "Die Zahl heißt 8921.",
        "steps": [
            "Größte Zahl aus 4,6,5,2: 6542",
            "Kleinste Zahl aus 9,2,7,3: 2379",
            "6542 + 2379 = 8921",
        ],
        "points": 1,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.zahlenraetsel",
            "mathe.klasse4.zahlen1000000.stellenwerte",
            "mathe.klasse4.schriftlich.addition",
        ],
    },
    {
        "n": 14,
        "type": "Mehrstufige Sachaufgabe",
        "text": (
            "Familie Meier kauft Weihnachtsgeschenke für die ganze Familie! "
            "Der 18-jährige Sohn bekommt einen Fernseher für 859 €, "
            "die 16-jährige Schwester wünscht sich eine neue Stereoanlage für 974 €. "
            "Außerdem kaufen sie 6 neue Videokassetten zu je 6 €. "
            "Mutter braucht dringend einen Wäschetrockner, der 1720 € kostet. "
            "Sie können den Preis etwas herunterhandeln, weil ein kleiner Lackschaden "
            "daran ist und bezahlen deshalb 140 € weniger. "
            "Sie zahlen 1449 € an und möchten den Rest in 20 gleichen Raten abzahlen.\n"
            "Wie viel beträgt eine Rate?"
        ),
        "answer": "Eine Rate beträgt 100 €.",
        "steps": [
            "Wäschetrockner nach Rabatt: 1720 − 140 = 1580 €",
            "Gesamtbetrag: 859 + 974 + 6·6 + 1580 = 859 + 974 + 36 + 1580 = 3449 €",
            "Restbetrag: 3449 − 1449 = 2000 €",
            "Rate: 2000 ÷ 20 = 100 €",
            "Antwort: Eine Rate beträgt 100 €.",
        ],
        "points": 6,
        "knowledge": [
            "mathe.klasse4.sachaufgaben.mehrstufig",
            "mathe.klasse4.schriftlich.addition",
            "mathe.klasse4.schriftlich.subtraktion",
            "mathe.klasse4.schriftlich.multiplikation",
            "mathe.klasse4.schriftlich.division",
        ],
    },
]

# ── Build ─────────────────────────────────────────────────────────────────────

def build():
    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)

    cur = con.cursor()

    # Upsert exercise
    cur.execute("""
        INSERT OR REPLACE INTO exercises
            (id, subject, grade, title, topic, publisher, source_pdf, answer_pdf, total_points)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        EXERCISE["id"], EXERCISE["subject"], EXERCISE["grade"],
        EXERCISE["title"], EXERCISE["topic"], EXERCISE["publisher"],
        EXERCISE["source_pdf"], EXERCISE["answer_pdf"], EXERCISE["total_points"],
    ))

    for q in QUESTIONS:
        cur.execute("""
            INSERT OR REPLACE INTO questions
                (exercise_id, question_number, question_type, question_text,
                 answer_text, answer_steps, max_points, has_image, image_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            EXERCISE["id"], q["n"], q["type"], q["text"],
            q["answer"], json.dumps(q.get("steps", []), ensure_ascii=False),
            q["points"],
            1 if q.get("has_image") else 0,
            q.get("image"),
        ))
        qid = cur.lastrowid

        for kid in q.get("knowledge", []):
            cur.execute("""
                INSERT OR IGNORE INTO question_knowledge (question_id, knowledge_id)
                VALUES (?, ?)
            """, (qid, kid))

    con.commit()
    con.close()

    # Quick summary
    con2 = sqlite3.connect(DB_PATH)
    rows = con2.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    krows = con2.execute("SELECT COUNT(*) FROM question_knowledge").fetchone()[0]
    con2.close()
    print(f"✓ Database built: {rows} questions, {krows} knowledge links → {DB_PATH}")


if __name__ == "__main__":
    build()
