from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEMPLATES = {
    "problem-framing.md": "# Problem framing\n\n[replace with the decision, owner, action, unit of observation, assumptions, risks, and success criteria]\n",
    "implementation-test-plan.md": "# Implementation and test plan\n\n[replace with the planned steps plus normal, empty, invalid-input, and reproducibility tests]\n",
    "rubric-evidence.md": "# Rubric evidence map\n\n[replace with concise links from each rubric criterion to code, output, test, or explanation]\n",
    "change-record.md": "# Part B change record\n\n[replace with each change made after the preserved Part A commit and why it was made]\n",
    "ai-use-declaration.md": "# AI-use declaration\n\n[replace with tools used, purpose, prompts/assistance summarized, verification performed, and what you changed]\n",
    "README.md": "# Lab evidence\n\n[replace with exact setup, run, test, database, app-page, and evidence reproduction commands]\n",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create one lab's evidence and SQL workspace files.")
    parser.add_argument("--lab", type=int, choices=range(1, 11), required=True)
    args = parser.parse_args()
    evidence = ROOT / "evidence" / f"lab_{args.lab:02d}"
    evidence.mkdir(parents=True, exist_ok=True)
    for name, content in TEMPLATES.items():
        path = evidence / name
        if not path.exists():
            path.write_text(content, encoding="utf-8", newline="\n")
    sql = ROOT / "workspace_sql" / f"lab_{args.lab:02d}.sql"
    sql.parent.mkdir(parents=True, exist_ok=True)
    if not sql.exists():
        sql.write_text(
            "-- Optional reproducible workspace changes for this lab.\n"
            "-- Never modify shared_* schemas. Use only your assigned ws_* schema.\n",
            encoding="utf-8",
            newline="\n",
        )
    print(f"Prepared {evidence.relative_to(ROOT)} and {sql.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())