#!/bin/bash
# Wrapper script to generate PDFs with automatic virtual environment handling
# Supports multilingual generation (Japanese and English versions)

set -e

# Parse command line arguments
UNIT=""
LANGUAGE=""
HELP=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -l|--language)
            LANGUAGE="$2"
            shift 2
            ;;
        -h|--help)
            HELP=true
            shift
            ;;
        [1-3])
            UNIT="$1"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

if [[ "$HELP" == true ]]; then
    echo "Usage: $0 [UNIT] [OPTIONS]"
    echo ""
    echo "Generate PDF files from Spanish exercise markdown files."
    echo ""
    echo "Arguments:"
    echo "  CUADERNILLO       Cuadernillo number (1, 2, or 3). If not specified, generates all cuadernillos."
    echo ""
    echo "Options:"
    echo "  -l, --language    Language for instructions (japanese, english, or both)"
    echo "                    Default: both (generates PDFs for both languages)"
    echo "  -h, --help        Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                       # Generate all cuadernillos for both languages"
    echo "  $0 1                     # Generate cuadernillo 1 for both languages"
    echo "  $0 2 -l japanese         # Generate cuadernillo 2 with Japanese instructions only"
    echo "  $0 3 -l english          # Generate cuadernillo 3 with English instructions only"
    echo "  $0 -l both               # Generate all cuadernillos for both languages"
    echo ""
    echo "Output files:"
    echo "  Japanese: cuadernillo-1-ja.pdf, cuadernillo-2-ja.pdf, cuadernillo-3-ja.pdf"
    echo "  English:  cuadernillo-1-en.pdf, cuadernillo-2-en.pdf, cuadernillo-3-en.pdf"
    exit 0
fi

# Set default language if not specified
if [[ -z "$LANGUAGE" ]]; then
    LANGUAGE="both"
fi

# Validate language option
if [[ "$LANGUAGE" != "japanese" && "$LANGUAGE" != "english" && "$LANGUAGE" != "both" ]]; then
    echo "Error: Language must be 'japanese', 'english', or 'both'"
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

if [[ -n "$UNIT" ]]; then
    echo "Cuadernillo: $UNIT"
else
    echo "Cuadernillos: All (1, 2, 3)"
fi

echo ""

# Generate PDFs based on language selection
if [[ "$LANGUAGE" == "japanese" || "$LANGUAGE" == "both" ]]; then
    echo "📚 Generating Japanese versions..."
    if [[ -n "$UNIT" ]]; then
        python generate_pdf.py "$UNIT" japanese
    else
        python generate_pdf.py japanese
    fi
    echo ""
fi

if [[ "$LANGUAGE" == "english" || "$LANGUAGE" == "both" ]]; then
    echo "📚 Generating English versions..."
    if [[ -n "$UNIT" ]]; then
        python generate_pdf.py "$UNIT" english
    else
        python generate_pdf.py english
    fi
    echo ""
fi

# Deactivate virtual environment
deactivate

echo "✅ Done! PDFs are ready for printing in DIN A5 format."