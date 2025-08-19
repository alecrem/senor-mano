# Project Plan: Add Dependabot Configuration for Website Package Updates

## Problem
The website (`website/package.json`) has multiple dependencies that need to be kept up to date automatically. Currently, there's no automated system for creating PRs when package updates are available.

## Solution
Create a Dependabot configuration file that monitors the website directory and creates PRs for package updates with daily frequency.

## Todo Items
- [ ] Create feature branch for issue 45
- [ ] Create .github/dependabot.yml configuration file  
- [ ] Configure daily update frequency for website dependencies
- [ ] Set up dependency grouping rules for related packages
- [ ] Test the configuration and commit changes

## Implementation Details
- Target only `website/package.json` to avoid noise from other files
- Use daily schedule as requested by user (instead of weekly)
- Group related dependencies (e.g., Remix packages, testing libraries)
- Follow project commit message conventions
- Ensure PR titles are clear and descriptive

## Dependencies Analysis
From website/package.json:
- Runtime: Remix (@remix-run/*), React, fonts (@fontsource/*)
- Dev tools: TypeScript, ESLint, Vitest, testing libraries
- Build tools: Vite, various plugins

## Expected Outcome
Dependabot will automatically create PRs daily for package updates, grouped logically to reduce PR volume while keeping dependencies current.

## Review

### Implementation Summary
✅ Successfully implemented Dependabot configuration for the website dependencies with the following features:

1. **Daily Schedule**: Changed from weekly to daily as requested by user
2. **Targeted Monitoring**: Only monitors `website/package.json` to avoid noise from other files
3. **Dependency Grouping**: Organized into logical groups:
   - `remix`: All @remix-run/* packages
   - `react`: React core and related packages
   - `fonts`: @fontsource/* packages  
   - `testing`: Testing libraries (Vitest, Testing Library, jsdom)
   - `typescript-eslint`: TypeScript and ESLint related packages
   - `build-tools`: Vite, TypeScript, and build tooling
4. **Commit Message Format**: Uses `chore(deps)` prefix with scope inclusion
5. **Rate Limiting**: Set to maximum 10 concurrent PRs to avoid overwhelming

### Configuration Details
- **File Location**: `.github/dependabot.yml`
- **Package Ecosystem**: npm
- **Directory**: `/website`  
- **Schedule**: daily at 05:00 UTC
- **Commit Format**: Follows conventional commit style

### Next Steps
After merging this PR, Dependabot will start monitoring the website dependencies and automatically create PRs for updates. The grouping will help reduce PR volume by bundling related packages together.

### Files Changed
- Created `.github/dependabot.yml` - Main Dependabot configuration file