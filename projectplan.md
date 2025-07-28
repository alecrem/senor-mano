# Project Plan: Add Past Tense Unit Structure

## Overview
This project implements support for multiple grammar units in the Spanish exercises system, starting with a Past Tense unit alongside the existing Present Tense unit.

## Todo Items
- [x] Create GitHub issue for enabling different units structure (#27)
- [x] Create new Past Tense unit structure with first conjugation booklet  
- [x] Update Python scripts to support multiple units
- [x] Test PDF generation for new Past Tense booklet

## Implementation Details

### 1. Directory Structure
Created new units-based directory structure:
```
ejercicios-src/markdown/
├── present-tense/
│   ├── cuadernillo-1-ar-verbs/
│   ├── cuadernillo-2-er-verbs/
│   ├── cuadernillo-3-ir-verbs/
│   └── cuadernillo-4-mixed-verbs/
└── past-tense/
    └── cuadernillo-1-ar-verbs/
        ├── content/
        ├── japanese/
        └── english/
```

### 2. Past Tense Content Created
Created complete past-tense cuadernillo-1-ar-verbs with:
- **Verbs**: dibujar, buscar, hablar, bailar (past tense: dibujé, busqué, hablé, bailé)
- **6 pages**: dialogue, conjugation, choice exercises, transformation, word ordering, right/wrong
- **Both languages**: Japanese and English versions with appropriate headers and translations
- **Same structure**: Follows existing 6-page format and DIN A5 specifications

### 3. Updated Scripts
Modified both Python and shell scripts to support units:
- **generate_pdf.py**: Added `unit` parameter with fallback compatibility
- **generate_pdfs.sh**: Added `-u/--unit` option supporting present-tense, past-tense, or both
- **Backward compatibility**: Scripts still work with existing present-tense structure

### 4. Testing Results
✅ Successfully generated PDFs for:
- Past-tense cuadernillo 1 (Japanese and English)
- Present-tense cuadernillo 1 (verified still working)
- All PDFs output to website/public/pdfs/ directory

## Changes Made

### Files Added
- `ejercicios-src/markdown/past-tense/cuadernillo-1-ar-verbs/content/` (6 files)
- `ejercicios-src/markdown/past-tense/cuadernillo-1-ar-verbs/japanese/` (6 files)  
- `ejercicios-src/markdown/past-tense/cuadernillo-1-ar-verbs/english/` (6 files)

### Files Modified  
- `ejercicios-src/scripts/generate_pdf.py` - Added unit support with backward compatibility
- `ejercicios-src/scripts/generate_pdfs.sh` - Added unit parameter handling

### Files Moved
- Moved existing cuadernillos from `ejercicios-src/markdown/cuadernillo-*` to `ejercicios-src/markdown/present-tense/cuadernillo-*`

## Next Steps
- Implement cuadernillo-2-er-verbs and cuadernillo-3-ir-verbs for past-tense unit (future)
- Update website routing to handle multiple units (future)
- Add unit selection in user interface (future)