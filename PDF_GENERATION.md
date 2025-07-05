# PDF Generation for Spanish Exercise Units

This directory contains scripts to convert the markdown exercise files into PDF format optimized for DIN A5 printing.

## Quick Start

### Option 1: Automated Setup and Generation
```bash
# Generate all units (runs setup automatically)
./generate_pdfs.sh

# Generate specific unit
./generate_pdfs.sh 1    # Unit 1 only
./generate_pdfs.sh 2    # Unit 2 only
./generate_pdfs.sh 3    # Unit 3 only
```

### Option 2: Manual Setup
```bash
# Run setup once (uses Python 3.12 by default)
./setup.sh

# Or specify a different Python version
PYTHON_VERSION=python3.11 ./setup.sh

# Then generate PDFs
source venv/bin/activate
python generate_pdf.py        # All units
python generate_pdf.py 1      # Unit 1 only
python generate_pdf.py 2      # Unit 2 only
python generate_pdf.py 3      # Unit 3 only
deactivate
```

### Option 3: Use specific Python version directly
```bash
# Create venv with specific Python version
/opt/homebrew/bin/python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate_pdf.py
deactivate
```

## Output

The scripts will generate:
- `unidad-1.pdf` - First conjugation (-AR verbs)
- `unidad-2.pdf` - Second conjugation (-ER verbs)
- `unidad-3.pdf` - Third conjugation (-IR verbs)

## Features

- **DIN A5 Format**: Optimized for A5 paper size
- **Large Text**: 14pt base font size, suitable for children
- **Japanese Font Support**: Includes Hiragino Sans and Yu Gothic fonts
- **Proper Page Breaks**: Each exercise page starts on a new page
- **Table Formatting**: Clean tables for verb conjugations
- **Answer Lines**: Underscores converted to proper blank lines

## Requirements

- Python 3.6+
- Virtual environment (automatically created)
- Required packages (automatically installed):
  - `weasyprint` - PDF generation
  - `markdown` - Markdown parsing

## Troubleshooting

If you encounter issues:

1. **Permission errors**: Make sure scripts are executable
   ```bash
   chmod +x setup.sh generate_pdf.py generate_pdfs.sh
   ```

2. **Font issues**: The script uses system fonts. On macOS, it will use Hiragino Sans for Japanese text.

3. **PDF generation errors**: Check that all markdown files exist in the unit directories.

## Customization

To modify the PDF appearance, edit the CSS styles in `generate_pdf.py`:
- Page margins: Adjust `@page` margin values
- Font sizes: Modify `font-size` values
- Colors: Change color values for headers and text
- Page breaks: Adjust `page-break-before` rules