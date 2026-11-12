#!/usr/bin/env python3
"""Check local Markdown file links and installed skill frontmatter.

No external dependencies or network access. Anchor identifiers and remote URLs
are intentionally out of scope. CI checks repository sources, not external sites.
"""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"!?(?:\[[^\]\n]+\])\((<[^>]+>|[^)\s]+)")
REF = re.compile(r"^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
SKIP = {".git", ".venv", "node_modules", "build", "dist"}


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    for doc in sorted(root.rglob("*.md")):
        if any(part in SKIP for part in doc.relative_to(root).parts):
            continue
        raw = doc.read_text(encoding="utf-8")
        rel = doc.relative_to(root).as_posix()
        if len(doc.relative_to(root).parts) == 3 and rel.startswith("skills/") and rel.endswith("/SKILL.md"):
            lines = raw.splitlines()
            if not lines or lines[0].strip() != "---":
                errors.append(f"{rel}: missing SKILL.md YAML frontmatter")
            else:
                try:
                    stop = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
                except StopIteration:
                    errors.append(f"{rel}: frontmatter not closed")
                else:
                    front = "\n".join(lines[1:stop])
                    for field in ("name", "description"):
                        if not re.search(rf"(?m)^{field}:\s*\S+", front):
                            errors.append(f"{rel}: frontmatter missing {field}")
        fence_marker = None
        for number, line in enumerate(raw.splitlines(), 1):
            marker = FENCE.match(line)
            if marker:
                token = marker.group(1)
                if fence_marker is None:
                    fence_marker = token[0]
                elif token[0] == fence_marker:
                    fence_marker = None
                continue
            if fence_marker:
                continue
            hrefs = [m.group(1) for m in LINK.finditer(line)]
            reference = REF.match(line)
            if reference:
                hrefs.append(reference.group(1))
            for href in hrefs:
                href = href.strip("<>")
                if href.startswith("#") or href.startswith("//") or SCHEME.match(href):
                    continue
                path = unquote(urlsplit(href).path)
                if not path:
                    continue
                target = (doc.parent / path).resolve()
                if not target.is_relative_to(root):
                    errors.append(f"{rel}:{number}: link escapes repository: {href}")
                elif not target.exists():
                    errors.append(f"{rel}:{number}: missing local link target: {href}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    problems = check(args.root)
    for problem in problems:
        print(problem)
    if problems:
        raise SystemExit(f"Documentation check FAILED: {len(problems)} issue(s)")
    print("Documentation check PASSED (relative Markdown paths and skill frontmatter)")
