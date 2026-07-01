#!/usr/bin/env python3
"""
intake_prefill.py
-----------------
Intake form pre-population utility for Institutional thesis skill.

Parses partial student input (title, section name, references pasted
as plain text) and pre-fills the Phase 0 intake form so the student
only needs to review and confirm rather than fill everything from scratch.

Usage:
    python scripts/intake_prefill.py --title "TITLE" --section "SECTION" \
        --category development --voice VOICE-A \
        --refs references.txt

Output:
    Pre-filled [SECTION INTAKE] block ready to paste into chat.
"""

import argparse
import sys
import textwrap


VOICE_OPTIONS = ("VOICE-A", "VOICE-B", "BASE")
CATEGORY_OPTIONS = ("Research", "Development")

SECTION_TO_CHAPTER = {
    "introduction": "Chapter 1",
    "background": "Chapter 1",
    "problem statement": "Chapter 1",
    "objectives": "Chapter 1",
    "scope": "Chapter 1",
    "significance": "Chapter 1",
    "framework": "Chapter 1",
    "conceptual framework": "Chapter 1",
    "definition of terms": "Chapter 1",
    "rrl": "Chapter 2",
    "related literature": "Chapter 2",
    "rrs": "Chapter 2",
    "related studies": "Chapter 2",
    "synthesis": "Chapter 2",
    "research design": "Chapter 3",
    "methodology": "Chapter 3",
    "data gathering": "Chapter 3",
    "instrumentation": "Chapter 3",
    "statistical tools": "Chapter 3",
    "results": "Chapter 4",
    "discussion": "Chapter 4",
    "summary": "Chapter 5",
    "conclusions": "Chapter 5",
    "recommendations": "Chapter 5",
}

CHAPTERS_NEEDING_ANCHOR = {"Chapter 3", "Chapter 4", "Chapter 5"}
SECTIONS_NEEDING_THEME_MAP = {"rrl", "rrs", "related literature", "related studies"}


def detect_chapter(section: str) -> str:
    """Detect which chapter a section belongs to."""
    key = section.strip().lower()
    return SECTION_TO_CHAPTER.get(key, "Unknown Chapter")


def needs_thesis_anchor(section: str) -> bool:
    chapter = detect_chapter(section)
    return chapter in CHAPTERS_NEEDING_ANCHOR


def needs_theme_map(section: str) -> bool:
    return section.strip().lower() in SECTIONS_NEEDING_THEME_MAP


def parse_references(refs_text: str) -> list[str]:
    """Split multi-line reference block into individual references."""
    lines = [l.strip() for l in refs_text.strip().splitlines() if l.strip()]
    # Group by blank line or by detecting author-year pattern at line start
    refs = []
    current = []
    for line in lines:
        if current and line and line[0].isupper() and "(" in line[:30]:
            refs.append(" ".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        refs.append(" ".join(current))
    return refs


def build_intake_form(
    title: str,
    category: str,
    section: str,
    voice: str,
    refs: list[str],
    chapter: str
) -> str:
    """Build the full [SECTION INTAKE] block."""

    ref_block = ""
    for i, r in enumerate(refs, 1):
        ref_block += f"   {i}. {r}\n"

    if not ref_block:
        ref_block = "   [NO REFERENCES PROVIDED — ADD BEFORE GENERATING]\n"

    theme_map_block = ""
    if needs_theme_map(section):
        theme_map_block = textwrap.dedent("""
FOR RRL/RRS — Theme Map (REQUIRED):
6. Theme Map:
   Theme 1: [theme name] — [Author(s)]
   Theme 2: [theme name] — [Author(s)]
   [continue for all themes]
""")

    anchor_block = ""
    if needs_thesis_anchor(section):
        anchor_block = textwrap.dedent("""
FOR CHAPTERS 3, 4, 5 — Thesis Anchor (REQUIRED):
7. [THESIS ANCHOR]
   Title: """ + title + """
   Category: """ + category + """
   General Objective: [FILL IN]
   Scope (one sentence): [FILL IN]
   Key methodology: [FILL IN]
""")

    form = f"""[SECTION INTAKE — PRE-FILLED]

Reply with everything in one message.
Review the pre-filled fields and correct any errors before confirming.

REQUIRED:
1. Thesis Title/Topic: {title}
2. Thesis Category: {category}
3. Section/Part: {section} ({chapter})
4. Voice Target: {voice}
5. References ({len(refs)} pre-loaded):
{ref_block}
{theme_map_block}{anchor_block}
OPTIONAL:
   - Research objectives
   - Methodology details
   - Data/results
   - Your writing sample (for voice calibration)
   - Existing draft or bullet list

[Review and confirm or correct above, then reply.]
"""
    return form


def main():
    parser = argparse.ArgumentParser(
        description="Pre-fill Section Intake form for Institutional thesis skill"
    )
    parser.add_argument("--title", required=True, help="Full thesis title")
    parser.add_argument(
        "--section", required=True,
        help="Section to generate (e.g., Introduction, RRL, Research Design)"
    )
    parser.add_argument(
        "--category", default="Development",
        choices=[c.lower() for c in CATEGORY_OPTIONS],
        help="Thesis category: research or development"
    )
    parser.add_argument(
        "--voice", default="VOICE-A",
        choices=VOICE_OPTIONS,
        help="Voice profile: VOICE-A, VOICE-B, or BASE"
    )
    parser.add_argument(
        "--refs", type=str,
        help="Path to plain text file with one reference per line"
    )

    args = parser.parse_args()

    refs = []
    if args.refs:
        try:
            with open(args.refs, "r", encoding="utf-8") as f:
                refs_text = f.read()
            refs = parse_references(refs_text)
        except FileNotFoundError:
            print(
                f"Warning: References file not found: {args.refs}",
                file=sys.stderr
            )

    category = args.category.capitalize()
    chapter = detect_chapter(args.section)

    form = build_intake_form(
        title=args.title,
        category=category,
        section=args.section,
        voice=args.voice,
        refs=refs,
        chapter=chapter
    )

    print(form)


if __name__ == "__main__":
    main()
