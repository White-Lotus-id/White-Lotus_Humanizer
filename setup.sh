#!/usr/bin/env bash
# setup.sh
# --------
# Setup and environment verification script for the humanize skill.
# Run this once after cloning the repository.
#
# Usage:
#   bash setup.sh

set -e

echo "========================================"
echo "humanize skill — Setup"
echo "Version 6.0.0"
echo "========================================"
echo ""

# ---- Python version check ----

echo "[1/4] Checking Python version..."

if ! command -v python3 &>/dev/null; then
  echo "ERROR: python3 not found. Install Python 3.9 or higher."
  exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)')
PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')

if [ "$PYTHON_MAJOR" -lt 3 ] || { [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 9 ]; }; then
  echo "ERROR: Python 3.9+ required. Found: $PYTHON_VERSION"
  exit 1
fi

echo "OK — Python $PYTHON_VERSION"
echo ""

# ---- Script smoke tests ----

echo "[2/4] Verifying scripts are importable..."

python3 -c "import scripts.verify_citations" 2>/dev/null || \
  python3 scripts/verify_citations.py --help > /dev/null 2>&1 && \
  echo "OK — verify_citations.py" || echo "WARNING: verify_citations.py may have issues"

python3 scripts/tier5_audit.py --help > /dev/null 2>&1 && \
  echo "OK — tier5_audit.py" || echo "WARNING: tier5_audit.py may have issues"

python3 scripts/intake_prefill.py --help > /dev/null 2>&1 && \
  echo "OK — intake_prefill.py" || echo "WARNING: intake_prefill.py may have issues"

echo ""

# ---- Reference file presence check ----

echo "[3/4] Checking reference files..."

REFERENCES=(
  "references/voice_base.md"
  "references/voice_a.md"
  "references/voice_b.md"
  "references/humanization_techniques.md"
  "references/tier5_mistake_layer.md"
  "references/bu_format_specs.md"
  "references/apa_citation_rules.md"
  "references/section_templates_ch1.md"
  "references/section_templates_ch2.md"
  "references/section_templates_ch3.md"
  "references/section_templates_ch4_ch5.md"
  "references/conflict_resolution.md"
  "references/authenticity_checklist.md"
)

ALL_OK=true
for ref in "${REFERENCES[@]}"; do
  if [ -f "$ref" ]; then
    echo "OK — $ref"
  else
    echo "MISSING — $ref"
    ALL_OK=false
  fi
done

if [ "$ALL_OK" = false ]; then
  echo ""
  echo "WARNING: Some reference files are missing. The skill will not load"
  echo "correctly in Claude Projects without all reference files."
fi

echo ""

# ---- Claude Projects upload reminder ----

echo "[4/4] Claude Projects setup reminder..."
echo ""
echo "To use this skill in Claude.ai Projects:"
echo "  1. Go to your Project in claude.ai"
echo "  2. Open Project Settings"
echo "  3. Upload SKILL.md as the instructions file"
echo "  4. Upload ALL files from references/ as knowledge files"
echo "  5. Optional: Upload metadata/ files as additional knowledge"
echo ""
echo "Do NOT upload scripts/ to Claude Projects — they are for local use only."
echo ""

echo "========================================"
echo "Setup complete."
echo "========================================"
