"""
File utilities for PDF generation.

Handles discovery and reading of markdown files from the exercise directory structure.
"""

from pathlib import Path


def get_available_cuadernillos(unit="present-tense", language="japanese"):
    """Get list of available cuadernillos for a given unit and language."""
    available = []
    verb_types = {1: "ar", 2: "er", 3: "ir", 4: "mixed"}

    for cuadernillo_num, verb_type in verb_types.items():
        # Check if cuadernillo directory exists for this unit
        cuadernillo_dir = Path(
            f"../markdown/{unit}/cuadernillo-{cuadernillo_num}-{verb_type}-verbs/{language}"
        )

        # Fallback to legacy multilingual structure
        if not cuadernillo_dir.exists():
            cuadernillo_dir = Path(
                f"../markdown/cuadernillo-{cuadernillo_num}-{verb_type}-verbs/{language}"
            )

            # Fallback to legacy structure
            if not cuadernillo_dir.exists():
                cuadernillo_dir = Path(f"../markdown/cuadernillo-{cuadernillo_num}")

        # Check if any required page files exist
        if cuadernillo_dir.exists():
            page_files = ["pagina-1-dialogo.md", "pagina-2-conjugacion-completar.md"]
            if any((cuadernillo_dir / page_file).exists() for page_file in page_files):
                available.append(cuadernillo_num)

    return available