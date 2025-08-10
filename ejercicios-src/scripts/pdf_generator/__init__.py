"""
PDF Generator package for Spanish exercise cuadernillos.

This package provides functionality to generate PDF files from Spanish exercise
markdown files, optimized for DIN A5 format with large text for children.

Copyright (c) 2025 alecrem
Licensed under the MIT License. See LICENSE file for details.
"""

from .css_styles import create_css_style
from .markdown_processor import markdown_to_html
from .file_utils import get_available_cuadernillos
from .pdf_builder import generate_cuadernillo_pdf

__all__ = [
    'create_css_style',
    'markdown_to_html', 
    'get_available_cuadernillos',
    'generate_cuadernillo_pdf'
]