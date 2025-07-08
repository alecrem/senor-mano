# Project Plan: Fix Underscore Linter Conflicts (Issue #5)

## Problem Analysis

The exercise files contain underscores (`___`) used to create answer lines for students in printed PDFs. Markdown linters automatically modify these underscores, causing inconsistent formatting and breaking the visual appearance of the exercises.

### Current Underscore Usage Patterns

After analyzing the codebase, I found 28 files containing underscores with the following patterns:

1. **Page 2 (Conjugation)**: Long underscores (~15 characters) for fill-in-the-blank exercises
2. **Page 3 (Choice)**: Long underscores (~33 characters) for complete sentence writing 
3. **Page 6 (Bien/Mal)**: Long underscores (~33 characters) for correction writing
4. **Page 4 (Transformation)**: Some files have underscores for transformation exercises
5. **Page 5 (Ordering)**: Some files have underscores for answer lines

### Affected Files
- All 3 units (AR, ER, IR verbs)
- Both Japanese and English versions
- Primarily pages 2, 3, 4, 5, and 6

## Proposed Solution

Based on the issue description and user feedback, I recommend **Option 4: HTML/CSS solution with placeholders**.

### Why HTML/CSS Placeholders?
- **Completely linter-safe**: No special characters to trigger formatting
- **Professional output**: Clean, consistent lines styled with CSS
- **Flexible formatting**: Easy to adjust line width, thickness, spacing globally
- **Clean markdown**: Simple placeholders instead of long character strings
- **Maintainable**: Single point of control for all answer line styling
- **Future-proof**: Can easily adapt styling for different output formats

### Implementation Strategy

1. **Replace underscore patterns** with semantic HTML placeholders:
   - Short lines (conjugation): `<div class="answer-line-short"></div>`
   - Long lines (choice/correction): `<div class="answer-line-long"></div>`

2. **CSS styling** will handle the visual formatting:
   ```css
   .answer-line-short {
     border-bottom: 1px solid black;
     height: 1.5em;
     width: 8em;
     display: inline-block;
     margin: 0 0.2em;
   }
   
   .answer-line-long {
     border-bottom: 1px solid black;
     height: 1.5em;
     width: 100%;
     display: block;
     margin: 0.2em 0;
   }
   ```

3. **Test PDF generation** to ensure proper formatting and styling is applied

## Todo List

- [x] Analyze current underscore usage in exercise files to understand the scope
- [x] Write project plan to projectplan.md with detailed analysis and approach
- [x] Get user approval for the plan before implementing changes
- [x] Replace underscores with HTML placeholders in all affected exercise files
- [x] Test the changes by generating PDFs to ensure proper formatting
- [x] Commit changes and add review section to projectplan.md

## Expected Outcomes

- **Eliminated linter conflicts**: No more automatic underscore modifications
- **Professional PDF formatting**: Clean, consistent lines styled with CSS
- **Enhanced flexibility**: Easy to adjust line appearance globally
- **Cleaner markdown**: Simple placeholders instead of character strings
- **Preserved functionality**: Students can still write answers clearly
- **Improved maintainability**: Single point of control for styling

## Files to Modify

All 28 files identified in the analysis, spanning:
- `exercises/unidad-1-ar-verbs/japanese/` (5 files)
- `exercises/unidad-1-ar-verbs/english/` (5 files)
- `exercises/unidad-2-er-verbs/japanese/` (4 files)
- `exercises/unidad-2-er-verbs/english/` (5 files)
- `exercises/unidad-3-ir-verbs/japanese/` (5 files)
- `exercises/unidad-3-ir-verbs/english/` (5 files)

## Next Steps

1. Get user approval for this HTML/CSS placeholder approach
2. Implement the placeholder replacements systematically
3. Test PDF generation to verify CSS styling works correctly
4. Document the new placeholder system for future reference

## Additional Considerations

- **PDF generation process**: Need to ensure the CSS is properly included in PDF output
- **Placeholder documentation**: Create reference for future contributors
- **Styling consistency**: Ensure all answer lines have uniform appearance
- **Testing**: Verify that lines print at appropriate thickness and spacing

## Review

### Implementation Summary

Successfully implemented HTML/CSS placeholder solution for underscore linter conflicts across all Spanish exercise files. The solution replaced problematic underscore patterns with clean HTML div elements that are styled via CSS during PDF generation.

### Key Changes Made

1. **Exercise Files Updated (28 files total)**:
   - All `_______________` patterns → `<div class="answer-line-short"></div>`
   - All `_________________________________` patterns → `<div class="answer-line-long"></div>`
   - Cleaned up any remaining underscore artifacts

2. **PDF Generation Enhanced**:
   - Added CSS styles for `.answer-line-short` and `.answer-line-long` classes
   - Short lines: 25mm width, inline display for fill-in-the-blank exercises
   - Long lines: 100% width, block display for full sentence answers
   - Proper spacing and minimum height for handwriting

3. **Files Modified**:
   - All exercise files in `exercises/unidad-[1-3]-*-verbs/[japanese|english]/`
   - `generate_pdf.py` - Updated with CSS for new placeholder classes

### Benefits Achieved

- **Eliminated linter conflicts**: No more automatic underscore modifications
- **Professional PDF output**: Clean, consistent lines with proper CSS styling
- **Maintainable solution**: Single point of CSS control for all answer lines
- **Clean markdown**: Simple HTML placeholders instead of character strings
- **Future-proof**: Easy to adjust styling globally without touching individual files

### Testing Results

- PDF generation tested successfully for Unit 1 in both Japanese and English
- HTML placeholders render correctly as styled lines in PDF output
- No underscore patterns remain in any exercise files
- All answer line functionality preserved for student use

### Technical Implementation

The solution uses semantic HTML div elements with CSS classes that render as answer lines in the PDF output. This approach is completely linter-safe and provides flexible styling control through CSS, making it easy to adjust line appearance, spacing, and formatting for different exercise types.

This implementation resolves Issue #5 completely and establishes a robust foundation for future exercise file maintenance.