#!/usr/bin/env python3
"""
tier5_audit.py
--------------
Tier 5 human mistake layer audit utility for Institutional thesis skill.

Scans a generated thesis chunk for potential Tier 5 mistake patterns and
flags clustering, over-injection, or patterned repetition.

Usage:
    python scripts/tier5_audit.py --input chunk.txt
    python scripts/tier5_audit.py --inline "paste thesis text here"

Output:
    Audit report with counts, clustering warnings, and recommendations.

Note:
    This script uses heuristics only. It does not replace the internal
    Phase 4 authenticity pass. It is a supplementary diagnostic tool.
"""

import argparse
import re
import sys
from collections import defaultdict


# ---- Mistake pattern signatures ----
# These are heuristic pattern checks. They will not catch all injections
# and will occasionally flag non-injected text.

MISTAKE_PATTERNS = {
    "Tense Slip": [
        (r'\bwill\b.{0,30}\bwas\b', "will ... was in same sentence"),
        (r'\bwas\b.{0,30}\bwill\b', "was ... will in same sentence"),
        (r'\bis\b.{0,30}\bwas\b', "is ... was mix"),
    ],
    "Missing Article": [
        (r'\bfrom \d+(st|nd|rd|th)\b', "missing article before ordinal"),
        (r'\b(in|at|on|of) [A-Z][a-z]+ (that|which|when|where|who)\b',
         "possible missing article before noun clause"),
    ],
    "Passive Voice Drift": [
        (r'\bwas (performed|conducted|done|analyzed|collected|measured|tested|evaluated)\b',
         "passive voice in likely active context"),
    ],
    "Throat-Clearing Opening": [
        (r'^There (are|is|were|was) (many|several|various|a number of)',
         "throat-clearing paragraph opener"),
    ],
    "Vague Pronoun": [
        (r'\b(This|That|It) (is|was|are|were|has|have|had) (also|further|therefore|thus|hence)\b',
         "vague pronoun + connector"),
    ],
    "Weak Sentence Ending": [
        (r'(and other related factors|among others|and the like|and so on)\.',
         "weak sentence ending"),
    ],
    "Overly Long Citation Setup": [
        (r'According to the study conducted by .{0,30} which was published in',
         "overly long citation setup"),
    ],
    "Redundant Transition": [
        (r'\.(Also,|In addition,|Furthermore,|Moreover,).{0,50}\.(Also,|In addition,|Furthermore,|Moreover,)',
         "same additive connector used twice in close proximity"),
    ],
}


def split_paragraphs(text: str) -> list[str]:
    """Split text into paragraphs on blank lines."""
    paragraphs = re.split(r'\n\s*\n', text.strip())
    return [p.strip() for p in paragraphs if p.strip()]


def audit_paragraph(paragraph: str, para_index: int) -> dict:
    """Check a single paragraph for Tier 5 patterns."""
    findings = []

    for mistake_type, patterns in MISTAKE_PATTERNS.items():
        for pattern, description in patterns:
            match = re.search(pattern, paragraph, re.IGNORECASE | re.MULTILINE)
            if match:
                findings.append({
                    "type": mistake_type,
                    "description": description,
                    "match": match.group(0)[:60]
                })

    return {
        "para_index": para_index,
        "paragraph_preview": paragraph[:80] + "..." if len(paragraph) > 80 else paragraph,
        "findings": findings,
        "count": len(findings)
    }


def check_clustering(para_audits: list[dict]) -> list[str]:
    """Check for mistake clustering across adjacent paragraphs."""
    warnings = []

    for i in range(len(para_audits) - 1):
        current = para_audits[i]
        nxt = para_audits[i + 1]

        if current["count"] > 0 and nxt["count"] > 0:
            warnings.append(
                f"CLUSTERING WARNING: Paragraphs {current['para_index']} and "
                f"{nxt['para_index']} both have Tier 5 findings. "
                f"Consider removing one."
            )

    return warnings


def check_same_type_repetition(para_audits: list[dict]) -> list[str]:
    """Check for repeated use of the same mistake type across the chunk."""
    warnings = []
    type_counts = defaultdict(int)

    for audit in para_audits:
        for finding in audit["findings"]:
            type_counts[finding["type"]] += 1

    for mistake_type, count in type_counts.items():
        if count >= 2:
            warnings.append(
                f"REPETITION WARNING: '{mistake_type}' pattern detected "
                f"{count} times. Remove at least one."
            )

    return warnings


def count_total_injections(para_audits: list[dict]) -> int:
    """Count total detected injections in the chunk."""
    return sum(a["count"] for a in para_audits)


def format_report(para_audits: list[dict], clustering: list[str],
                  repetition: list[str]) -> str:
    """Format the full audit report."""
    lines = []
    lines.append("=" * 60)
    lines.append("TIER 5 MISTAKE LAYER AUDIT")
    lines.append("Institutional Thesis Skill")
    lines.append("=" * 60)
    lines.append("")

    for audit in para_audits:
        if audit["findings"]:
            lines.append(f"Paragraph {audit['para_index']}:")
            lines.append(f"  Preview: {audit['paragraph_preview']}")
            for f in audit["findings"]:
                lines.append(f"  [{f['type']}] {f['description']}")
                lines.append(f"    Match: \"{f['match']}\"")
            lines.append("")

    total = count_total_injections(para_audits)
    paragraphs = len(para_audits)
    lines.append("-" * 60)
    lines.append(f"Paragraphs scanned: {paragraphs}")
    lines.append(f"Total Tier 5 patterns detected: {total}")
    lines.append("")

    if total == 0:
        lines.append("RESULT: No Tier 5 patterns detected. Acceptable (60% chance of zero).")
    elif total <= 2:
        lines.append("RESULT: Acceptable injection rate.")
    else:
        lines.append(
            f"RESULT: High injection rate ({total}). Consider removing some."
        )

    lines.append("")

    if clustering:
        lines.append("--- CLUSTERING WARNINGS ---")
        for w in clustering:
            lines.append(f"  {w}")
        lines.append("")

    if repetition:
        lines.append("--- REPETITION WARNINGS ---")
        for w in repetition:
            lines.append(f"  {w}")
        lines.append("")

    lines.append("=" * 60)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Audit Tier 5 human mistake injection for Institutional thesis"
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Path to a plain text file containing the thesis chunk"
    )
    parser.add_argument(
        "--inline",
        type=str,
        help="Thesis chunk as a string (wrap in quotes)"
    )

    args = parser.parse_args()

    text = ""

    if args.inline:
        text = args.inline
    elif args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
    else:
        print(
            "Usage: python tier5_audit.py --input FILE or --inline 'TEXT'",
            file=sys.stderr
        )
        sys.exit(1)

    paragraphs = split_paragraphs(text)
    para_audits = [audit_paragraph(p, i + 1) for i, p in enumerate(paragraphs)]
    clustering = check_clustering(para_audits)
    repetition = check_same_type_repetition(para_audits)

    report = format_report(para_audits, clustering, repetition)
    print(report)


if __name__ == "__main__":
    main()
