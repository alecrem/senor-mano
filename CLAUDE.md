# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains Spanish language exercises for children aged 7-16 who receive their education primarily in Japanese. These children have good listening comprehension and natural grammar usage in Spanish but need formal structure. They can read and write in Japanese but find Spanish reading/writing challenging.

## Content Structure and Standards

### Multilingual File Organization
The repository supports multiple languages (Japanese and English) while maintaining a single source of truth for Spanish content. Use this structure:

```
exercises/
├── cuadernillo-1-ar-verbs/
│   ├── content/
│   │   ├── dialogues.md
│   │   ├── conjugations.md
│   │   ├── choice-exercises.md
│   │   ├── transformation-exercises.md
│   │   ├── word-ordering.md
│   │   └── correct-incorrect.md
│   ├── japanese/
│   │   ├── pagina-1-dialogo.md
│   │   ├── pagina-2-conjugacion-completar.md
│   │   ├── pagina-3-eleccion.md
│   │   ├── pagina-4-transformacion.md
│   │   ├── pagina-5-ordenar.md
│   │   └── pagina-6-bien-mal.md
│   └── english/
│       ├── pagina-1-dialogo.md
│       ├── pagina-2-conjugacion-completar.md
│       ├── pagina-3-eleccion.md
│       ├── pagina-4-transformacion.md
│       ├── pagina-5-ordenar.md
│       └── pagina-6-bien-mal.md
├── cuadernillo-2-er-verbs/
│   └── (same structure)
└── cuadernillo-3-ir-verbs/
    └── (same structure)
```

### Content Management
- **content/**: Contains core Spanish exercises without language-specific headers
- **japanese/**: Contains complete pages with Japanese headers and instructions
- **english/**: Contains complete pages with English headers and instructions
- **Legacy structure**: The original `cuadernillo-[N]/` directories remain for backward compatibility

### Page Specifications

**Page 1: Dialogue (pagina-1-dialogo.md)**
- Contextualized dialogue between 2 characters
- 8-10 lines of dialogue
- Simple, everyday vocabulary
- Use at least 2 of the 4 cuadernillo verbs
- Clear narrative with familiar situations
- Format: **Name:** for each intervention

**Page 2: Conjugation and completion (pagina-2-conjugacion-completar.md)**
- Representative verb conjugation table
- Complete sentence example using the verb
- 5 completion exercises with personal pronouns
- Balanced distribution of the 4 cuadernillo verbs

**Page 3: Choice exercises (pagina-3-eleccion.md)**
- 6 multiple choice sentences
- Format: "subject [option1 | option2] rest of sentence"
- Blank line for writing complete sentence
- Use clear names/nouns (no omitted pronouns)

**Page 4: Transformation (pagina-4-transformacion.md)**
- 4 person-change exercises
- 2 question-answer dialogue exercises
- Format: "Yo verb → Nosotros **___**"

**Page 5: Word ordering (pagina-5-ordenar.md)**
- 6 word ordering exercises
- Line 1: "[word1 / word2 / word3 / word4 / word5]"
- Line 2: Translation of the ordered sentence (Japanese for Japanese version, English for English version)
- Blank line for handwritten correct sentence

**Page 6: Right/wrong (pagina-6-bien-mal.md)**
- 6 sentences to evaluate
- Format: "sentence. ___" (space for B/M)
- "Corrección: **___**" below each sentence

## Verb Cuadernillos

- **Cuadernillo 1**: First conjugation (-AR): dibujar, buscar, hablar, bailar
- **Cuadernillo 2**: Second conjugation (-ER): comer, leer, aprender, beber  
- **Cuadernillo 3**: Third conjugation (-IR): vivir, escribir, abrir, subir

## Content Guidelines

1. **Format requirements**: DIN A5 print format, large text, max 12 lines per page, max 10 words per line
2. **Language**: Headers and instructions in target language (Japanese for Japanese-educated students, English for English-educated students)
3. **Vocabulary**: Age-appropriate for 7-16 years, avoid complex words
4. **Contexts**: Home, school, family, daily activities
5. **Irregular verbs**: Avoid irregular verbs similar to study verbs (e.g., avoid "juego", use "jugar"; but "soy" or "haces" are acceptable)
6. **Capitalization**: Normal sentence capitalization in titles/headers (not title case)
7. **Progression**: From exposure to active production
8. **Connections**: Subtle links between exercises without being obvious

## Sample Content

Reference materials are available in the `./samples/` directory:
- `cuadernillos-espanol-1.md` (first conjugation -AR)
- `cuadernillos-espanol-2.md` (second conjugation -ER)
- `cuadernillos-espanol-3.md` (third conjugation -IR)

These samples are valid but need adaptation to current specifications (e.g., "bien/mal" instead of "verdadero/falso", target language headers, target language translations for word ordering exercises).

## Multilingual Implementation

The new structure separates content concerns:
- **Core Spanish content**: Maintained in `content/` subdirectories
- **Language-specific presentation**: Japanese and English versions in respective subdirectories
- **Consistency**: All Spanish exercises identical across languages, only headers/instructions translated
- **Scalability**: Easy to add new languages by creating new language subdirectories

## Markdown Template

Each file should begin with:
```markdown
# [Page Title]

## [Subtitle if applicable]

[Page content]
```

## PDF Testing Protocol

**Always test PDF generation for all cuadernillos** after making any changes that could affect PDF output, including:
- Modifying markdown content in exercise files
- Updating the PDF generation scripts (`generate_pdf.py`, `generate_pdfs.sh`)
- Changing directory structures or file paths
- Modifying CSS styles or PDF formatting
- Any other changes to the build system

This ensures:
- All placeholders render correctly
- Layout remains consistent
- No formatting issues arise
- All cuadernillos work in both languages

**Required testing command:**
```bash
./generate_pdfs.sh
```

This generates all cuadernillos in both Japanese and English to verify the complete system works properly.

**Exception:** When actively developing/debugging the generation scripts themselves, you may test with a single cuadernillo (e.g., `./generate_pdfs.sh 1 -l japanese`) for faster iteration, but always run the full test before completing your work.