#!/bin/bash
# Script to generate all PDF files from Spanish exercise markdown files
# Always generates all cuadernillos for all units in both languages

set -e

# Check if virtual environment exists (look in project root)
if [ ! -d "../../venv" ]; then
    echo "Virtual environment not found. Running setup..."
    cd "$(dirname "$0")"  # Ensure we're in the scripts directory
    ./setup.sh
fi

# Activate virtual environment from project root
source ../../venv/bin/activate

echo "🚀 Generating all PDF files..."
echo ""

# Update website markdown files for preview functionality
echo "📄 Updating website preview data..."
if [[ -f "../../website/copy-markdown.js" ]]; then
    cd ../../website
    node copy-markdown.js
    cd - > /dev/null
    echo "✅ Website preview data updated"
else
    echo "⚠️  Website copy script not found, skipping website update"
fi
echo ""

# Generate all PDFs for all languages and units
echo "📚 Generating all PDFs..."
python generate_pdfs.py
echo ""

# Deactivate virtual environment
deactivate

echo "✅ Done! PDFs are ready for printing in DIN A5 format."
echo ""

# Check PDF page counts
echo "📄 Verifying PDF page counts..."
FAILED_PDFS=()
TOTAL_PDFS=0
CORRECT_PDFS=0

# Find all generated PDFs and check their page counts
while IFS= read -r -d '' pdf_file; do
    if [[ -f "$pdf_file" ]]; then
        TOTAL_PDFS=$((TOTAL_PDFS + 1))
        PAGE_COUNT=$(pdfinfo "$pdf_file" 2>/dev/null | grep "Pages:" | awk '{print $2}')
        if [[ "$PAGE_COUNT" != "6" ]]; then
            FAILED_PDFS+=("$pdf_file (${PAGE_COUNT:-unknown} pages)")
            echo "❌ $pdf_file has ${PAGE_COUNT:-unknown} pages (expected: 6)"
        else
            CORRECT_PDFS=$((CORRECT_PDFS + 1))
        fi
    fi
done < <(find ../../website/public/pdfs -name "*.pdf" -print0 2>/dev/null)

if [[ ${#FAILED_PDFS[@]} -gt 0 ]]; then
    echo ""
    echo "⚠️  WARNING: The following PDFs do not have exactly 6 pages:"
    for failed_pdf in "${FAILED_PDFS[@]}"; do
        echo "   - $failed_pdf"
    done
    echo ""
    echo "Each cuadernillo should have exactly 6 pages (one per exercise type)."
    echo "Please check the content for page overflow or underflow issues."
    exit 1
else
    echo "✅ All $TOTAL_PDFS PDFs have exactly 6 pages as expected!"
fi