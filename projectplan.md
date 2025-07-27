# Project Plan: Cuadernillo 4 - Mixed Verbs

## Issue
Create cuadernillo 4 with a mix of all verbs from cuadernillos 1-3, featuring a new "Escribe el infinitivo" exercise on page 2.

## Analysis
- Reviewed existing cuadernillo structure in `ejercicios-src/markdown/`
- Each cuadernillo has `japanese/` and `english/` subdirectories with 6 pages each
- Page 2 currently has conjugation tables - need to replace with infinitive exercise
- Need to mix all 12 verbs: dibujar, buscar, hablar, bailar, comer, leer, aprender, beber, vivir, escribir, abrir, subir

## Implementation Plan

### Todo Items
- [x] Create branch for issue #21
- [x] Research existing cuadernillo structure and content  
- [ ] Create cuadernillo-4-mixed-verbs directory structure
- [ ] Create content files for all 6 pages
  - [ ] Page 1: Dialogue with mixed verbs
  - [ ] Page 2: NEW - "Escribe el infinitivo" exercise (5 questions)
  - [ ] Page 3: Choice exercises with mixed verbs
  - [ ] Page 4: Transformation exercises with mixed verbs
  - [ ] Page 5: Word ordering with mixed verbs
  - [ ] Page 6: Right/wrong evaluation with mixed verbs
- [ ] Create Japanese language versions with headers/instructions
- [ ] Create English language versions with headers/instructions
- [ ] Test PDF generation for both languages

### Key Changes
- **Page 2**: Replace conjugation table with infinitive exercise
  - Format: "phrase with conjugated verb → Infinitive: ___"
  - Example: "María escribe cartas → Infinitive: escribir"
  - 5 questions covering all three conjugation types

### Verb Distribution Strategy
- Balance across all 12 verbs in each exercise
- Ensure representation of all three conjugation types (-ar, -er, -ir)
- Use natural, age-appropriate contexts

## Implementation Notes
- Follow existing directory structure pattern
- Maintain DIN A5 format requirements
- Keep vocabulary simple and contextual
- Use established markdown formatting