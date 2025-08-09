# PDF Generation for Spanish Exercise Cuadernillos

The PDF generation tools are located in `ejercicios-src/scripts/` and convert the markdown exercise files into PDF format optimized for DIN A5 printing.

## Quick Start

### Option 1: Simple Generation (Recommended)
```bash
# Generate all cuadernillos for all units in both languages
# Also updates website preview data
./generate_pdfs.sh
```

This single command will:
- Generate all cuadernillos (1-4) 
- Generate all units (present-tense, past-tense)
- Generate both languages (Japanese and English)
- Update website preview data
- Verify all PDFs have exactly 6 pages

### Option 2: Advanced Usage (For Development)
If you need to generate specific combinations for testing:

```bash
# Navigate to scripts directory
cd ejercicios-src/scripts

# Run setup once (uses Python 3.12 by default)
./setup.sh

# Generate specific combinations
source ../../venv/bin/activate
python generate_pdf.py japanese all           # All Japanese cuadernillos
python generate_pdf.py english all            # All English cuadernillos  
python generate_pdf.py japanese present-tense # Japanese present tense only
python generate_pdf.py english past-tense     # English past tense only
deactivate
```

## Output

The scripts will generate PDFs in organized directories:

### Japanese versions:
- `website/public/pdfs/japanese/cuadernillo-1-present-tense-ja.pdf` - First conjugation (-AR verbs), present tense
- `website/public/pdfs/japanese/cuadernillo-1-past-tense-ja.pdf` - First conjugation (-AR verbs), past tense
- `website/public/pdfs/japanese/cuadernillo-2-present-tense-ja.pdf` - Second conjugation (-ER verbs), present tense
- `website/public/pdfs/japanese/cuadernillo-2-past-tense-ja.pdf` - Second conjugation (-ER verbs), past tense
- `website/public/pdfs/japanese/cuadernillo-3-present-tense-ja.pdf` - Third conjugation (-IR verbs), present tense
- `website/public/pdfs/japanese/cuadernillo-3-past-tense-ja.pdf` - Third conjugation (-IR verbs), past tense
- `website/public/pdfs/japanese/cuadernillo-4-present-tense-ja.pdf` - Mixed verbs, present tense
- `website/public/pdfs/japanese/cuadernillo-4-past-tense-ja.pdf` - Mixed verbs, past tense

### English versions:
- `website/public/pdfs/english/cuadernillo-1-present-tense-en.pdf` - First conjugation (-AR verbs), present tense
- `website/public/pdfs/english/cuadernillo-1-past-tense-en.pdf` - First conjugation (-AR verbs), past tense
- `website/public/pdfs/english/cuadernillo-2-present-tense-en.pdf` - Second conjugation (-ER verbs), present tense
- `website/public/pdfs/english/cuadernillo-2-past-tense-en.pdf` - Second conjugation (-ER verbs), past tense
- `website/public/pdfs/english/cuadernillo-3-present-tense-en.pdf` - Third conjugation (-IR verbs), present tense
- `website/public/pdfs/english/cuadernillo-3-past-tense-en.pdf` - Third conjugation (-IR verbs), past tense
- `website/public/pdfs/english/cuadernillo-4-present-tense-en.pdf` - Mixed verbs, present tense
- `website/public/pdfs/english/cuadernillo-4-past-tense-en.pdf` - Mixed verbs, past tense

### Website Preview Data:
The script also updates `website/app/data/markdown/` with all exercise content for the web preview system.

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