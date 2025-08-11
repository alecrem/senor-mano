"""
PDF building logic for Spanish exercise cuadernillos.

Handles the core PDF generation functionality including file reading,
content assembly, and PDF output.
"""

import os
from pathlib import Path
import yaml
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

from .css_styles import create_css_style
from .markdown_processor import markdown_to_html


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
    metadata_file = cuadernillo_dir.parent / "cuadernillo.yaml"  # Go up one level from language dir
    legacy_metadata = (
        Path(f"../markdown/cuadernillo-{cuadernillo_number}") / "cuadernillo.yaml"
    )

    cuadernillo_title_for_page = f"Cuadernillo {cuadernillo_number}"  # Default fallback
    unit_title_for_footer = ""  # Default fallback

    # Try new structure first, then legacy
    for meta_path in [metadata_file, legacy_metadata]:
        if meta_path.exists():
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    metadata = yaml.safe_load(f)
                    cuadernillo_title_for_page = metadata.get(
                        "title", cuadernillo_title_for_page
                    )
                    unit_title_for_footer = metadata.get("unit_title", "")
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

    try:
        font_config = FontConfiguration()
        html_doc = HTML(string=full_html)
        css_style = create_css_style(unit_title_for_footer)

        # Generate PDF to website public directory
        html_doc.write_pdf(
            output_file, stylesheets=[css_style], font_config=font_config
        )

        print(f"• Generated {output_file}")
        return True

    except Exception as e:
        print(
            f"❌ Error generating PDF for cuadernillo {cuadernillo_number} ({language}): {e}"
        )
        return False