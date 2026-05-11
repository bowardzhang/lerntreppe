# LernTreppe — Claude Instructions

## Git Workflow

After pushing changes to any feature branch:

1. **Immediately create a PR** (non-draft, base: `main`) — do not ask for confirmation.
2. **Immediately merge the PR** (squash merge) into `main` — do not ask for confirmation.
3. Delete the feature branch after merging.

This applies to all repositories in this project (`lerntreppe`, `Schule-Uebungen`).

## Repository Scope

- Exercises: `bowardzhang/Schule-Uebungen` (private, source PDFs)
- Website/DB: `bowardzhang/lerntreppe` (seed files, questions.db, db.json, knowledge-index.json)

## Seed File Conventions

- File: `scripts/seeds/<ID>_seed.py`
- Export: `EXERCISE` dict, `QUESTIONS` list, `NEW_KNOWLEDGE` list
- After adding seeds: run `python3 scripts/build_db.py` then `python3 scripts/export_json.py` from repo root
- Knowledge IDs must match nodes in `knowledge-index.json`
- Do NOT link magic squares or similar arithmetic puzzles to multiplication knowledge nodes
- Per question, `has_image`/`image` is the prompt illustration, `has_answer_image`/`answer_image` (optional) is a separate image shown with the answer (e.g., a sample drawing to compare against). Both default to False/None.
