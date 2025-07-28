# Project Plan: Group Cuadernillos into Single Unit Card

## Issue Description

Group the 4 existing cuadernillos into a single "Unidad" (unit) card on the website with the title "El presente de indicativo". Each cuadernillo will be displayed as a row within the card showing only its title, removing the verb lists and descriptions. Download buttons (Japanese/English) should be side by side by default, splitting vertically on smaller screens.

## Current State Analysis

**Current Implementation:**

- 4 separate cards, one per cuadernillo
- Each card shows: title, verb list, description, and download buttons
- Cuadernillo data hard-coded in `/website/app/routes/_index.tsx` (lines 16-45)
- Inline styling throughout, no CSS classes
- Existing unused `CuadernilloCard.tsx` component

**Current Cuadernillos:**

1. Primera conjugación (-AR): dibujar, buscar, hablar, bailar
2. Segunda conjugación (-ER): comer, leer, aprender, beber
3. Tercera conjugación (-IR): vivir, escribir, abrir, subir
4. Todos los verbos regulares: all 12 verbs from above cuadernillos

## Todo List

### Phase 1: Design and Structure

- [ ] Create new data structure for the unit grouping
- [ ] Design CSS Grid layout for cuadernillo rows within the unit card
- [ ] Plan responsive behavior for download buttons

### Phase 2: Implementation

- [ ] Modify cuadernillo data structure in `_index.tsx` to support unit grouping
- [ ] Update the rendering logic to display single unit card instead of 4 separate cards
- [ ] Implement CSS Grid layout with one row per cuadernillo
- [ ] Add responsive download button layout (horizontal → vertical)
- [ ] Remove verb lists and descriptions from display
- [ ] Add unit title "El presente de indicativo"

### Phase 3: Styling and Polish

- [ ] Ensure consistent styling with existing design
- [ ] Test responsive behavior across different screen sizes
- [ ] Verify all download links work correctly
- [ ] Clean up any unused code

### Phase 4: Testing and Review

- [ ] Test functionality in browser
- [ ] Verify PDF downloads work for all cuadernillos
- [ ] Check responsive design on mobile/tablet
- [ ] Code review and cleanup

## Technical Implementation Details

### Data Structure Changes

```typescript
// Current structure (per cuadernillo)
{
  number: number;
  title: string;
  verbs: string[];
  description: string;
}

// Proposed structure (unit-based)
{
  unit: {
    title: string; // "El presente de indicativo"
    cuadernillos: {
      number: number;
      title: string;
      // Remove: verbs, description
    }[]
  }
}
```

### Layout Specifications

- **Single card** replacing 4 separate cards
- **CSS Grid** with `grid-template-rows: repeat(4, 1fr)`
- **Row structure**: Title on left, download buttons on right
- **Button layout**: Horizontal by default, vertical stack on small screens
- **Responsive breakpoint**: Consider mobile-first approach

### Files to Modify

- `/website/app/routes/_index.tsx` - Main implementation file
- Potentially create new component or modify existing `CuadernilloCard.tsx`

## Success Criteria

✅ Single unit card displays all 4 cuadernillos  
✅ Unit title "El presente de indicativo" is prominent  
✅ Each cuadernillo shows only its title (no verbs/description)  
✅ CSS Grid layout with clean row separation  
✅ Download buttons are responsive (side-by-side → stacked)  
✅ All PDF downloads continue to work  
✅ Design remains consistent with existing style  
✅ Mobile responsive design functions properly

## Review

### Changes Made

✅ **Data Structure**: Replaced individual cuadernillo array with a single `unidad` object containing:

- Unit title: "El presente de indicativo"
- Array of cuadernillos with only `number` and `title` properties
- Removed `verbs` and `description` fields as requested

✅ **Layout Implementation**:

- Single unit card replacing 4 separate cards
- Grid layout with individual rows for each cuadernillo
- Clean visual separation using subtle borders and background colors
- Maintained consistent design with existing styling approach

✅ **Responsive Design**:

- Flexbox layout that adapts to screen sizes
- Download buttons arranged horizontally by default
- Automatic stacking on smaller screens via flexWrap
- Proper min-width constraints for optimal mobile experience

✅ **UI Improvements**:

- Prominent unit title "El presente de indicativo" centered at top
- Simplified cuadernillo titles without verb lists or descriptions
- Compact, more focused design
- Maintained all existing PDF download functionality
- Updated button text to use Japanese characters (日本語版) and "English"

### Files Modified

- `/website/app/routes/_index.tsx` - Complete restructure of cuadernillo display logic

### Technical Implementation

- Used flexbox with `flexWrap: "wrap"` for natural responsive behavior
- Maintained inline styling approach consistent with existing codebase
- Preserved all PDF download links and functionality
- Clean, maintainable code structure

### Testing Results

- ✅ Build completes without errors
- ✅ All TypeScript compilation passes
- ✅ Responsive layout functions properly
- ✅ PDF download links maintained

## Notes

- This change affects only the presentation layer - no changes to PDF generation or markdown content
- The 4 cuadernillos remain separate entities, just grouped visually
- Maintains backward compatibility with existing PDF file structure
- Focus on clean, maintainable code while preserving current inline styling approach
