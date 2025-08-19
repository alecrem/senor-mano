# Fix esbuild CORS Vulnerability - Issue #49

## Problem
Security vulnerability in esbuild (GHSA-67mh-4wv8-2f99) affecting the development server. esbuild versions <= 0.24.2 have permissive CORS settings that allow any website to read development server responses.

## Solution
Update esbuild to version 0.25.0 or later to fix the CORS vulnerability.

## Todo Items
- [ ] Check current esbuild version in website package
- [ ] Update esbuild to version 0.25.0 or later  
- [ ] Test website development server functionality
- [ ] Run website build and tests to verify no regressions

## Impact
This is a development-only security issue that affects the website development server. No production systems are impacted.

## Testing
- Verify website development server starts correctly
- Ensure build process works without errors
- Run all website tests to confirm no regressions

## Review

### Changes Made
1. **Updated main dependencies**: Updated `@remix-run/dev`, `@remix-run/node`, `@remix-run/react`, `@remix-run/serve` to version 2.17.0
2. **Updated build tools**: Updated `vite` to 6.3.5, `@vitejs/plugin-react` to 5.0.1  
3. **Added dependency override**: Added `pnpm.overrides` to force all esbuild versions to ^0.25.0
4. **Verified security fix**: All esbuild dependencies now use version 0.25.9 (above the vulnerable 0.24.2 threshold)

### Security Impact
- **Fixed vulnerability**: GHSA-67mh-4wv8-2f99 resolved by updating esbuild from vulnerable versions (0.17.6, 0.21.5) to secure version 0.25.9
- **CORS protection**: Development server now has proper CORS settings, preventing malicious websites from reading dev server responses
- **No production impact**: This was a development-only vulnerability

### Testing Results
- ✅ Development server starts successfully on http://localhost:5173/
- ✅ All 36 unit tests pass
- ✅ TypeScript compilation succeeds
- ✅ Linting passes with no errors
- ✅ Production build completes successfully

The esbuild CORS vulnerability has been completely resolved with no regressions to website functionality.