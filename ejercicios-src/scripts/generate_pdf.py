#!/usr/bin/env python3
"""
Generate PDF files from Spanish exercise markdown files.
Optimized for DIN A5 format with large text for children.

Copyright (c) 2025 alecrem
Licensed under the MIT License. See LICENSE file for details.
"""

import os
import sys
from pathlib import Path
import markdown
import yaml
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


def create_css_style(unit_title=""):
    """Create CSS styling for DIN A5 format with compact layout."""
    css_template = """
    @page {
        size: A5;
        margin: 10mm 8mm 15mm 8mm;
        @bottom-left {
            content: "UNIT_TITLE_PLACEHOLDER";
            font-size: 9pt;
            color: #666;
        }
        @bottom-right {
            content: counter(page);
            font-size: 9pt;
            color: #666;
        }
    }
    
    body {
        font-family: "Hiragino Sans", "Yu Gothic", "Meiryo", sans-serif;
        font-size: 11pt;
        line-height: 1.3;
        color: #333;
        margin: 0;
        padding: 0;
    }
    
    h1 {
        font-size: 14pt;
        font-weight: bold;
        margin: 0 0 6mm 0;
        text-align: center;
        color: #2c3e50;
    }
    
    h2 {
        font-size: 12pt;
        font-weight: bold;
        margin: 4mm 0 2mm 0;
        color: #34495e;
    }
    
    h3 {
        font-size: 11pt;
        font-weight: bold;
        margin: 3mm 0 1mm 0;
        color: #34495e;
    }
    
    p {
        margin-bottom: 1.5mm;
        text-align: left;
    }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 2mm 0;
        font-size: 9pt;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 2mm;
        text-align: center;
    }
    
    th {
        background-color: #f8f9fa;
        font-weight: bold;
    }
    
    strong {
        font-weight: bold;
    }
    
    /* Ensure dialogue formatting */
    p strong {
        color: #2980b9;
    }
    
    /* Exercise lines */
    hr {
        border: none;
        border-top: 1px solid #bdc3c7;
        margin: 4mm 0;
    }
    
    /* Blank lines for answers */
    ._blank_line {
        border-bottom: 1px solid #333;
        display: inline-block;
        width: 50mm;
        margin: 0 1mm;
    }
    
    /* Longer blank lines for verb exercises (pages 2, 4) */
    ._long_blank_line {
        border-bottom: 1px solid #333;
        display: inline-block;
        width: 25mm;
        margin: 0 1mm;
    }
    
    /* Full-width correction lines (page 6) */
    ._correction_line {
        border-bottom: 1px solid #333;
        display: inline-block;
        width: 80mm;
        margin: 0 1mm;
        min-height: 3mm;
    }
    
    /* Very short lines for B/M answers (page 6) */
    ._short_line {
        border-bottom: 1px solid #333;
        display: inline-block;
        width: 8mm;
        margin: 0 1mm;
    }
    
    /* New HTML placeholder styles for answer lines */
    .answer-line-short {
        border-bottom: 1px solid #333;
        display: inline-block;
        width: 25mm;
        margin: 0 1mm;
        min-height: 3mm;
    }
    
    .answer-line-long {
        border-bottom: 1px solid #333;
        display: inline-block;
        width: 80mm;
        margin: 0 1mm;
        min-height: 3mm;
    }
    
    /* B/M answer space for page 6 */
    .b-m-space {
        border-bottom: 1px solid #333;
        display: inline-block;
        width: 8mm;
        margin: 0 2mm;
        min-height: 3mm;
    }
    
    /* Writing space for page 5 with more vertical room */
    .writing-space {
        border-bottom: 1px solid #333;
        display: block;
        width: 100%;
        margin: 4mm 0;
        min-height: 4mm;
    }
    
    /* Page breaks between exercises */
    .page-break {
        page-break-before: always;
    }
    
    /* Compact list spacing */
    ol, ul {
        margin: 2mm 0;
        padding-left: 5mm;
    }
    
    li {
        margin-bottom: 1mm;
    }
    
    /* Compact paragraph spacing for exercises */
    .exercise p {
        margin-bottom: 1mm;
    }
    """

    # Replace the placeholder with the actual unit title
    css_content = css_template.replace("UNIT_TITLE_PLACEHOLDER", unit_title)
    return CSS(string=css_content)


def markdown_to_html(markdown_content):
    """Convert markdown content to HTML."""
    # Replace human-readable placeholders with HTML spans
    # These are the new placeholders that are easy to read and type

    # Replace text placeholders with temporary tokens
    markdown_content = markdown_content.replace(
        "[SHORT_LINE]", "{{SHORT_LINE_PLACEHOLDER}}"
    )
    markdown_content = markdown_content.replace(
        "[LONG_LINE]", "{{LONG_LINE_PLACEHOLDER}}"
    )
    markdown_content = markdown_content.replace("[ONE_LETTER_LINE]", "{{ONE_LETTER_LINE_PLACEHOLDER}}")
    markdown_content = markdown_content.replace(
        "[LONG_TALL_LINE]", "{{LONG_TALL_LINE_PLACEHOLDER}}"
    )

    # Also handle legacy underscore patterns for backwards compatibility
    # IMPORTANT: Process longer patterns first to avoid partial matches

    # Long correction lines (page 6) - use 30+ underscores (FIRST!)
    markdown_content = markdown_content.replace("_" * 33, "{{CORRECTION_LINE}}")
    markdown_content = markdown_content.replace("_" * 30, "{{CORRECTION_LINE}}")

    # Medium answer lines (pages 2, 4) - use 13-20 underscores
    markdown_content = markdown_content.replace("_" * 20, "{{LONG_BLANK_LINE}}")
    markdown_content = markdown_content.replace("_" * 15, "{{LONG_BLANK_LINE}}")
    markdown_content = markdown_content.replace("_" * 13, "{{LONG_BLANK_LINE}}")

    # Short answer lines (page 3) - use 10 underscores
    markdown_content = markdown_content.replace("_" * 10, "{{BLANK_LINE}}")

    # Very short lines for B/M (page 6) - use 3 underscores (LAST!)
    markdown_content = markdown_content.replace("_" * 3, "{{SHORT_LINE}}")

    # Configure markdown with extensions
    md = markdown.Markdown(extensions=["tables", "nl2br"])

    # Process the markdown content
    html_content = md.convert(markdown_content)

    # Now replace the placeholders with actual HTML
    html_content = html_content.replace(
        "{{SHORT_LINE_PLACEHOLDER}}", '<span class="answer-line-short"></span>'
    )
    html_content = html_content.replace(
        "{{LONG_LINE_PLACEHOLDER}}", '<span class="answer-line-long"></span>'
    )
    html_content = html_content.replace(
        "{{ONE_LETTER_LINE_PLACEHOLDER}}", '<span class="b-m-space"></span>'
    )
    html_content = html_content.replace(
        "{{LONG_TALL_LINE_PLACEHOLDER}}", '<div class="writing-space"></div>'
    )

    # Legacy underscore replacements
    html_content = html_content.replace(
        "{{CORRECTION_LINE}}", '<span class="_correction_line"></span>'
    )
    html_content = html_content.replace(
        "{{LONG_BLANK_LINE}}", '<span class="_long_blank_line"></span>'
    )
    html_content = html_content.replace(
        "{{BLANK_LINE}}", '<span class="_blank_line"></span>'
    )
    html_content = html_content.replace(
        "{{SHORT_LINE}}", '<span class="_short_line"></span>'
    )

    return html_content


def generate_unit_pdf(unit_number, language="japanese"):
    """Generate PDF for a specific unit and language."""
    # Map unit numbers to verb types
    verb_types = {1: "ar", 2: "er", 3: "ir"}
    verb_type = verb_types.get(unit_number)

    # Try new multilingual structure first (adjust for new directory structure)
    unit_dir = Path(f"../markdown/cuadernillo-{unit_number}-{verb_type}-verbs/{language}")

    # Fallback to legacy structure for backward compatibility
    if not unit_dir.exists():
        print(
            f"Warning: New structure {unit_dir} not found, falling back to legacy structure"
        )
        unit_dir = Path(f"../markdown/cuadernillo-{unit_number}")
        if not unit_dir.exists():
            print(
                f"Error: Neither new nor legacy cuadernillo directory exists for cuadernillo {unit_number}"
            )
            return False

    # Collect all markdown files for the unit
    pages = []
    for i in range(1, 7):
        page_files = {
            1: "pagina-1-dialogo.md",
            2: "pagina-2-conjugacion-completar.md",
            3: "pagina-3-eleccion.md",
            4: "pagina-4-transformacion.md",
            5: "pagina-5-ordenar.md",
            6: "pagina-6-bien-mal.md",
        }

        page_file = unit_dir / page_files[i]
        if page_file.exists():
            with open(page_file, "r", encoding="utf-8") as f:
                content = f.read()
                pages.append(content)
        else:
            print(f"Warning: {page_file} not found")

    if not pages:
        print(f"Error: No pages found for cuadernillo {unit_number} in {language}")
        return False

    # Read unit metadata for title insertion (try both locations)
    metadata_file = unit_dir / "unit.yaml"
    legacy_metadata = Path(f"../markdown/cuadernillo-{unit_number}") / "unit.yaml"

    unit_title_for_page = f"Cuadernillo {unit_number}"  # Default fallback

    # Try new structure first, then legacy
    for meta_path in [metadata_file, legacy_metadata]:
        if meta_path.exists():
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    metadata = yaml.safe_load(f)
                    unit_title_for_page = metadata.get("title", unit_title_for_page)
                    break
            except Exception as e:
                print(f"Warning: Could not read metadata from {meta_path}: {e}")

    # No need for language indicator in title - families use only one language

    # Combine all pages with page breaks
    combined_content = ""
    for i, page_content in enumerate(pages):
        if i > 0:
            combined_content += "\n\n<div style='page-break-before: always;'></div>\n\n"

        # Add unit title as H1 before the first page content
        if i == 0:
            combined_content += f"# {unit_title_for_page}\n\n"

        combined_content += page_content

    # Convert to HTML
    html_content = markdown_to_html(combined_content)

    # Wrap in proper HTML structure
    full_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cuadernillo de Español - Cuadernillo {unit_number}</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Generate PDF with language-specific filename (output to website directory only)
    lang_code = {"japanese": "ja", "english": "en"}
    file_suffix = f"-{lang_code.get(language, 'ja')}"
    
    # Output to website public directory for web serving
    output_dir = Path(f"../../website/public/pdfs/{language}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"cuadernillo-{unit_number}{file_suffix}.pdf"

    # Use the same unit title we read earlier for the footer
    unit_title = unit_title_for_page

    try:
        font_config = FontConfiguration()
        html_doc = HTML(string=full_html)
        css_style = create_css_style(unit_title)

        # Generate PDF to website public directory
        html_doc.write_pdf(
            output_file, stylesheets=[css_style], font_config=font_config
        )

        print(f"✅ Generated {output_file}")
        return True

    except Exception as e:
        print(f"❌ Error generating PDF for cuadernillo {unit_number} ({language}): {e}")
        return False


def main():
    """Main function to generate PDFs."""
    # Parse arguments
    args = sys.argv[1:]
    unit_number = None
    language = "japanese"  # Default language

    # Parse command line arguments
    i = 0
    while i < len(args):
        arg = args[i]

        if arg in ["japanese", "english"]:
            language = arg
        elif arg.isdigit() and int(arg) in [1, 2, 3]:
            unit_number = int(arg)
        else:
            print(f"Error: Unknown argument '{arg}'")
            print("Usage: python generate_pdf.py [CUADERNILLO] [LANGUAGE]")
            print("  CUADERNILLO: 1, 2, or 3 (optional)")
            print("  LANGUAGE: japanese or english (default: japanese)")
            print("Examples:")
            print(
                "  python generate_pdf.py              # Generate all cuadernillos in Japanese"
            )
            print(
                "  python generate_pdf.py english      # Generate all cuadernillos in English"
            )
            print("  python generate_pdf.py 1 japanese   # Generate cuadernillo 1 in Japanese")
            print("  python generate_pdf.py 2 english    # Generate cuadernillo 2 in English")
            sys.exit(1)
        i += 1

    if unit_number is not None:
        # Generate specific cuadernillo
        print(f"Generating cuadernillo {unit_number} in {language}...")
        success = generate_unit_pdf(unit_number, language)
        if success:
            print(f"\n🎉 Successfully generated cuadernillo {unit_number} PDF in {language}")
        else:
            print(f"\n❌ Failed to generate cuadernillo {unit_number} PDF in {language}")
            sys.exit(1)
    else:
        # Generate all cuadernillos
        print(f"Generating PDFs for all cuadernillos in {language}...")
        success_count = 0
        for unit_num in [1, 2, 3]:
            if generate_unit_pdf(unit_num, language):
                success_count += 1

        print(f"\n🎉 Successfully generated {success_count}/3 cuadernillo PDFs in {language}")

        if success_count == 3:
            print(f"\nAll {language} PDFs are ready for printing in DIN A5 format!")
        else:
            print(
                f"\nSome {language} PDFs failed to generate. Check the error messages above."
            )
            sys.exit(1)


if __name__ == "__main__":
    main()
