#!/usr/bin/env python3
"""
Generate PDF files from Spanish exercise markdown files.
Optimized for DIN A5 format with large text for children.

Copyright (c) 2025 alecrem
Licensed under the MIT License. See LICENSE file for details.
"""

import sys
from pdf_generator import get_available_cuadernillos, generate_cuadernillo_pdf


def main():
    """Main function to generate all PDFs."""
    # Check for any arguments and show error if provided
    if len(sys.argv) > 1:
        print("Error: This script does not accept any arguments.")
        print("Usage: python generate_pdfs.py")
        print("This script always generates ALL available cuadernillos for ALL units in BOTH languages.")
        print("This ensures consistency and prevents partial generations that could cause confusion.")
        sys.exit(1)

    # Always generate all available cuadernillos for all units in all languages
    languages_to_generate = ["japanese", "english"]
    units_to_generate = ["present-tense", "past-tense"]
    
    total_success = 0
    total_attempted = 0

    for lang in languages_to_generate:
        for unit_name in units_to_generate:
            available = get_available_cuadernillos(unit_name, lang)
            if available:
                print(
                    f"Generating {unit_name} cuadernillos {available} in {lang}..."
                )
                for cuadernillo_num in available:
                    total_attempted += 1
                    if generate_cuadernillo_pdf(cuadernillo_num, lang, unit_name):
                        total_success += 1
            else:
                print(f"No {unit_name} cuadernillos found for {lang}")

    if total_attempted == 0:
        print(f"❌ No cuadernillos found")
        sys.exit(1)
    else:
        print(
            f"\n🎉 Successfully generated {total_success}/{total_attempted} cuadernillo PDFs for all languages"
        )
        if total_success == total_attempted:
            print(
                f"\nAll available PDFs are ready for printing in DIN A5 format!"
            )
        else:
            print(
                f"\nSome PDFs failed to generate. Check the error messages above."
            )


if __name__ == "__main__":
    main()