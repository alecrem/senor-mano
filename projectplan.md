# Project Plan: Implement Dual Licensing System (Issue #13)

## Overview
Implement a dual licensing approach for the ejercicios-espanol repository to properly distinguish between software components (MIT License) and educational content (CC BY-SA 4.0 License).

## Problem Analysis
Currently, the repository lacks proper licensing, making it unclear what permissions users and contributors have. The repository contains both technical software components and educational materials that serve different purposes and should have different licensing approaches.

## Solution Design

### Licensing Structure
- **MIT License**: For all software components (allows free commercial and non-commercial use)
- **CC BY-SA 4.0 License**: For educational content and illustrations (ensures content improvements are shared back)

### File Classification

#### Software Components (MIT License):
- PDF generation scripts (`ejercicios-src/scripts/`)
- Website code (`website/` directory)
- Build configuration files (`package.json`, `tsconfig.json`, `vite.config.ts`, etc.)
- Setup and deployment scripts (`generate_pdfs.sh`, `setup.sh`)
- Technical documentation (`PDF_GENERATION.md`)

#### Educational Content (CC BY-SA 4.0):
- All exercise content in `ejercicios-src/markdown/`
- Educational methodology in `CLAUDE.md`
- Sample materials and illustrations
- Generated PDF files (derivative works of educational content)

## Implementation Tasks

### Phase 1: License Files and Documentation
- [ ] Create MIT LICENSE file
- [ ] Create LICENSE-CC-BY-SA-4.0 file  
- [ ] Update README.md with dual licensing section
- [ ] Add license headers to key software files

### Phase 2: Website Updates
- [ ] Update website footer to include CC BY-SA 4.0 reference for educational materials
- [ ] Add repository link to website footer
- [ ] Ensure footer maintains clean, professional appearance

### Phase 3: Documentation and Clarity
- [ ] Create clear guidelines about which license applies to which parts
- [ ] Update contributing guidelines if they exist
- [ ] Test all changes to ensure website functionality

## Technical Considerations

### Website Footer Updates
The footer in `website/app/components/Layout.tsx` (lines 56-78) currently contains:
- Branding: "Señor Mano"
- Format info: "Formato DIN A5 optimizado para impresión"
- Language availability note

New footer will add:
- CC BY-SA 4.0 license reference for educational materials
- Repository link for transparency
- Maintain existing green styling (#6aad2f)

### File Structure Impact
No changes to existing file structure needed. License files will be added to repository root:
- `LICENSE` (MIT License for software)
- `LICENSE-CC-BY-SA-4.0` (Creative Commons for content)

## Success Criteria
1. Clear licensing for all repository components
2. Proper legal attribution in footer
3. Repository link accessible from website
4. Documentation reflects dual licensing approach
5. No breaking changes to existing functionality

## Timeline
Estimated completion: 2-3 hours
- Phase 1: 1-1.5 hours
- Phase 2: 30-45 minutes  
- Phase 3: 30-45 minutes

## Risk Assessment
- **Low Risk**: Changes are primarily additive
- **No Impact**: Existing functionality remains unchanged
- **Legal Clarity**: Proper licensing reduces legal ambiguity

## Post-Implementation
After completion, users will have:
- Clear understanding of what they can do with the software vs. content
- Proper attribution requirements for educational materials
- Access to repository source from the website
- Professional, legally compliant project presentation