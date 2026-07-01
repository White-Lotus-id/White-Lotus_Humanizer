#!/usr/bin/env bash
# zip_package.sh
# --------------
# Packages the humanize skill repository into a distributable ZIP archive.
# Excludes development artifacts, caches, and test files.
#
# Usage:
#   bash zip_package.sh
#   bash zip_package.sh --output my-humanize-v6.zip

set -e

VERSION="6.0.0"
DEFAULT_OUTPUT="humanize-v${VERSION}.zip"

OUTPUT="${1:-$DEFAULT_OUTPUT}"

# Parse --output flag
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --output) OUTPUT="$2"; shift ;;
  esac
  shift
done

echo "========================================"
echo "humanize skill — Package Builder"
echo "Version $VERSION"
echo "========================================"
echo ""
echo "Output: $OUTPUT"
echo ""

# Clean up any previous package
if [ -f "$OUTPUT" ]; then
  rm "$OUTPUT"
  echo "Removed previous package: $OUTPUT"
fi

# Create ZIP excluding unwanted files
zip -r "$OUTPUT" . \
  --exclude "*.pyc" \
  --exclude "__pycache__/*" \
  --exclude ".git/*" \
  --exclude ".gitignore" \
  --exclude "*.egg-info/*" \
  --exclude ".DS_Store" \
  --exclude "*.log" \
  --exclude "scratch*.txt" \
  --exclude "draft*.txt" \
  --exclude "test_input*.txt" \
  --exclude "test_chunk*.txt" \
  --exclude "*.zip" \
  --exclude "*.tar.gz" \
  --exclude ".venv/*" \
  --exclude "venv/*"

echo ""
echo "Package created: $OUTPUT"
echo ""

# Show contents
echo "Contents:"
unzip -l "$OUTPUT" | grep -v "^Archive" | grep -v "^---" | awk '{print $NF}' | sort

echo ""
echo "========================================"
echo "Done."
echo "========================================"
