# Project Plan: Website Branding (Issue #11)

## Overview
Update the website with proper branding to establish a cohesive visual identity for "Señor Mano".

## Completed Tasks

### ✅ Favicon and Logo Implementation
- [x] Created favicon.ico from logo artwork (multi-size: 16x16, 32x32, 48x48)
- [x] Generated logo-200.png (200x200px version)
- [x] Added logo to header navigation (40x40px display size)
- [x] Proper alt text and accessibility

### ✅ Rebranding Implementation
- [x] Updated header title: "Cuadernillos de español" → "Señor Mano"
- [x] Updated page title and main heading: "Cuadernillos de español para niños" → "Señor Mano te enseña castellano"
- [x] Updated footer text: "Cuadernillos de español para niños" → "Señor Mano te enseña castellano"
- [x] Updated meta descriptions in root.tsx and _index.tsx
- [x] All brand references consistently updated

### ✅ Color Scheme Implementation
- [x] Primary buttons: Custom green (#6AAD2F) with darker hover (#5A9426)
- [x] Info box: Warm orange-yellow theme (#FDF2E0 background, #F5BF66 border, #B8842B text)
- [x] Footer: Green background (#6AAD2F) with white text
- [x] Body background: Light blue (#AADFEB) 
- [x] Section backgrounds: Light blue (#F0F8FF)
- [x] Section headers: Dark green (#5A9426)

### ✅ UX Improvements
- [x] Added consistent padding to hero and instructions sections (2rem horizontal)
- [x] Improved mobile responsiveness for card-like containers

## Current Status
All primary requirements completed. Branch `feature/issue-11/website-branding` ready for commit.

## Header Background Color Options

### Current Implementation
- Header background: Bright orange (#FFCC7B)
- Original concern: Warning color background (info box) too close to white hero section created visual collision
- Current solution: Bright orange header provides separation and looks good
- Opportunity: Explore alternative header background options while maintaining visual separation

### Alternative Options

#### Option 1: Transparent/Minimal Header
```css
backgroundColor: "transparent" // or match body background
borderBottom: "2px solid #6AAD2F" // stronger green border instead
```

#### Option 2: Subtle Light Blue Header
```css
backgroundColor: "#E8F4F8" // lighter version of body blue
```

#### Option 3: Very Light Green
```css
backgroundColor: "#F0F9F4" // very light version of primary green
```

#### Option 4: Hero Section Adjustment
Keep orange header but change hero:
```css
// Hero section
backgroundColor: "#FAFCFF" // very light blue instead of white
border: "1px solid #E8F4F8" // subtle border
```

#### Option 5: Increased Separation
Keep both colors but add more visual breathing room:
```css
// Header
padding: "1.5rem 0" // more padding
borderBottom: "3px solid rgba(106, 173, 47, 0.2)" // subtle green accent

// Hero section  
marginTop: "2rem" // more space from header
```

## Recommendations
- **Primary recommendation:** Option 1 (transparent header with green border) or Option 3 (light green header)
- Both maintain brand cohesion while eliminating orange-white visual clash
- Preserve the warm, welcoming feel while improving visual hierarchy

## Next Steps
1. Choose header background approach
2. Implement selected option if needed
3. Commit changes to feature branch
4. Create pull request
5. Link PR to issue #11