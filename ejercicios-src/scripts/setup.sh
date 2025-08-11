#!/bin/bash
# Setup script for PDF generation

echo "Setting up PDF generation environment..."

# Set preferred Python version (you can change this)
PYTHON_VERSION="${PYTHON_VERSION:-python3.12}"

# Check if the specified Python version is available
if ! command -v $PYTHON_VERSION &> /dev/null; then
    echo "❌ $PYTHON_VERSION is not available"
    echo "Available versions:"
    ls -1 /opt/homebrew/bin/python3* | grep -E "python3\.[0-9]+$"
    exit 1
fi

echo "Using $PYTHON_VERSION"

# Create virtual environment if it doesn't exist (in project root)
if [ ! -d "../../venv" ]; then
    echo "Creating virtual environment with $PYTHON_VERSION..."
    cd ../..
    $PYTHON_VERSION -m venv venv
    cd ejercicios-src/scripts
fi

# Activate virtual environment
echo "Activating virtual environment..."
source ../../venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Make scripts executable
chmod +x generate_pdf.py

echo "✅ Setup complete!"