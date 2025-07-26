# PDF Generation for Spanish Exercise Cuadernillos

The PDF generation tools are located in `ejercicios-src/scripts/` and convert the markdown exercise files into PDF format optimized for DIN A5 printing.

## Quick Start

### Option 1: Automated Setup and Generation (using root wrapper)
```bash
# Generate all cuadernillos for both languages (runs setup automatically)
./generate_pdfs.sh

# Generate specific cuadernillo for both languages
./generate_pdfs.sh 1    # Cuadernillo 1 only
./generate_pdfs.sh 2    # Cuadernillo 2 only
./generate_pdfs.sh 3    # Cuadernillo 3 only

# Generate for specific language
./generate_pdfs.sh -l japanese    # All cuadernillos in Japanese
./generate_pdfs.sh -l english     # All cuadernillos in English
./generate_pdfs.sh 1 -l english   # Cuadernillo 1 in English only
```

### Option 2: Direct Script Usage
```bash
# Navigate to scripts directory
cd ejercicios-src/scripts

# Run setup once (uses Python 3.12 by default)
./setup.sh

# Or specify a different Python version
PYTHON_VERSION=python3.11 ./setup.sh

# Then generate PDFs
source ../../venv/bin/activate
python generate_pdf.py        # All cuadernillos in Japanese (default)
python generate_pdf.py english # All cuadernillos in English
python generate_pdf.py 1      # Cuadernillo 1 in Japanese only
python generate_pdf.py 1 english # Cuadernillo 1 in English only
deactivate
```

### Option 3: Use specific Python version directly
```bash
# Navigate to scripts directory and create venv with specific Python version
cd ejercicios-src/scripts
/opt/homebrew/bin/python3.11 -m venv ../../venv
source ../../venv/bin/activate
pip install -r requirements.txt
python generate_pdf.py
deactivate
```

## Output

The scripts will generate PDFs in organized directories:

### Japanese versions (default):
- `website/public/pdfs/japanese/cuadernillo-1-ja.pdf` - First conjugation (-AR verbs)
- `website/public/pdfs/japanese/cuadernillo-2-ja.pdf` - Second conjugation (-ER verbs)  
- `website/public/pdfs/japanese/cuadernillo-3-ja.pdf` - Third conjugation (-IR verbs)

### English versions:
- `website/public/pdfs/english/cuadernillo-1-en.pdf` - First conjugation (-AR verbs)
- `website/public/pdfs/english/cuadernillo-2-en.pdf` - Second conjugation (-ER verbs)
- `website/public/pdfs/english/cuadernillo-3-en.pdf` - Third conjugation (-IR verbs)

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
   chmod +x ejercicios-src/scripts/setup.sh ejercicios-src/scripts/generate_pdf.py ejercicios-src/scripts/generate_pdfs.sh
   ```

2. **Font issues**: The script uses system fonts. On macOS, it will use Hiragino Sans for Japanese text.

3. **PDF generation errors**: Check that all markdown files exist in the exercise directories:
   ```bash
   ls -la ejercicios-src/markdown/cuadernillo-1-ar-verbs/japanese/
   ls -la ejercicios-src/markdown/cuadernillo-1-ar-verbs/english/
   ```

## Customization

To modify the PDF appearance, edit the CSS styles in `ejercicios-src/scripts/generate_pdf.py`:
- Page margins: Adjust `@page` margin values
- Font sizes: Modify `font-size` values
- Colors: Change color values for headers and text
- Page breaks: Adjust `page-break-before` rules