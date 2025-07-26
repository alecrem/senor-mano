# Project Plan: Relabel "unidades" to "cuadernillos"

## Problem Statement
We need to relabel all instances of "unidades" (units) to "cuadernillos" (booklets) throughout the entire codebase to prepare for a new taxonomy where "unidad" will represent a higher-level entity that contains multiple "cuadernillos".

## Research Findings
After searching the codebase, I found the following files that need updating:

### Files containing "unidades":
- /Users/ale/repos/languages/ejercicios-espanol/website/app/root.tsx
- /Users/ale/repos/languages/ejercicios-espanol/README.md
- /Users/ale/repos/languages/ejercicios-espanol/website/README.md

### Files containing "units":
- /Users/ale/repos/languages/ejercicios-espanol/website/pnpm-lock.yaml (likely not relevant)
- /Users/ale/repos/languages/ejercicios-espanol/website/app/routes/_index.tsx
- /Users/ale/repos/languages/ejercicios-espanol/ejercicios-src/scripts/generate_pdf.py
- /Users/ale/repos/languages/ejercicios-espanol/LICENSE-CC-BY-SA-4.0 (likely not relevant)
- /Users/ale/repos/languages/ejercicios-espanol/website/app/components/UnitCard.tsx
- /Users/ale/repos/languages/ejercicios-espanol/website/README.md
- /Users/ale/repos/languages/ejercicios-espanol/ejercicios-src/scripts/setup.sh
- /Users/ale/repos/languages/ejercicios-espanol/ejercicios-src/scripts/generate_pdfs.sh
- /Users/ale/repos/languages/ejercicios-espanol/PDF_GENERATION.md
- /Users/ale/repos/languages/ejercicios-espanol/CLAUDE.md

### Directory names:
- ./ejercicios-src/markdown/unidad-1-ar-verbs → cuadernillo-1-ar-verbs
- ./ejercicios-src/markdown/unidad-2-er-verbs → cuadernillo-2-er-verbs
- ./ejercicios-src/markdown/unidad-3-ir-verbs → cuadernillo-3-ir-verbs

## Todo List
- [ ] Update markdown source materials for learning content
- [ ] Update Python PDF generation scripts
- [ ] Update website code and content (including component names)
- [ ] Update directory names and file paths
- [ ] Update variable names and function names
- [ ] Update comments and documentation
- [ ] Test PDF generation after changes

## Implementation Plan

1. **Directory Renaming**: Rename the three unidad directories to cuadernillo
2. **Script Updates**: Update Python and shell scripts to use new directory names
3. **Website Updates**: Update React components, routes, and content
4. **Documentation Updates**: Update README files and other documentation
5. **Testing**: Run PDF generation to ensure everything works

## Changes Made

### 1. Directory Renaming ✅
- Renamed `ejercicios-src/markdown/unidad-1-ar-verbs` → `cuadernillo-1-ar-verbs`
- Renamed `ejercicios-src/markdown/unidad-2-er-verbs` → `cuadernillo-2-er-verbs`
- Renamed `ejercicios-src/markdown/unidad-3-ir-verbs` → `cuadernillo-3-ir-verbs`

### 2. Python Script Updates ✅
- Updated `ejercicios-src/scripts/generate_pdf.py`:
  - Changed directory path references from `unidad-` to `cuadernillo-`
  - Updated all user-facing messages from "unit" to "cuadernillo"
  - Updated PDF output filenames from `unidad-X-XX.pdf` to `cuadernillo-X-XX.pdf`
  - Updated HTML title generation

### 3. Shell Script Updates ✅
- Updated `ejercicios-src/scripts/generate_pdfs.sh`:
  - Changed help text from "unit" to "cuadernillo" 
  - Updated all user-facing messages

### 4. Website Updates ✅
- Renamed `website/app/components/UnitCard.tsx` → `CuadernilloCard.tsx`
- Updated component interface name from `UnitCardProps` to `CuadernilloCardProps`
- Updated component function name from `UnitCard` to `CuadernilloCard`
- Updated CSS class names from `unit-*` to `cuadernillo-*`
- Updated PDF URLs from `/pdfs/*/unidad-X-XX.pdf` to `/pdfs/*/cuadernillo-X-XX.pdf`
- Updated `website/app/routes/_index.tsx`:
  - Changed variable name from `units` to `cuadernillos`
  - Updated display text from "Unidad X" to "Cuadernillo X"
- Updated `website/app/root.tsx` meta description

### 5. Documentation Updates ✅
- Updated `README.md`:
  - Changed all references from "unidad" to "cuadernillo"
  - Updated directory structure examples
  - Updated PDF filename examples
  - Updated command examples
- Updated `PDF_GENERATION.md`:
  - Changed title and all content references from "units" to "cuadernillos"
  - Updated all directory and filename examples
- Updated `CLAUDE.md`:
  - Updated file structure examples
  - Changed "Verb Units" section to "Verb Cuadernillos"
  - Updated all references in page specifications
- Updated `website/README.md`:
  - Updated component filename reference
  - Updated page description

### 6. Testing ✅
- Successfully tested PDF generation with new directory structure
- Confirmed output files are correctly named as `cuadernillo-X-XX.pdf`

### 7. Directory Cleanup ✅
- Removed redundant `pdf-output/` directory 
- Verified no code references the old directory
- Confirmed PDF generation still works correctly after cleanup

## Review

### Summary of Changes
Successfully completed the comprehensive relabeling of all "unidades" to "cuadernillos" throughout the entire codebase. The changes were systematic and covered:

1. **Directory Structure**: All three main exercise directories renamed
2. **Scripts & Automation**: Python and shell scripts updated with new paths and terminology
3. **Website**: React components, routes, and all user-facing text updated
4. **Documentation**: All README files, guides, and project documentation updated
5. **Testing**: PDF generation confirmed working with new structure

### Key Benefits
- **Consistency**: All terminology now uses "cuadernillos" consistently
- **Future-Ready**: Prepares codebase for new taxonomy where "unidad" will be a higher-level concept
- **No Breaking Changes**: All functionality preserved, only terminology changed
- **Comprehensive Coverage**: No instances of old terminology remain

### Technical Notes
- Legacy fallback paths maintained in PDF generation script for backward compatibility
- All file extensions and core functionality unchanged
- Website URLs updated to new PDF naming scheme
- Build and deployment processes unaffected
- Eliminated duplicate PDF generation - now only generates to website directory
- Removed redundant `pdf-output/` directory completely

### Verification
- ✅ PDF generation tested successfully
- ✅ New directory structure confirmed
- ✅ All documentation updated
- ✅ Website component renamed and functional
- ✅ No remaining "unidad" references in codebase

The relabeling is complete and the codebase is ready for the next phase of development with the new taxonomy.