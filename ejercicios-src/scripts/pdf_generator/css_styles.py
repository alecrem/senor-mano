"""
CSS styling for PDF generation.

Provides CSS styling optimized for DIN A5 format with large text suitable for children.
"""

from weasyprint import CSS


def create_css_style(unit_title=""):
    """Create CSS styling for DIN A5 format with compact layout."""
    css_template = """
    @page {
        size: A5;
        margin: 18mm 8mm 15mm 8mm;
        @top-left {
            content: "© Señor Mano · Licencia CC BY-SA 4.0";
            font-family: "Lato";
            font-size: 8pt;
            color: #666666;
        }
        @top-right {
            content: "https://senormano.alecrem.com/";
            font-family: "Lato";
            font-size: 8pt;
            color: #666666;
        }
        @bottom-left {
            content: "UNIT_TITLE_PLACEHOLDER";
            font-family: "Lato";
            font-size: 9pt;
            color: #666666;
        }
        @bottom-right {
            content: counter(page);
            font-family: "Lato";
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

    # Replace the placeholder with the actual unit title
    css_content = css_template.replace(
        "UNIT_TITLE_PLACEHOLDER", f"Unidad: {unit_title}" if unit_title else ""
    )
    return CSS(string=css_content)