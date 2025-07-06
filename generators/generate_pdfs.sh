#!/bin/bash
# Wrapper script to generate PDFs with automatic virtual environment handling

set -e

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup..."
    ./setup.sh
fi

# Activate virtual environment
source venv/bin/activate

# Run the PDF generation script
python generate_pdf.py "$@"

# Deactivate virtual environment
deactivate

echo "Done!"