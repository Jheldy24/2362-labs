from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache", ".streamlit", "submissions"}
FORBIDDEN_NAMES = {"secrets.toml", ".env", "student-profile.json"}
PLACEHOLDERS = ("[replace", "TODO")


def run_git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a clean, reproducible D2L lab submission ZIP.")
    parser.add_argument("--lab", type=int, choices=range(1, 11), required=True)
    parser.add_argument("--part", choices=("A", "B"), required=True)
    args = parser.parse_args()

    if run_git("status", "--porcelain"):
        raise SystemExit("Commit your intended work and remove untracked files before packaging.")
    commit = run_git("rev-parse", "HEAD")
    files = [Path(value) for value in run_git("ls-files").splitlines() if value]
    evidence_root = Path("evidence") / f"lab_{args.lab:02d}"
    required = {
        evidence_root / "README.md",
        evidence_root / "problem-framing.md",
        evidence_root / "implementation-test-plan.md",
        evidence_root / "rubric-evidence.md",
        evidence_root / "ai-use-declaration.md",
    }
    if args.part == "B":
        required.add(evidence_root / "change-record.md")
    missing = sorted(str(path) for path in required if path not in files or not (ROOT / path).is_file())
    if missing:
        raise SystemExit("Missing committed evidence files: " + ", ".join(missing))
    for path in required:
        text = (ROOT / path).read_text(encoding="utf-8")
        if any(marker.lower() in text.lower() for marker in PLACEHOLDERS):
            raise SystemExit(f"Finish the evidence template before packaging: {path}")

    payload: list[tuple[Path, bytes]] = []
    for relative in files:
        if any(part in FORBIDDEN_PARTS for part in relative.parts) or relative.name in FORBIDDEN_NAMES:
            continue
        source = ROOT / relative
        if source.is_file():
            payload.append((relative, source.read_bytes()))
    manifest = {
        "course": "Geographic Information Systems",
        "lab": f"LAB{args.lab:02d}",
        "part": args.part,
        "git_commit": commit,
        "files": [{"path": path.as_posix(), "sha256": digest(data)} for path, data in payload],
    }
    manifest_data = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    output = ROOT / "submissions" / f"LAB{args.lab:02d}-{args.part}-{commit[:8]}.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, data in payload:
            archive.writestr(path.as_posix(), data)
        archive.writestr("SUBMISSION-MANIFEST.json", manifest_data)
    print(f"PASS: {output.relative_to(ROOT)} contains {len(payload)} tracked files from {commit}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())