#!/usr/bin/env python3
"""
Generate PDF files from Spanish exercise markdown files.
Optimized for DIN A5 format with large text for children.
Supports multi-language instructions (Japanese, English, Spanish).
"""

import os
import sys
import argparse
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
    # First, replace underscore patterns BEFORE markdown processing
    # to avoid markdown treating them as emphasis
    # IMPORTANT: Process longer patterns first to avoid partial matches
    
    # Long correction lines (page 6) - use 30+ underscores (FIRST!)
    original_content = markdown_content
    markdown_content = markdown_content.replace('_' * 33, '{{CORRECTION_LINE}}')
    markdown_content = markdown_content.replace('_' * 30, '{{CORRECTION_LINE}}')
    
    
    # Medium answer lines (pages 2, 4) - use 13-20 underscores  
    markdown_content = markdown_content.replace('_' * 20, '{{LONG_BLANK_LINE}}')
    markdown_content = markdown_content.replace('_' * 15, '{{LONG_BLANK_LINE}}')
    markdown_content = markdown_content.replace('_' * 13, '{{LONG_BLANK_LINE}}')
    
    # Short answer lines (page 3) - use 10 underscores
    markdown_content = markdown_content.replace('_' * 10, '{{BLANK_LINE}}')
    
    # Very short lines for B/M (page 6) - use 3 underscores (LAST!)
    markdown_content = markdown_content.replace('_' * 3, '{{SHORT_LINE}}')
    
    # Configure markdown with extensions
    md = markdown.Markdown(extensions=['tables', 'nl2br'])
    
    # Process the markdown content
    html_content = md.convert(markdown_content)
    
    # Now replace the placeholders with actual HTML
    html_content = html_content.replace('{{CORRECTION_LINE}}', '<span class="_correction_line"></span>')
    html_content = html_content.replace('{{LONG_BLANK_LINE}}', '<span class="_long_blank_line"></span>')
    html_content = html_content.replace('{{BLANK_LINE}}', '<span class="_blank_line"></span>')
    html_content = html_content.replace('{{SHORT_LINE}}', '<span class="_short_line"></span>')
    
    return html_content


def load_translations(language='ja'):
    """Load translation strings for the specified language."""
    translation_file = Path(f"content/translations/{language}.yaml")
    
    if not translation_file.exists():
        print(f"Warning: Translation file {translation_file} not found, using Japanese as fallback")
        translation_file = Path("content/translations/ja.yaml")
    
    try:
        with open(translation_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error: Could not load translations: {e}")
        return {}


def generate_page_content(unit_number, page_type, translations):
    """Generate content for a specific page with translated headers."""
    content_file = Path(f"content/units/unit-{unit_number}/{page_type}.md")
    
    if not content_file.exists():
        print(f"Warning: Content file {content_file} not found")
        return ""
    
    # Read the markdown content
    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add translated header based on page type
    header_map = {
        'dialogue': translations.get('dialogue_header', '会話 (Diálogo)'),
        'conjugation': translations.get('conjugation_header', '動詞の活用と完成 (Conjugación y completar)'),
        'choice': translations.get('choice_header', '選択問題 (Ejercicios de elección)'),
        'transformation': translations.get('transformation_header', '変換練習 (Ejercicios de transformación)'),
        'ordering': translations.get('ordering_header', '語順並べ替え (Ejercicios de ordenar)'),
        'correction': translations.get('correction_header', '正しい・間違い (Bien / Mal)')
    }
    
    header = header_map.get(page_type, page_type.title())
    
    # Add instructions for specific page types
    if page_type == 'conjugation':
        instruction = translations.get('conjugation_instructions', '正しい形で空欄を埋めてください (Completa con la forma correcta):')
        content += f"\n\n### {instruction}"
    elif page_type == 'choice':
        instruction = translations.get('choice_instructions', '正しい形を選んで完全な文を書いてください:')
        content = f"### {instruction}\n\n{content}"
    elif page_type == 'transformation':
        instruction = translations.get('transformation_instructions', '指示に従って動詞の人称を変えてください:')
        qa_header = translations.get('transformation_qa_header', '質問に答えてください:')
        # Split transformation content at the "---" divider and add headers
        if '---' in content:
            parts = content.split('---', 1)
            content = f"### {instruction}\n\n{parts[0]}\n\n---\n\n### {qa_header}\n\n{parts[1]}"
        else:
            content = f"### {instruction}\n\n{content}"
    elif page_type == 'ordering':
        instruction = translations.get('ordering_instructions', '単語を並べ替えて正しい文を作ってください:')
        content = f"### {instruction}\n\n{content}"
    elif page_type == 'correction':
        instruction = translations.get('correction_instructions', '文を読んで、正しければB、間違っていればMを書き、間違いを訂正してください:')
        content = f"### {instruction}\n\n{content}"
    
    return f"## {header}\n\n{content}"


def generate_unit_pdf(unit_number, language='ja', output_dir='output/pdfs'):
    """Generate PDF for a specific unit with specified language."""
    unit_dir = Path(f"content/units/unit-{unit_number}")
    
    if not unit_dir.exists():
        print(f"Error: Unit directory {unit_dir} does not exist")
        return False
    
    # Load translations
    translations = load_translations(language)
    
    # Load unit metadata
    metadata_file = unit_dir / "metadata.yaml"
    unit_title = f"Unidad {unit_number}"  # Default fallback
    
    if metadata_file.exists():
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = yaml.safe_load(f)
                unit_title = metadata.get('title', unit_title)
        except Exception as e:
            print(f"Warning: Could not read metadata: {e}")
    
    # Generate content for each page type
    page_types = ['dialogue', 'conjugation', 'choice', 'transformation', 'ordering', 'correction']
    pages = []
    
    for page_type in page_types:
        page_content = generate_page_content(unit_number, page_type, translations)
        if page_content:
            pages.append(page_content)
    
    if not pages:
        print(f"Error: No pages found for unit {unit_number}")
        return False
    
    # Combine all pages with page breaks
    combined_content = f"# {unit_title}\n\n"
    
    for i, page_content in enumerate(pages):
        if i > 0:
            combined_content += "\n\n<div style='page-break-before: always;'></div>\n\n"
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
        <title>Cuadernillo de Español - Unidad {unit_number} ({translations.get('language_name', 'Japanese')})</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir) / language
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate PDF
    output_file = output_path / f"unidad-{unit_number}.pdf"
    
    try:
        font_config = FontConfiguration()
        html_doc = HTML(string=full_html)
        css_style = create_css_style(unit_title)
        
        html_doc.write_pdf(
            str(output_file),
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
    parser = argparse.ArgumentParser(description='Generate Spanish exercise PDFs with multi-language support')
    parser.add_argument('--unit', type=int, choices=[1, 2, 3], help='Generate PDF for specific unit (1-3)')
    parser.add_argument('--language', type=str, choices=['ja', 'en', 'es'], default='ja', 
                       help='Language for instructions (ja=Japanese, en=English, es=Spanish)')
    parser.add_argument('--output', type=str, default='output/pdfs', help='Output directory for PDFs')
    parser.add_argument('--all-languages', action='store_true', help='Generate PDFs in all languages')
    
    args = parser.parse_args()
    
    languages = ['ja', 'en', 'es'] if args.all_languages else [args.language]
    units = [args.unit] if args.unit else [1, 2, 3]
    
    total_pdfs = len(languages) * len(units)
    success_count = 0
    
    print(f"Generating {total_pdfs} PDFs...")
    
    for language in languages:
        lang_name = {'ja': 'Japanese', 'en': 'English', 'es': 'Spanish'}[language]
        print(f"\n📚 Generating {lang_name} versions...")
        
        for unit_num in units:
            if generate_unit_pdf(unit_num, language, args.output):
                success_count += 1
    
    print(f"\n🎉 Successfully generated {success_count}/{total_pdfs} unit PDFs")
    
    if success_count == total_pdfs:
        print("\nAll PDFs are ready for printing in DIN A5 format!")
        if args.all_languages:
            print("Generated in Japanese (ja/), English (en/), and Spanish (es/) subdirectories.")
    else:
        print("\nSome PDFs failed to generate. Check the error messages above.")


if __name__ == "__main__":
    main()