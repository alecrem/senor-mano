# Project Plan: Multilingual Spanish Exercise Structure

## Goal
Implement a multilingual content structure that allows creating English versions of Spanish exercise PDFs while maintaining Japanese versions, using Option B (separate language-specific sections).

## Problem
Currently, Spanish exercises are designed for Japanese-educated children. We need versions for English-educated children with translated instructions while keeping Spanish content identical.

## Solution Overview
Using Option B content separation strategy:
```
unidad-[N]/
├── content/
│   ├── pagina-1-spanish-content.md (Spanish exercises)
│   └── ...
├── japanese/
│   ├── pagina-1-dialogo.md (Japanese headers + Spanish content)
│   └── ...
└── english/
    ├── pagina-1-dialogo.md (English headers + Spanish content)
    └── ...
```

## Implementation Plan

### Phase 1: Structure Setup
- [x] Create project plan
- [ ] Create feature branch
- [ ] Analyze existing sample content
- [ ] Create new directory structure

### Phase 2: Content Migration
- [ ] Extract core Spanish content from samples
- [ ] Create Japanese versions maintaining existing format
- [ ] Create English versions with translated instructions

### Phase 3: Documentation and Testing
- [ ] Update CLAUDE.md with new structure guidelines
- [ ] Test and validate content consistency

## Key Requirements
1. **Maintainability**: Single source of truth for Spanish content
2. **Consistency**: Spanish exercises identical across languages
3. **Scalability**: Easy to add more languages
4. **Simplicity**: Follow existing exercise specifications

## Translation Elements
- **Need translation**: Headers, instructions, word ordering translations
- **Stay same**: All Spanish dialogues, sentences, vocabulary, exercise formats

## Success Criteria
- English-speaking students can use the same Spanish exercises
- Content maintenance remains simple (no duplication of Spanish content)
- Clear structure for future language additions
- Maintains existing exercise quality and format

## Review

### Implementation Summary
Successfully implemented the multilingual content structure using Option B approach. Created:

1. **New directory structure**: `exercises/unidad-[N]-[type]-verbs/` with `content/`, `japanese/`, and `english/` subdirectories
2. **Core Spanish content**: Extracted pure Spanish exercises into `content/` files (6 files per unit × 3 units = 18 core files)
3. **Japanese versions**: Created complete pages with Japanese headers and instructions (6 files per unit × 3 units = 18 files)
4. **English versions**: Created complete pages with English headers and instructions (6 files per unit × 3 units = 18 files)
5. **Documentation**: Updated CLAUDE.md with new structure guidelines and multilingual implementation details

### Key Achievements
- **Content consistency**: Spanish exercises identical across all language versions
- **Proper translations**: Headers, instructions, and word ordering translations correctly implemented
- **Maintainability**: Single source of truth for Spanish content prevents duplication
- **Scalability**: Structure allows easy addition of new languages
- **Backward compatibility**: Legacy structure preserved

### Structure Validation
- ✅ Spanish dialogue content identical across versions
- ✅ Headers properly translated (Japanese: "ページ 1: 対話", English: "Page 1: Dialogue")
- ✅ Instructions translated (Japanese: "単語を正しい順序に並べて文を作りなさい", English: "Put the words in the correct order to form sentences")
- ✅ Word ordering translations accurate (Japanese: "私の兄は上手に踊ります", English: "My brother dances very well")
- ✅ Exercise formats maintained consistently

### Benefits Achieved
1. **For English-speaking students**: Can now use identical Spanish exercises with English instructions
2. **For content maintainers**: Single source of truth reduces maintenance burden
3. **For future expansion**: Easy to add new languages (French, German, etc.) by creating new language subdirectories
4. **For consistency**: Automated processes possible for ensuring content stays in sync

### Next Steps
- Consider implementing templating system for automated generation of language-specific files
- Add build process for generating PDFs from multilingual content
- Create comprehensive content for all units (currently demonstrated with key samples)
- Test with actual students to validate effectiveness