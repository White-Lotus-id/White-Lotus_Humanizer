#!/usr/bin/env python3
"""
verify_citations.py
-------------------
Citation verification utility for Institutional thesis skill.

Parses a list of APA 7th references submitted by the student, checks
format compliance, and flags issues for review before generation.

Usage:
    python scripts/verify_citations.py --input citations.txt
    python scripts/verify_citations.py --inline "Author, A. (2023). Title. Journal."

Output:
    Structured verification report with flags:
    - [OK] — format appears compliant
    - [FORMAT WARNING: X] — APA 7th formatting issue detected
    - [MISSING FIELD: X] — required APA field absent
    - [NEEDS SEARCH] — cannot verify without web search
"""

import argparse
import re
import sys


# ---- APA 7th basic pattern checks ----

def check_year_format(citation: str) -> list[str]:
    """Check that year appears in parentheses after author."""
    issues = []
    if not re.search(r'\(\d{4}\)', citation):
        issues.append("MISSING FIELD: Year not found in (YYYY) format")
    return issues


def check_author_format(citation: str) -> list[str]:
    """Basic check for Last, F. I. pattern."""
    issues = []
    # Very basic: check for comma after first word (Last name pattern)
    first_token = citation.split(',')[0].strip()
    if len(first_token.split()) > 2:
        issues.append(
            "FORMAT WARNING: Author name may not follow Last, F. I. format"
        )
    return issues


def check_doi_or_url(citation: str) -> list[str]:
    """Check for DOI or URL presence for journal articles."""
    issues = []
    has_doi = bool(re.search(r'https?://doi\.org', citation, re.IGNORECASE))
    has_url = bool(re.search(r'https?://', citation))
    has_volume = bool(re.search(r',\s*\d+\(', citation))  # volume(issue) pattern

    # If looks like a journal article (has volume/issue) but no DOI
    if has_volume and not has_doi and not has_url:
        issues.append(
            "MISSING FIELD: Journal article appears to be missing DOI or URL"
        )
    return issues


def check_title_case(citation: str) -> list[str]:
    """
    APA 7th uses sentence case for article/book titles (only first word and
    proper nouns capitalized). Cannot fully verify programmatically, but flag
    if multiple title-case words appear in sequence.
    """
    issues = []
    # Look for a run of 3+ capitalized words (excluding known proper nouns
    # heuristic — this is imperfect but catches obvious cases)
    if re.search(r'([A-Z][a-z]+\s){3,}', citation):
        issues.append(
            "FORMAT WARNING: Title may be in title case (APA 7th requires "
            "sentence case for article/book titles)"
        )
    return issues


def check_hanging_indent_note(citation: str) -> list[str]:
    """
    Hanging indent is a Word formatting requirement, not verifiable in plain
    text. Just remind.
    """
    return ["NOTE: Verify hanging indent applied in Word document (APA 7th)"]


# ---- Main verification logic ----

def verify_citation(citation: str, index: int) -> dict:
    """Run all checks on a single citation string."""
    citation = citation.strip()
    if not citation:
        return {}

    issues = []
    issues.extend(check_year_format(citation))
    issues.extend(check_author_format(citation))
    issues.extend(check_doi_or_url(citation))
    issues.extend(check_title_case(citation))

    status = "OK" if not [i for i in issues if "WARNING" in i or "MISSING" in i] else "NEEDS REVIEW"

    return {
        "index": index,
        "citation": citation,
        "status": status,
        "issues": issues,
        "search_needed": True  # Always flag for web search verification
    }


def format_report(results: list[dict]) -> str:
    """Format verification results as a readable report."""
    lines = []
    lines.append("=" * 60)
    lines.append("CITATION VERIFICATION REPORT")
    lines.append("Institutional Thesis Skill — APA 7th Edition Check")
    lines.append("=" * 60)
    lines.append("")

    for r in results:
        if not r:
            continue
        lines.append(f"[{r['index']}] {r['citation'][:80]}...")
        lines.append(f"    Status: [{r['status']}]")
        for issue in r["issues"]:
            lines.append(f"    -> {issue}")
        if r["search_needed"]:
            lines.append(
                "    -> [NEEDS SEARCH] Web search recommended for abstract "
                "verification"
            )
        lines.append("")

    lines.append("=" * 60)
    lines.append(
        f"Total citations checked: {len([r for r in results if r])}"
    )
    flagged = len(
        [r for r in results if r and r["status"] == "NEEDS REVIEW"]
    )
    lines.append(f"Flagged for review: {flagged}")
    lines.append("=" * 60)

    return "\n".join(lines)


# ---- CLI entry point ----

def main():
    parser = argparse.ArgumentParser(
        description="Verify APA 7th citations for Institutional thesis skill"
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Path to a plain text file with one citation per line"
    )
    parser.add_argument(
        "--inline",
        type=str,
        help="Single citation string to verify"
    )

    args = parser.parse_args()

    citations = []

    if args.inline:
        citations = [args.inline]
    elif args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                citations = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
    else:
        print(
            "Usage: python verify_citations.py --input FILE or --inline 'CITATION'",
            file=sys.stderr
        )
        sys.exit(1)

    results = [verify_citation(c, i + 1) for i, c in enumerate(citations)]
    report = format_report(results)
    print(report)


if __name__ == "__main__":
    main()
