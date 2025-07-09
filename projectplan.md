# Project Plan: Organize Repository File Structure (Issue #7)

## Overview
Reorganize the repository structure to improve maintainability by separating source content, build tools, and outputs into logical directories.

## Current State Analysis
- Exercise markdown files in `exercises/` subdirectories
- PDF generation scripts in root (`generate_pdf.py`, `generate_pdfs.sh`)
- Generated PDF files in root (`unidad-*.pdf`)
- Supporting files in root (`requirements.txt`, `setup.sh`)
- Documentation files in root

## Proposed New Structure
```
ejercicios-src/
├── markdown/                    # Source markdown files
│   ├── unidad-1-ar-verbs/
│   ├── unidad-2-er-verbs/
│   └── unidad-3-ir-verbs/
├── scripts/                      # PDF generation tools
│   ├── generate_pdf.py
│   ├── generate_pdfs.sh
│   ├── requirements.txt
│   └── setup.sh
└── templates/ (if needed)        # CSS/HTML templates for PDF generation

pdf-output/
├── japanese/
│   ├── unidad-1-ja.pdf
│   ├── unidad-2-ja.pdf
│   └── unidad-3-ja.pdf
└── english/
    ├── unidad-1-en.pdf
    ├── unidad-2-en.pdf
    └── unidad-3-en.pdf
```

## Todo List

### Phase 1: Create new directory structure
- [x] Create `ejercicios-src/` directory
- [x] Create `ejercicios-src/markdown/` directory
- [x] Create `ejercicios-src/scripts/` directory
- [x] Create `pdf-output/` directory
- [x] Create `pdf-output/japanese/` directory
- [x] Create `pdf-output/english/` directory

### Phase 2: Move source files
- [x] Move `exercises/` contents to `ejercicios-src/markdown/`
- [x] Remove empty `exercises/` directory

### Phase 3: Move build tools
- [x] Move `generate_pdf.py` to `ejercicios-src/scripts/`
- [x] Move `generate_pdfs.sh` to `ejercicios-src/scripts/`
- [x] Move `requirements.txt` to `ejercicios-src/scripts/`
- [x] Move `setup.sh` to `ejercicios-src/scripts/`

### Phase 4: Move PDF outputs
- [x] Move Japanese PDFs to `pdf-output/japanese/`
- [x] Move English PDFs to `pdf-output/english/`

### Phase 5: Update scripts and paths
- [x] Update `generate_pdf.py` to work with new directory structure
- [x] Update `generate_pdfs.sh` to work with new directory structure
- [x] Update `setup.sh` to work with new directory structure
- [x] Create backward compatibility wrapper script

### Phase 6: Update documentation
- [x] Update `README.md` to reflect new structure
- [x] Update `PDF_GENERATION.md` to reflect new paths
- [x] Update `CLAUDE.md` if needed (no changes required)

### Phase 7: Test and validate
- [x] Test PDF generation with new structure
- [x] Verify all scripts work correctly
- [x] Ensure backward compatibility considerations

## Implementation Notes
- All script paths and references need updating
- PDF generation should continue to work seamlessly
- Maintain clear documentation of the new structure
- Consider impact on any CI/CD processes

## Review Section

### Summary of Changes Made
✅ **Successfully reorganized the repository structure according to issue #7**

### Key Accomplishments:
1. **Created organized directory structure:**
   - `ejercicios-src/markdown/` - Contains all exercise source files
   - `ejercicios-src/scripts/` - Contains all build tools and dependencies
   - `pdf-output/japanese/` and `pdf-output/english/` - Organized PDF outputs

2. **Moved all files to appropriate locations:**
   - Exercise markdown files moved from `exercises/` to `ejercicios-src/markdown/`
   - Build scripts moved from root to `ejercicios-src/scripts/`
   - PDF outputs moved from root to organized subdirectories
   - Virtual environment remains in project root for accessibility

3. **Updated all scripts for new structure:**
   - `generate_pdf.py` - Updated paths to reference `../markdown/` and output to `../../pdf-output/`
   - `generate_pdfs.sh` - Updated to work from scripts directory and use virtual environment from project root
   - `setup.sh` - Updated to create virtual environment in project root and work from scripts directory
   - Created backward compatibility wrapper script in project root

4. **Updated documentation:**
   - `README.md` - Updated all paths, commands, and examples to reflect new structure
   - `PDF_GENERATION.md` - Updated all references to new script locations and output paths
   - `CLAUDE.md` - No changes required as it uses relative project structure

5. **Verified functionality:**
   - Successfully tested PDF generation with new structure
   - Confirmed proper file organization in output directories
   - Validated backward compatibility through wrapper script

### Benefits Achieved:
- **Clear separation** between source content, build tools, and outputs
- **Improved maintainability** with logical directory organization
- **Better organization** for CI/CD and automation workflows
- **Maintained backward compatibility** through wrapper scripts
- **Enhanced scalability** for future enhancements

### Files Modified:
- `ejercicios-src/scripts/generate_pdf.py` - Path updates
- `ejercicios-src/scripts/generate_pdfs.sh` - Path and working directory updates
- `ejercicios-src/scripts/setup.sh` - Virtual environment and path updates
- `generate_pdfs.sh` (new) - Backward compatibility wrapper
- `README.md` - Documentation updates
- `PDF_GENERATION.md` - Documentation updates

### Testing Completed:
- ✅ PDF generation working correctly
- ✅ Output files created in proper directories
- ✅ Backward compatibility maintained
- ✅ Virtual environment setup functioning
- ✅ All documentation references updated correctly

The repository reorganization has been completed successfully and provides a much cleaner, more maintainable structure.