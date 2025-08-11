import React from "react";
import { render, screen } from "@testing-library/react";
import { describe, it, expect, vi, beforeEach } from "vitest";
import type { MetaArgs } from "@remix-run/node";
import Index, { loader, meta } from "~/routes/_index";
import * as RemixReact from "@remix-run/react";

vi.mock("@remix-run/react", () => ({
  useLoaderData: vi.fn(),
  Link: ({ children, to, ...props }: { children: React.ReactNode; to: string; [key: string]: unknown }) => 
    <a href={to} {...props}>{children}</a>,
}));

const IndexWrapper = () => <Index />;

describe("Index Route", () => {
  describe("meta function", () => {
    it("returns correct meta tags", () => {
      const mockMetaArgs: MetaArgs = {
        data: undefined,
        params: {},
        location: { pathname: '/', search: '', hash: '', state: null, key: '' },
        matches: [],
        error: undefined
      };
      
      const result = meta(mockMetaArgs);
      
      expect(result).toEqual([
        { title: "Señor Mano te enseña castellano" },
        {
          name: "description",
          content: "Ejercicios de español para niños que reciben su educación principalmente en japonés o inglés. Cuadernillos organizados por conjugaciones verbales con formato DIN A5 optimizado para impresión.",
        },
      ]);
    });
  });

  describe("loader function", () => {
    it("returns current year for copyright when year matches start year", async () => {
      vi.spyOn(Date.prototype, "getFullYear").mockReturnValue(2025);
      
      const result = await loader();
      
      expect(result).toEqual({
        copyrightYear: "2025",
      });
    });

    it("returns year range for copyright when current year is different", async () => {
      vi.spyOn(Date.prototype, "getFullYear").mockReturnValue(2026);
      
      const result = await loader();
      
      expect(result).toEqual({
        copyrightYear: "2025 - 2026",
      });
    });
  });

  describe("Index Component", () => {
    beforeEach(() => {
      vi.mocked(RemixReact.useLoaderData).mockReturnValue({
        copyrightYear: "2025",
      });
    });

    it("renders main heading", () => {
      render(<IndexWrapper />);
      expect(screen.getByRole("heading", { level: 1, name: "Señor Mano te enseña castellano" })).toBeInTheDocument();
    });

    it("renders introduction text", () => {
      render(<IndexWrapper />);
      expect(screen.getByText(/Estos cuadernillos para practicar español están diseñados específicamente/)).toBeInTheDocument();
    });

    it("renders present tense section", () => {
      render(<IndexWrapper />);
      expect(screen.getByText("El presente de indicativo")).toBeInTheDocument();
    });

    it("renders past tense section", () => {
      render(<IndexWrapper />);
      expect(screen.getByText("El pasado de indicativo")).toBeInTheDocument();
    });

    it("renders all cuadernillos for present tense", () => {
      render(<IndexWrapper />);
      
      expect(screen.getAllByText(/Cuadernillo 1: primera conjugación \(-AR\)/)).toHaveLength(2); // present and past
      expect(screen.getAllByText(/Cuadernillo 2: segunda conjugación \(-ER\)/)).toHaveLength(2);
      expect(screen.getAllByText(/Cuadernillo 3: tercera conjugación \(-IR\)/)).toHaveLength(2);
      expect(screen.getAllByText(/Cuadernillo 4: todos los verbos regulares/)).toHaveLength(2);
    });

    it("renders preview links for each cuadernillo", () => {
      render(<IndexWrapper />);
      
      // Check for some preview links - there should be multiple (2 tenses * 4 cuadernillos * 2 languages each)
      expect(screen.getAllByRole("link", { name: "👁️ Vista previa (JA)" }).length).toBeGreaterThan(0);
      expect(screen.getAllByRole("link", { name: "👁️ Vista previa (EN)" }).length).toBeGreaterThan(0);
    });

    it("renders download links for each cuadernillo", () => {
      render(<IndexWrapper />);
      
      // Check for some download links - there should be multiple
      expect(screen.getAllByRole("link", { name: "📖 Descargar (JA)" }).length).toBeGreaterThan(0);
      expect(screen.getAllByRole("link", { name: "📖 Descargar (EN)" }).length).toBeGreaterThan(0);
    });

    it("renders printing information box", () => {
      render(<IndexWrapper />);
      expect(screen.getByText("📋 Información de impresión")).toBeInTheDocument();
      expect(screen.getByText(/Los PDFs están optimizados para formato DIN A5/)).toBeInTheDocument();
    });

    it("matches snapshot", () => {
      const { container } = render(<IndexWrapper />);
      expect(container).toMatchSnapshot();
    });
  });
});