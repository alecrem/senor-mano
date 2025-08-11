# PDF Generation for Spanish Exercise Cuadernillos

The PDF generation tools are located in `ejercicios-src/scripts/` and convert the markdown exercise files into PDF format optimized for DIN A5 printing.

## Quick Start

```bash
./generate_pdfs.sh
```

This command will:
- Generate all cuadernillos and units
- Update website preview data
- Verify all PDFs have exactly 6 pages

## Output

PDFs are generated in organized directories:

- `website/public/pdfs/japanese/` - Japanese instruction versions  
- `website/public/pdfs/english/` - English instruction versions
- `website/app/data/markdown/` - Exercise content for web preview system

Files follow the naming pattern: `cuadernillo-[number]-[tense]-[language].pdf`

## Features

- **DIN A5 Format**: Optimized for A5 paper size
- **Large Text**: 14pt base font size, suitable for children
- **Font Support**: Uses Lato, Delius, and Hiragino Maru Gothic ProN fonts
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

1. **Font issues**: The script requires specific fonts to be installed on your system:
   - **Lato** - Main body font ([Download from Adobe Fonts](https://fonts.adobe.com/fonts/lato) or [Font Squirrel](https://www.fontsquirrel.com/fonts/lato))
   - **Delius** - Header font ([Download from Font Library](https://fontlibrary.org/en/font/delius) or [1001 Fonts](https://www.1001fonts.com/delius-font.html))
   - **Hiragino Maru Gothic ProN** - For Japanese text support

2. **PDF generation errors**: Check that all markdown files exist in the exercise directories:
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