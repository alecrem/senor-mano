# Plan: Add Cuadernillo Previews to Website

## Overview
Add web-based previews so users can see cuadernillo content before downloading PDFs, using the existing Remix/TypeScript structure.

## Implementation Steps

### 1. Create Preview Route and Components
- Add new route `/preview/[tense]/[cuadernillo]/[language]` in `website/app/routes/`
- Create preview components for each exercise type:
  - `DialoguePreview.tsx` - renders conversations
  - `ConjugationPreview.tsx` - verb tables and fill-in exercises  
  - `ChoicePreview.tsx` - multiple choice questions
  - `TransformationPreview.tsx` - transformation exercises
  - `OrderingPreview.tsx` - word ordering exercises
  - `EvaluationPreview.tsx` - right/wrong exercises

### 2. Content Loading System
- Create utility functions to read and parse markdown files
- Build content loader that can fetch Japanese/English versions from exercise files
- Remove PDF-specific placeholders ([SHORT_LINE], etc.) and replace with web-appropriate elements
- Handle markdown-to-JSX conversion for exercise content

### 3. Update Main Page UI
- Add "👁️ Preview" buttons alongside existing PDF download links
- Maintain consistent styling with current green theme
- Ensure mobile-friendly responsive design

### 4. Preview Page Features
- Display all 6 exercise types in a single scrollable page
- Include navigation back to main page
- Show all exercise content (same as PDF content)
- Add "Download PDF" button for easy access after preview
- Each language (Japanese/English) will be separate pages - no switching needed

### 5. Styling and UX
- Match existing design language and color scheme
- Use existing font setup from current website
- Ensure accessibility (proper heading structure, alt text)
- Add loading states and error handling

## Technical Approach
- Leverage existing Remix SSR capabilities for content loading
- Use styled components or shared style objects for efficient styling
- Build reusable components for different exercise formats
- Static routes for each language version (no client-side switching)

## Benefits
- Users can evaluate content before downloading
- Reduces PDF download traffic for browsers
- Better mobile experience than PDF viewing
- Showcases content quality and variety

## Review

### Implementation Completed
✅ **Preview Route System**: Created dynamic route `/preview/$tense.$cuadernillo.$language` that loads and displays all 6 exercise types from markdown files.

✅ **Preview Components**: Built 6 specialized components to render different exercise types:
- `DialoguePreview`: Renders conversations with proper speaker formatting
- `ConjugationPreview`: Shows verb tables and fill-in exercises with visual blanks
- `ChoicePreview`: Displays multiple choice questions with highlighted options
- `TransformationPreview`: Handles person-change and Q&A exercises with arrows
- `OrderingPreview`: Shows word scrambles with draggable-style word boxes
- `EvaluationPreview`: Presents right/wrong exercises with evaluation boxes

✅ **Content Loading**: Implemented server-side content loading that reads markdown files directly from the exercise source and processes placeholders ([SHORT_LINE], [LONG_LINE]) into web-friendly elements.

✅ **UI Integration**: Updated main page with preview buttons alongside PDF downloads, maintaining consistent design language and responsive layout.

✅ **Styling**: Used shared style objects for consistent appearance, matching the existing green theme and typography choices.

### Technical Details
- **Route Structure**: Uses Remix's file-based routing with dynamic segments
- **Content Processing**: Removes PDF-specific placeholders and converts to interactive elements
- **Error Handling**: Includes proper validation for route parameters and file existence
- **Build Quality**: All TypeScript checks pass, builds successfully without warnings
- **Responsive Design**: Works on mobile and desktop with flexible layouts

### User Experience Improvements
- **Quick Preview**: Users can see complete exercise content without downloading
- **Language Selection**: Separate preview pages for Japanese and English instructions
- **Easy Navigation**: Clear back button and download PDF option from preview
- **Visual Clarity**: Well-formatted exercises with proper spacing and visual hierarchy

The preview system is fully functional and ready for users to explore cuadernillo content before downloading PDFs.