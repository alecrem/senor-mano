#!/usr/bin/env python3
"""
Generate PDF files from Spanish exercise markdown files.
Optimized for DIN A5 format with large text for children.
"""

import os
import sys
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


def create_css_style():
    """Create CSS styling for DIN A5 format with large text."""
    return CSS(string="""
    @page {
        size: A5;
        margin: 20mm;
    }
    
    body {
        font-family: "Hiragino Sans", "Yu Gothic", "Meiryo", sans-serif;
        font-size: 14pt;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 0;
    }
    
    h1 {
        font-size: 18pt;
        font-weight: bold;
        margin-bottom: 15mm;
        text-align: center;
        color: #2c3e50;
        page-break-before: always;
    }
    
    h1:first-child {
        page-break-before: avoid;
    }
    
    h2 {
        font-size: 16pt;
        font-weight: bold;
        margin: 10mm 0 5mm 0;
        color: #34495e;
    }
    
    h3 {
        font-size: 14pt;
        font-weight: bold;
        margin: 8mm 0 4mm 0;
        color: #34495e;
    }
    
    p {
        margin-bottom: 5mm;
        text-align: left;
    }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 5mm 0;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 3mm;
        text-align: center;
        font-size: 12pt;
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
        margin: 8mm 0;
    }
    
    /* Blank lines for answers */
    ._blank_line {
        border-bottom: 1px solid #333;
        display: inline-block;
        width: 60mm;
        margin: 0 2mm;
    }
    
    /* Page breaks between exercises */
    .page-break {
        page-break-before: always;
    }
    """)


def markdown_to_html(markdown_content):
    """Convert markdown content to HTML."""
    # Configure markdown with extensions
    md = markdown.Markdown(extensions=['tables', 'nl2br'])
    
    # Process the markdown content
    html_content = md.convert(markdown_content)
    
    # Replace underscores with styled blank lines for answers
    html_content = html_content.replace('_' * 20, '<span class="_blank_line"></span>')
    html_content = html_content.replace('_' * 15, '<span class="_blank_line"></span>')
    html_content = html_content.replace('_' * 10, '<span class="_blank_line"></span>')
    
    return html_content


def generate_unit_pdf(unit_number):
    """Generate PDF for a specific unit."""
    unit_dir = Path(f"unidad-{unit_number}")
    
    if not unit_dir.exists():
        print(f"Error: Unit directory {unit_dir} does not exist")
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
            6: "pagina-6-bien-mal.md"
        }
        
        page_file = unit_dir / page_files[i]
        if page_file.exists():
            with open(page_file, 'r', encoding='utf-8') as f:
                content = f.read()
                pages.append(content)
        else:
            print(f"Warning: {page_file} not found")
    
    if not pages:
        print(f"Error: No pages found for unit {unit_number}")
        return False
    
    # Combine all pages with page breaks
    combined_content = ""
    for i, page_content in enumerate(pages):
        if i > 0:
            combined_content += "\n\n<div class='page-break'></div>\n\n"
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
        <title>Cuadernillo de Español - Unidad {unit_number}</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Generate PDF
    output_file = f"unidad-{unit_number}.pdf"
    
    try:
        font_config = FontConfiguration()
        html_doc = HTML(string=full_html)
        css_style = create_css_style()
        
        html_doc.write_pdf(
            output_file,
            stylesheets=[css_style],
            font_config=font_config
        )
        
        print(f"✅ Generated {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error generating PDF for unit {unit_number}: {e}")
        return False


def main():
    """Main function to generate PDFs."""
    if len(sys.argv) > 1:
        # Generate specific unit
        try:
            unit_number = int(sys.argv[1])
            if unit_number not in [1, 2, 3]:
                print("Error: Unit number must be 1, 2, or 3")
                sys.exit(1)
            generate_unit_pdf(unit_number)
        except ValueError:
            print("Error: Please provide a valid unit number (1, 2, or 3)")
            sys.exit(1)
    else:
        # Generate all units
        print("Generating PDFs for all units...")
        success_count = 0
        for unit_num in [1, 2, 3]:
            if generate_unit_pdf(unit_num):
                success_count += 1
        
        print(f"\n🎉 Successfully generated {success_count}/3 unit PDFs")
        
        if success_count == 3:
            print("\nAll PDFs are ready for printing in DIN A5 format!")
        else:
            print("\nSome PDFs failed to generate. Check the error messages above.")


if __name__ == "__main__":
    main()