#!/bin/bash
# Wrapper script to generate PDFs with automatic virtual environment handling
# Supports multilingual generation (Japanese and English versions)

set -e

# Parse command line arguments
CUADERNILLO=""
LANGUAGE=""
UNIT=""
HELP=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -l|--language)
            LANGUAGE="$2"
            shift 2
            ;;
        -u|--unit)
            UNIT="$2"
            shift 2
            ;;
        -h|--help)
            HELP=true
            shift
            ;;
        [1-4])
            CUADERNILLO="$1"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

if [[ "$HELP" == true ]]; then
    echo "Usage: $0 [CUADERNILLO] [OPTIONS]"
    echo ""
    echo "Generate PDF files from Spanish exercise markdown files."
    echo ""
    echo "Arguments:"
    echo "  CUADERNILLO       Cuadernillo number (1, 2, 3, or 4). If not specified, generates all cuadernillos."
    echo ""
    echo "Options:"
    echo "  -l, --language    Language for instructions (japanese, english, or both)"
    echo "                    Default: both (generates PDFs for both languages)"
    echo "  -u, --unit        Grammar unit (present-tense, past-tense, or all)"
    echo "                    Default: all (generates PDFs for all available units)"
    echo "  -h, --help        Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                          # Generate all available cuadernillos for all units in both languages"
    echo "  $0 1                        # Generate cuadernillo 1 for all available units in both languages"
    echo "  $0 2 -l japanese            # Generate cuadernillo 2 for all available units with Japanese instructions only"
    echo "  $0 1 -u past-tense          # Generate cuadernillo 1 past-tense for both languages"
    echo "  $0 1 -l english -u past-tense # Generate cuadernillo 1 past-tense with English instructions only"
    echo ""
    echo "Output files:"
    echo "  Japanese: cuadernillo-1-ja.pdf, cuadernillo-2-ja.pdf, cuadernillo-3-ja.pdf, cuadernillo-4-ja.pdf"
    echo "  English:  cuadernillo-1-en.pdf, cuadernillo-2-en.pdf, cuadernillo-3-en.pdf, cuadernillo-4-en.pdf"
    exit 0
fi

# Set default language if not specified
if [[ -z "$LANGUAGE" ]]; then
    LANGUAGE="both"
fi

# Set default unit if not specified
if [[ -z "$UNIT" ]]; then
    UNIT="all"
fi

# Validate language option
if [[ "$LANGUAGE" != "japanese" && "$LANGUAGE" != "english" && "$LANGUAGE" != "both" ]]; then
    echo "Error: Language must be 'japanese', 'english', or 'both'"
    echo "Use -h or --help for usage information"
    exit 1
fi

# Validate unit option
if [[ "$UNIT" != "present-tense" && "$UNIT" != "past-tense" && "$UNIT" != "all" ]]; then
    echo "Error: Unit must be 'present-tense', 'past-tense', or 'all'"
    echo "Use -h or --help for usage information"
    exit 1
fi

# Check if virtual environment exists (look in project root)
if [ ! -d "../../venv" ]; then
    echo "Virtual environment not found. Running setup..."
    cd "$(dirname "$0")"  # Ensure we're in the scripts directory
    ./setup.sh
fi

# Activate virtual environment from project root
source ../../venv/bin/activate

echo "🚀 Starting PDF generation..."
echo "Language(s): $LANGUAGE"
echo "Unit(s): $UNIT"

if [[ -n "$CUADERNILLO" ]]; then
    echo "Cuadernillo: $CUADERNILLO"
else
    echo "Cuadernillos: All (1, 2, 3, 4)"
fi

echo ""

# Generate function for a specific unit and language
generate_for_unit_and_language() {
    local unit="$1"
    local language="$2"
    
    echo "📚 Generating $language $unit versions..."
    if [[ -n "$CUADERNILLO" ]]; then
        python generate_pdf.py "$CUADERNILLO" "$language" "$unit"
    else
        python generate_pdf.py "$language" "$unit"
    fi
    echo ""
}

# Generate PDFs based on unit and language selection
if [[ "$UNIT" == "all" ]]; then
    # Generate all available units
    if [[ "$LANGUAGE" == "japanese" || "$LANGUAGE" == "both" ]]; then
        if [[ -n "$CUADERNILLO" ]]; then
            python generate_pdf.py "$CUADERNILLO" japanese all
        else
            python generate_pdf.py japanese all
        fi
        echo ""
    fi
    
    if [[ "$LANGUAGE" == "english" || "$LANGUAGE" == "both" ]]; then
        if [[ -n "$CUADERNILLO" ]]; then
            python generate_pdf.py "$CUADERNILLO" english all
        else
            python generate_pdf.py english all
        fi
        echo ""
    fi
else
    # Generate specific unit(s)
    if [[ "$UNIT" == "present-tense" ]]; then
        if [[ "$LANGUAGE" == "japanese" || "$LANGUAGE" == "both" ]]; then
            generate_for_unit_and_language "present-tense" "japanese"
        fi
        
        if [[ "$LANGUAGE" == "english" || "$LANGUAGE" == "both" ]]; then
            generate_for_unit_and_language "present-tense" "english"
        fi
    fi

    if [[ "$UNIT" == "past-tense" ]]; then
        if [[ "$LANGUAGE" == "japanese" || "$LANGUAGE" == "both" ]]; then
            generate_for_unit_and_language "past-tense" "japanese"
        fi
        
        if [[ "$LANGUAGE" == "english" || "$LANGUAGE" == "both" ]]; then
            generate_for_unit_and_language "past-tense" "english"
        fi
    fi
fi

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