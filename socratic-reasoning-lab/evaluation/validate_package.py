#!/usr/bin/env python3
"""Check package integrity, not reasoning quality. Uses only the standard library."""
from __future__ import annotations
import json
from pathlib import Path
import re
import sys

def validate(root: Path) -> list[str]:
    errors = []
    root = root.resolve()
    required = ["SKILL.md", "README.md", "README.en.md", "LICENSE", "NOTICE.md",
                "agents/openai.yaml", "evaluation/cases.json", "evaluation/REPORT.md"]
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing file: {name}")
    skill = root / "SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append("SKILL.md must contain YAML frontmatter")
        else:
            front = text[4:].split("\n---\n", 1)[0]
            if not re.search(r"^name: socratic-reasoning-lab$", front, re.M):
                errors.append("Unexpected skill name")
            if not re.search(r"^description: .+", front, re.M):
                errors.append("Missing description")
        if len(text.splitlines()) >= 500:
            errors.append("Entrypoint exceeds repository line guidance")
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            errors.append(f"Symlink is not allowed in this package: {path.relative_to(root)}")
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".json", ".yaml", ".py"} and path.name != "LICENSE":
            errors.append(f"Unexpected file type: {path.relative_to(root)}")
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                    continue
                resolved = (path.parent / target.split("#", 1)[0]).resolve()
                if not resolved.is_relative_to(root):
                    errors.append(f"Link escapes package: {path.relative_to(root)} -> {target}")
                elif not resolved.exists():
                    errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")
        if path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, UnicodeError) as exc:
                errors.append(f"Invalid JSON: {path.relative_to(root)}: {exc}")
    cases_path = root / "evaluation/cases.json"
    if cases_path.is_file():
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
        if not isinstance(cases, list):
            errors.append("Cases must be a list")
        else:
            ids = [case.get("id") for case in cases]
            if any(not value for value in ids) or len(ids) != len(set(ids)):
                errors.append("Case IDs must be nonempty and unique")
            if any(not case.get("prompt") or not case.get("domain") for case in cases):
                errors.append("Each case needs a prompt and domain")
    return errors

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("Package integrity checks passed. Behavioral effectiveness is not established by this check.")

