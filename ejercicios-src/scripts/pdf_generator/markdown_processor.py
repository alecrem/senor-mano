"""
Markdown processing for PDF generation.

Handles conversion of markdown content to HTML with custom placeholder replacements
for answer lines and exercise formatting.
"""

import markdown


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