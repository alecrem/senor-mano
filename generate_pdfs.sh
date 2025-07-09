#!/bin/bash
# Backward compatibility wrapper for the PDF generation script
# This script forwards all arguments to the new location

echo "📦 Forwarding to new script location..."
exec ejercicios-src/scripts/generate_pdfs.sh "$@"