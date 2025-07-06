#!/bin/bash

# Setup script for Spanish exercises PDF generator
# Creates virtual environment and installs dependencies

echo "🚀 Setting up Spanish exercises environment..."

# Check if we're in the correct directory
if [[ ! -f "README.md" || ! -d "content" ]]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing dependencies..."
pip install -r generators/requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To activate the environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To generate PDFs, run:"
echo "  python generators/generate_pdf_multilang.py --help"