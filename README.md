# LernTreppe

A progressive learning platform for German primary-school students (Klasse 1–4),
covering **Deutsch**, **Mathe**, and **HSU** (Heimat- und Sachunterricht).

The site presents a hierarchical knowledge tree of curriculum topics; each
exercise sheet ("Übungsblatt") is linked to one or more knowledge nodes, so
students can drill down from a subject to a specific concept and find practice
material that targets it.

## Live site

https://bowardzhang.github.io/lerntreppe/

## Repository layout

```
lerntreppe/
├── index.html              Knowledge-tree browser (lists all exercises per subject)
├── exercise.html           Single-exercise viewer with questions, answers, hints
├── knowledge-index.json    Curriculum tree (subjects → grades → topics → leaves)
├── data/
│   ├── questions.db        SQLite database — single source of truth for exercises
│   └── db.json             Web-facing snapshot exported from questions.db
└── scripts/
    ├── seeds/              Per-exercise Python seed files (development input)
    ├── build_db.py         Compiles seed files → data/questions.db
    └── export_json.py      Exports data/questions.db → data/db.json
```

## Current architecture (development phase)

```
                     ┌────────────────────────────────┐
   developer edits   │  scripts/seeds/<id>_seed.py    │
                     └────────────────────────────────┘
                                  │
                  python3 scripts/build_db.py
                                  ▼
                     ┌────────────────────────────────┐
                     │       data/questions.db        │  ← single source of truth
                     │           (SQLite)             │
                     └────────────────────────────────┘
                                  │
                python3 scripts/export_json.py
                                  ▼
                     ┌────────────────────────────────┐
                     │          data/db.json          │  ← consumed by the static site
                     └────────────────────────────────┘
                                  │
                  fetch('./data/db.json')
                                  ▼
                     ┌────────────────────────────────┐
                     │   index.html / exercise.html   │  ← served by GitHub Pages
                     └────────────────────────────────┘
```

The site is hosted on **GitHub Pages** (static hosting only). Because the
browser cannot run SQL directly against a SQLite file without a heavy WASM
runtime, the data is exported to a JSON snapshot (`data/db.json`) that the
front-end consumes via plain `fetch`. The seed files are the editorial input;
`questions.db` is the canonical store; `db.json` is the read-optimized view
shipped to the browser.

### Rebuilding the database

After editing or adding any seed file:

```bash
python3 scripts/build_db.py    # seeds  → data/questions.db
python3 scripts/export_json.py # questions.db → data/db.json
```

Both files are committed to the repo so GitHub Pages can serve them.

## Planned architecture (post-launch on Railway)

When the project moves to **Railway**, the static-hosting constraint goes away.
The plan is:

- The backend will hold **only `questions.db`** as the single source of truth
  for exercise content — no more `db.json` snapshot.
- The front-end will query the backend over an HTTP API instead of fetching a
  pre-built JSON file.
- The seed files remain the editorial entry point during content authoring,
  and continue to compile into `questions.db`.

This eliminates the JSON export step and removes the duplication between
`questions.db` and `db.json`, ensuring a single canonical store of exercise data.

## Database schema (excerpt)

```sql
exercises          (id, subject, grade, title, topic, total_points, …)
questions          (exercise_id → exercises.id, question_number, question_text,
                    answer_text, answer_steps, max_points, has_image, …)
question_knowledge (question_id → questions.id, knowledge_id)  -- links to knowledge-index.json
attempts           (user_id, question_id, is_correct, …)        -- reserved for the future
```

`knowledge_id` values reference node IDs in `knowledge-index.json`
(e.g. `mathe.klasse4.schriftlich.addition`).

## Tech stack

- **Front-end:** vanilla HTML / CSS / JavaScript, no framework
- **Data pipeline:** Python 3 + SQLite (stdlib only)
- **Hosting (current):** GitHub Pages
- **Hosting (planned):** Railway

## License

See [LICENSE](./LICENSE).
