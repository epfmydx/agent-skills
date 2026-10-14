#!/usr/bin/env python3
"""Combine canonical references into the human edition, preserving its introduction."""

import argparse
from pathlib import Path
import re


REFERENCE_ORDER = (
    "workflow-design.md",
    "visual-craft.md",
    "apple-platforms.md",
    "accessibility.md",
    "evaluation.md",
    "examples.md",
    "evidence.md",
    "collaboration.md",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    guide = root / "UI-UX-DESIGN-GUIDE.md"
    current = guide.read_text(encoding="utf-8")
    first_heading = (root / "references" / REFERENCE_ORDER[0]).read_text(encoding="utf-8").splitlines()[0]
    marker = "\n#" + first_heading + "\n"
    if marker not in current:
        parser.error("Cannot locate the first reference heading; preserve the human introduction manually")
    intro = current.split(marker, 1)[0].rstrip()
    sections = []
    for name in REFERENCE_ORDER:
        source = (root / "references" / name).read_text(encoding="utf-8").strip()
        # Promote reference headings one level deeper, excluding fenced examples.
        lines = []
        fence = None
        for line in source.splitlines():
            match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
            if match:
                token = match.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
                lines.append(line)
            else:
                lines.append("#" + line if fence is None and re.match(r"^#{1,5} ", line) else line)
        sections.append("\n".join(lines))
    expected = intro + "\n\n" + "\n\n".join(sections) + "\n"
    if args.check:
        if current != expected:
            parser.exit(1, "Guide differs from canonical references; run build_guide.py\n")
        print("Guide matches canonical references.")
    else:
        guide.write_text(expected, encoding="utf-8")
        print("Updated human guide from canonical references.")


if __name__ == "__main__":
    main()
