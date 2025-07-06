#!/bin/bash

# Master build script for Spanish exercises
# Generates PDFs and HTML files for all languages and units

echo "🚀 Building all Spanish exercise materials..."

# Check if we're in the correct directory
if [[ ! -f "README.md" || ! -d "content" ]]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Check if virtual environment exists and activate it
if [[ -d "venv" ]]; then
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate
else
    echo "⚠️ Virtual environment not found. Run ./scripts/setup.sh first"
    exit 1
fi

# Create output directories
echo "📁 Creating output directories..."
mkdir -p output/pdfs/{ja,en,es}
mkdir -p docs/{ja,en,es}
mkdir -p docs/assets/css

# Generate PDFs for all languages and units
echo ""
echo "📄 Generating PDFs..."
python generators/generate_pdf_multilang.py --all-languages

# Generate HTML files for GitHub Pages
echo ""
echo "🌐 Generating HTML files..."
python generators/generate_html.py

# Copy PDF files to docs directory for web download
echo ""
echo "📋 Copying PDFs to web directory..."
cp -r output/pdfs/* docs/pdfs/ 2>/dev/null || mkdir -p docs/pdfs && cp -r output/pdfs/* docs/pdfs/

echo ""
echo "✅ Build complete!"
echo ""
echo "📊 Generated files:"
echo "  📄 PDFs: output/pdfs/ (and docs/pdfs/ for web)"
echo "  🌐 HTML: docs/ (ready for GitHub Pages)"
echo ""
echo "🔗 Next steps:"
echo "  • To preview locally: cd docs && python -m http.server 8000"
echo "  • To deploy: commit docs/ directory and enable GitHub Pages"
echo "  • To print: use PDF files in output/pdfs/"