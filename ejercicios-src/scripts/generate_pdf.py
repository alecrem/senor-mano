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


def create_css_style(cuadernillo_title=""):
    """Create CSS styling for DIN A5 format with compact layout."""
    css_template = """
    @page {
        size: A5;
        margin: 10mm 8mm 15mm 8mm;
        @bottom-left {
            content: "CUADERNILLO_TITLE_PLACEHOLDER";
            font-size: 9pt;
            color: #666666;
        }
        @bottom-right {
            content: counter(page);
            font-size: 9pt;
            color: #666666;
        }
    }
    
    body {
        font-family: "Lato", "Hiragino Maru Gothic ProN", sans-serif;
        font-size: 11pt;
        line-height: 1.3;
        color: #1a1a1a;
        margin: 0;
        padding: 0;
    }
    
    h1 {
        font-family: "Delius", "Hiragino Maru Gothic ProN", sans-serif;
        font-size: 14pt;
        font-weight: 400;
        margin: 0 0 6mm 0;
        text-align: center;
        color: #1a1a1a;
    }
    
    h2 {
        font-size: 12pt;
        font-weight: bold;
        margin: 4mm 0 2mm 0;
        color: #1a1a1a;
    }
    
    h3 {
        font-size: 11pt;
        font-weight: bold;
        margin: 3mm 0 1mm 0;
        color: #1a1a1a;
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
        background-color: #f5f5f5;
        font-weight: bold;
    }
    
    strong {
        font-weight: bold;
    }
    
    /* Ensure dialogue formatting */
    p strong {
        color: #1a1a1a;
        font-weight: 700;
    }
    
    /* Exercise lines */
    hr {
        border: none;
        border-top: 1px solid #cccccc;
        margin: 4mm 0;
    }
    
    /* Blank lines for answers */
    ._blank_line {
        border-bottom: 1px solid #1a1a1a;
        display: inline-block;
        width: 50mm;
        margin: 0 1mm;
    }
    
    /* Longer blank lines for verb exercises (pages 2, 4) */
    ._long_blank_line {
        border-bottom: 1px solid #1a1a1a;
        display: inline-block;
        width: 25mm;
        margin: 0 1mm;
    }
    
    /* Full-width correction lines (page 6) */
    ._correction_line {
        border-bottom: 1px solid #1a1a1a;
        display: inline-block;
        width: 80mm;
        margin: 0 1mm;
        min-height: 3mm;
    }
    
    /* Very short lines for B/M answers (page 6) */
    ._short_line {
        border-bottom: 1px solid #1a1a1a;
        display: inline-block;
        width: 8mm;
        margin: 0 1mm;
    }
    
    /* New HTML placeholder styles for answer lines */
    .answer-line-short {
        border-bottom: 1px solid #1a1a1a;
        display: inline-block;
        width: 25mm;
        margin: 0 1mm;
        min-height: 3mm;
    }
    
    .answer-line-long {
        border-bottom: 1px solid #1a1a1a;
        display: inline-block;
        width: 80mm;
        margin: 0 1mm;
        min-height: 3mm;
    }
    
    /* B/M answer space for page 6 */
    .b-m-space {
        border-bottom: 1px solid #1a1a1a;
        display: inline-block;
        width: 8mm;
        margin: 0 2mm;
        min-height: 3mm;
    }
    
    /* Writing space for page 5 with more vertical room */
    .writing-space {
        border-bottom: 1px solid #1a1a1a;
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

    # Replace the placeholder with the actual cuadernillo title
    css_content = css_template.replace(
        "CUADERNILLO_TITLE_PLACEHOLDER", cuadernillo_title
    )
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
    markdown_content = markdown_content.replace(
        "[ONE_LETTER_LINE]", "{{ONE_LETTER_LINE_PLACEHOLDER}}"
    )
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


def get_available_cuadernillos(unit="present-tense", language="japanese"):
    """Get list of available cuadernillos for a given unit and language."""
    available = []
    verb_types = {1: "ar", 2: "er", 3: "ir", 4: "mixed"}

    for cuadernillo_num, verb_type in verb_types.items():
        # Check if cuadernillo directory exists for this unit
        cuadernillo_dir = Path(
            f"../markdown/{unit}/cuadernillo-{cuadernillo_num}-{verb_type}-verbs/{language}"
        )

        # Fallback to legacy multilingual structure
        if not cuadernillo_dir.exists():
            cuadernillo_dir = Path(
                f"../markdown/cuadernillo-{cuadernillo_num}-{verb_type}-verbs/{language}"
            )

            # Fallback to legacy structure
            if not cuadernillo_dir.exists():
                cuadernillo_dir = Path(f"../markdown/cuadernillo-{cuadernillo_num}")

        # Check if any required page files exist
        if cuadernillo_dir.exists():
            page_files = ["pagina-1-dialogo.md", "pagina-2-conjugacion-completar.md"]
            if any((cuadernillo_dir / page_file).exists() for page_file in page_files):
                available.append(cuadernillo_num)

    return available


def generate_cuadernillo_pdf(
    cuadernillo_number, language="japanese", unit="present-tense"
):
    """Generate PDF for a specific cuadernillo and language."""
    # Map cuadernillo numbers to verb types
    verb_types = {1: "ar", 2: "er", 3: "ir", 4: "mixed"}
    verb_type = verb_types.get(cuadernillo_number)

    # Try new units structure first
    cuadernillo_dir = Path(
        f"../markdown/{unit}/cuadernillo-{cuadernillo_number}-{verb_type}-verbs/{language}"
    )

    # Fallback to legacy multilingual structure for backward compatibility
    if not cuadernillo_dir.exists():
        print(
            f"Warning: Units structure {cuadernillo_dir} not found, trying legacy multilingual structure"
        )
        cuadernillo_dir = Path(
            f"../markdown/cuadernillo-{cuadernillo_number}-{verb_type}-verbs/{language}"
        )

        # Fallback to legacy structure for backward compatibility
        if not cuadernillo_dir.exists():
            print(
                f"Warning: New structure {cuadernillo_dir} not found, falling back to legacy structure"
            )
            cuadernillo_dir = Path(f"../markdown/cuadernillo-{cuadernillo_number}")
            if not cuadernillo_dir.exists():
                print(
                    f"Error: None of the cuadernillo directory structures exist for cuadernillo {cuadernillo_number}"
                )
                return False

    # Collect all markdown files for the cuadernillo
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

        page_file = cuadernillo_dir / page_files[i]
        if page_file.exists():
            with open(page_file, "r", encoding="utf-8") as f:
                content = f.read()
                pages.append(content)
        else:
            print(f"Warning: {page_file} not found")

    if not pages:
        print(
            f"Error: No pages found for cuadernillo {cuadernillo_number} in {language}"
        )
        return False

    # Read cuadernillo metadata for title insertion (try both locations)
    metadata_file = cuadernillo_dir / "cuadernillo.yaml"
    legacy_metadata = (
        Path(f"../markdown/cuadernillo-{cuadernillo_number}") / "cuadernillo.yaml"
    )

    cuadernillo_title_for_page = f"Cuadernillo {cuadernillo_number}"  # Default fallback

    # Try new structure first, then legacy
    for meta_path in [metadata_file, legacy_metadata]:
        if meta_path.exists():
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    metadata = yaml.safe_load(f)
                    cuadernillo_title_for_page = metadata.get(
                        "title", cuadernillo_title_for_page
                    )
                    break
            except Exception as e:
                print(f"Warning: Could not read metadata from {meta_path}: {e}")

    # No need for language indicator in title - families use only one language

    # Combine all pages with page breaks
    combined_content = ""
    for i, page_content in enumerate(pages):
        if i > 0:
            combined_content += "\n\n<div style='page-break-before: always;'></div>\n\n"

        # Add cuadernillo title as H1 with logo before the first page content
        if i == 0:
            logo_path = os.path.abspath("../assets/senormano-logo-bw-small.png")
            combined_content += f'<div style="display: flex; align-items: center; margin-bottom: 6mm;"><img src="file://{logo_path}" alt="Logo" style="height: 2.4em; margin-right: 2mm;"><h1 style="margin: 0; text-align: left; font-size: 14pt;">{cuadernillo_title_for_page}</h1></div>\n\n'

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
        <title>Cuadernillo de Español - Cuadernillo {cuadernillo_number}</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Generate PDF with language-specific filename (output to website directory only)
    lang_code = {"japanese": "ja", "english": "en"}
    file_suffix = f"-{lang_code.get(language, 'ja')}"

    # Always include unit in filename for consistency
    unit_suffix = f"-{unit}"

    # Output to website public directory for web serving
    output_dir = Path(f"../../website/public/pdfs/{language}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = (
        output_dir / f"cuadernillo-{cuadernillo_number}{unit_suffix}{file_suffix}.pdf"
    )

    # Use the same cuadernillo title we read earlier for the footer
    cuadernillo_title = cuadernillo_title_for_page

    try:
        font_config = FontConfiguration()
        html_doc = HTML(string=full_html)
        css_style = create_css_style(cuadernillo_title)

        # Generate PDF to website public directory
        html_doc.write_pdf(
            output_file, stylesheets=[css_style], font_config=font_config
        )

        print(f"✅ Generated {output_file}")
        return True

    except Exception as e:
        print(
            f"❌ Error generating PDF for cuadernillo {cuadernillo_number} ({language}): {e}"
        )
        return False


def main():
    """Main function to generate PDFs."""
    # Parse arguments
    args = sys.argv[1:]
    cuadernillo_number = None
    language = "japanese"  # Default language
    unit = "all"  # Default to all units

    # Parse command line arguments
    i = 0
    while i < len(args):
        arg = args[i]

        if arg in ["japanese", "english"]:
            language = arg
        elif arg in ["present-tense", "past-tense", "all"]:
            unit = arg
        elif arg.isdigit() and int(arg) in [1, 2, 3, 4]:
            cuadernillo_number = int(arg)
        else:
            print(f"Error: Unknown argument '{arg}'")
            print("Usage: python generate_pdf.py [CUADERNILLO] [LANGUAGE] [UNIT]")
            print("  CUADERNILLO: 1, 2, 3, or 4 (optional)")
            print("  LANGUAGE: japanese or english (default: japanese)")
            print("  UNIT: present-tense, past-tense, or all (default: all)")
            print("Examples:")
            print(
                "  python generate_pdf.py                    # Generate all available cuadernillos for all units in Japanese"
            )
            print(
                "  python generate_pdf.py english            # Generate all available cuadernillos for all units in English"
            )
            print(
                "  python generate_pdf.py 1 japanese         # Generate cuadernillo 1 for all units in Japanese"
            )
            print(
                "  python generate_pdf.py 1 english past-tense # Generate cuadernillo 1 past-tense in English"
            )
            sys.exit(1)
        i += 1

    if cuadernillo_number is not None:
        # Generate specific cuadernillo
        if unit == "all":
            # Generate for all available units
            units_to_generate = ["present-tense", "past-tense"]
            total_success = 0
            total_attempted = 0

            for unit_name in units_to_generate:
                available = get_available_cuadernillos(unit_name, language)
                if cuadernillo_number in available:
                    print(
                        f"Generating cuadernillo {cuadernillo_number} ({unit_name}) in {language}..."
                    )
                    total_attempted += 1
                    if generate_cuadernillo_pdf(
                        cuadernillo_number, language, unit_name
                    ):
                        total_success += 1

            if total_attempted == 0:
                print(
                    f"❌ Cuadernillo {cuadernillo_number} not found in any unit for {language}"
                )
                sys.exit(1)
            elif total_success == total_attempted:
                print(
                    f"\n🎉 Successfully generated cuadernillo {cuadernillo_number} PDFs for all available units in {language}"
                )
            else:
                print(
                    f"\n⚠️  Generated {total_success}/{total_attempted} cuadernillo {cuadernillo_number} PDFs in {language}"
                )
        else:
            # Generate for specific unit
            print(
                f"Generating cuadernillo {cuadernillo_number} ({unit}) in {language}..."
            )
            success = generate_cuadernillo_pdf(cuadernillo_number, language, unit)
            if success:
                print(
                    f"\n🎉 Successfully generated cuadernillo {cuadernillo_number} ({unit}) PDF in {language}"
                )
            else:
                print(
                    f"\n❌ Failed to generate cuadernillo {cuadernillo_number} ({unit}) PDF in {language}"
                )
                sys.exit(1)
    else:
        # Generate all available cuadernillos
        if unit == "all":
            units_to_generate = ["present-tense", "past-tense"]
        else:
            units_to_generate = [unit]

        total_success = 0
        total_attempted = 0

        for unit_name in units_to_generate:
            available = get_available_cuadernillos(unit_name, language)
            if available:
                print(
                    f"Generating {unit_name} cuadernillos {available} in {language}..."
                )
                for cuadernillo_num in available:
                    total_attempted += 1
                    if generate_cuadernillo_pdf(cuadernillo_num, language, unit_name):
                        total_success += 1
            else:
                print(f"No {unit_name} cuadernillos found for {language}")

        if total_attempted == 0:
            print(f"❌ No cuadernillos found for {language}")
            sys.exit(1)
        else:
            print(
                f"\n🎉 Successfully generated {total_success}/{total_attempted} cuadernillo PDFs in {language}"
            )
            if total_success == total_attempted:
                print(
                    f"\nAll available {language} PDFs are ready for printing in DIN A5 format!"
                )
            else:
                print(
                    f"\nSome {language} PDFs failed to generate. Check the error messages above."
                )


if __name__ == "__main__":
    main()
