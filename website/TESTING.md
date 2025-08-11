# Testing Guidelines

This document provides guidelines for testing in the Ejercicios Español website.

## Test Setup

We use **Vitest** as our testing framework with the following stack:
- **Vitest**: Test runner and framework
- **@testing-library/react**: Component testing utilities
- **@testing-library/jest-dom**: Additional DOM matchers
- **jsdom**: DOM environment for tests

## Running Tests

```bash
# Run tests once
pnpm test

# Run tests in watch mode during development  
pnpm test --watch

# Run tests with coverage
pnpm test:coverage

# Run tests with UI
pnpm test:ui
```

## Test Structure

Tests are located in the `test/` directory with the following structure:
```
test/
├── components/
│   ├── Layout.test.tsx
│   ├── CuadernilloCard.test.tsx
│   └── DialoguePreview.test.tsx
├── routes/
│   ├── _index.test.tsx
│   └── preview.test.tsx
└── setup.ts
```

## Writing Tests

### Component Tests

For React components, follow this pattern:

```tsx
import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import ComponentName from "~/components/ComponentName";

describe("ComponentName", () => {
  it("renders correctly with props", () => {
    render(<ComponentName prop="value" />);
    expect(screen.getByText("expected text")).toBeInTheDocument();
  });

  it("matches snapshot", () => {
    const { container } = render(<ComponentName prop="value" />);
    expect(container).toMatchSnapshot();
  });
});
```

### Route Tests

For Remix routes, mock the necessary hooks:

```tsx
import { render, screen } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import Route, { loader, meta } from "~/routes/route-name";

vi.mock("@remix-run/react", () => ({
  useLoaderData: vi.fn(),
  Link: ({ children, to, ...props }: any) => <a href={to} {...props}>{children}</a>,
}));

describe("Route", () => {
  it("renders with mocked data", () => {
    vi.mocked(useLoaderData).mockReturnValue({ data: "test" });
    render(<Route />);
    expect(screen.getByText("test")).toBeInTheDocument();
  });
});
```

## Best Practices

### 1. Test Behavior, Not Implementation

Focus on testing what the component does, not how it does it:

```tsx
// ✅ Good - tests behavior
expect(screen.getByRole("button", { name: "Download" })).toBeInTheDocument();

// ❌ Bad - tests implementation details
expect(container.querySelector('.download-btn')).toBeInTheDocument();
```

### 2. Use Semantic Queries

Prefer queries that match how users interact with elements:

```tsx
// ✅ Good - semantic queries
screen.getByRole("heading", { name: "Page Title" })
screen.getByLabelText("Email address")
screen.getByText("Submit")

// ❌ Bad - implementation-focused queries
screen.getByClassName("title")
screen.getById("email-input")
```

### 3. Handle Async Operations

For async operations, use `findBy` queries:

```tsx
// ✅ Good - waits for async content
expect(await screen.findByText("Loading complete")).toBeInTheDocument();

// ❌ Bad - might fail with async content
expect(screen.getByText("Loading complete")).toBeInTheDocument();
```

### 4. Test Multiple Scenarios

Include edge cases and error states:

```tsx
describe("ComponentName", () => {
  it("renders with valid data", () => { /* ... */ });
  it("handles empty data gracefully", () => { /* ... */ });
  it("displays error state when needed", () => { /* ... */ });
});
```

### 5. Use Regex for Flexible Text Matching

When text is split across elements, use regex:

```tsx
// ✅ Good - handles text split by elements
expect(screen.getByText(/© 2025 Señor Mano/)).toBeInTheDocument();

// ❌ Bad - fails if text is split
expect(screen.getByText("© 2025 Señor Mano")).toBeInTheDocument();
```

## Snapshot Testing

Snapshot tests capture the rendered output and detect unexpected changes:

```tsx
it("matches snapshot", () => {
  const { container } = render(<Component />);
  expect(container).toMatchSnapshot();
});
```

### Updating Snapshots

When intentional changes are made:
```bash
pnpm test -- -u
```

## Coverage Guidelines

- **Aim for 80%+ coverage** on components and routes
- **Focus on critical paths** rather than 100% coverage
- **Exclude configuration files** and test utilities from coverage

Current coverage exclusions:
- `node_modules/`
- `test/`
- `build/`
- `public/`
- `*.config.*`

## Mocking

### Remix Hooks

Mock Remix hooks consistently:

```tsx
vi.mock("@remix-run/react", () => ({
  useLoaderData: vi.fn(),
  Link: ({ children, to, ...props }: any) => <a href={to} {...props}>{children}</a>,
}));
```

### External Dependencies

Mock external libraries when needed:

```tsx
vi.mock("external-library", () => ({
  someFunction: vi.fn(() => "mocked result"),
}));
```

## Continuous Integration

Tests run automatically on:
- Push to `main` branch
- Pull requests to `main`
- Changes to website files

The CI pipeline:
1. Installs dependencies
2. Runs type checking
3. Runs linting
4. Runs tests
5. Generates coverage report
6. Builds the project

## Debugging Tests

### VS Code Integration

Add to `.vscode/launch.json` for debugging:

```json
{
  "type": "node",
  "request": "launch",
  "name": "Debug Tests",
  "program": "${workspaceFolder}/website/node_modules/.bin/vitest",
  "args": ["--run", "--inspect-brk"],
  "cwd": "${workspaceFolder}/website"
}
```

### Common Issues

1. **Text not found**: Text might be split across elements - use regex
2. **Multiple elements**: Use `getAllBy*` or be more specific with queries
3. **Async content**: Use `findBy*` queries instead of `getBy*`
4. **Mock not working**: Ensure mocks are defined before imports

## Resources

- [Vitest Documentation](https://vitest.dev/)
- [Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)
- [Jest DOM Matchers](https://github.com/testing-library/jest-dom)