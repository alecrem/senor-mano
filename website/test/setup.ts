import "@testing-library/jest-dom";

// Mock Remix's useLoaderData hook for tests
import { vi } from "vitest";

vi.mock("@remix-run/react", async () => {
  const actual = await vi.importActual("@remix-run/react");
  return {
    ...actual,
    useLoaderData: vi.fn(),
  };
});