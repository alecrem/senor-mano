import React from "react";
import { render, screen } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import Layout from "~/components/Layout";

// Mock @remix-run/react
vi.mock("@remix-run/react", () => ({
  Link: ({ children, to, ...props }: { children: React.ReactNode; to: string; [key: string]: unknown }) => 
    <a href={to} {...props}>{children}</a>,
}));

const LayoutWrapper = ({ children, copyrightYear }: { children: React.ReactNode; copyrightYear: string }) => (
  <Layout copyrightYear={copyrightYear}>
    {children}
  </Layout>
);

describe("Layout", () => {
  it("renders header with logo and title", () => {
    render(
      <LayoutWrapper copyrightYear="2025">
        <div>Test content</div>
      </LayoutWrapper>
    );

    expect(screen.getByAltText("Señor Mano Logo")).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Señor Mano" })).toBeInTheDocument();
  });

  it("renders children content", () => {
    render(
      <LayoutWrapper copyrightYear="2025">
        <div>Test content</div>
      </LayoutWrapper>
    );

    expect(screen.getByText("Test content")).toBeInTheDocument();
  });

  it("displays copyright year in footer", () => {
    render(
      <LayoutWrapper copyrightYear="2025">
        <div>Test content</div>
      </LayoutWrapper>
    );

    expect(screen.getByText(/© 2025 Señor Mano/)).toBeInTheDocument();
  });

  it("displays copyright year range in footer", () => {
    render(
      <LayoutWrapper copyrightYear="2025 - 2026">
        <div>Test content</div>
      </LayoutWrapper>
    );

    expect(screen.getByText(/© 2025 - 2026 Señor Mano/)).toBeInTheDocument();
  });

  it("includes CC BY-SA 4.0 license link", () => {
    render(
      <LayoutWrapper copyrightYear="2025">
        <div>Test content</div>
      </LayoutWrapper>
    );

    const licenseLink = screen.getByRole("link", { name: "CC BY-SA 4.0" });
    expect(licenseLink).toBeInTheDocument();
    expect(licenseLink).toHaveAttribute("href", "https://creativecommons.org/licenses/by-sa/4.0/");
    expect(licenseLink).toHaveAttribute("target", "_blank");
  });

  it("includes source code link", () => {
    render(
      <LayoutWrapper copyrightYear="2025">
        <div>Test content</div>
      </LayoutWrapper>
    );

    const sourceLink = screen.getByRole("link", { name: "Código fuente" });
    expect(sourceLink).toBeInTheDocument();
    expect(sourceLink).toHaveAttribute("href", "https://github.com/alecrem/ejercicios-espanol");
    expect(sourceLink).toHaveAttribute("target", "_blank");
  });

  it("matches snapshot", () => {
    const { container } = render(
      <LayoutWrapper copyrightYear="2025">
        <div>Test content</div>
      </LayoutWrapper>
    );

    expect(container).toMatchSnapshot();
  });
});