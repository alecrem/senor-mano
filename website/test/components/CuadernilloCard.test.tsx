import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import CuadernilloCard from "~/components/CuadernilloCard";

describe("CuadernilloCard", () => {
  const mockProps = {
    number: 1,
    title: "primera conjugación (-AR)",
    verbs: ["dibujar", "buscar", "hablar", "bailar"],
    description: "Aprende los verbos de la primera conjugación"
  };

  it("displays cuadernillo number", () => {
    render(<CuadernilloCard {...mockProps} />);
    expect(screen.getByText("Cuadernillo 1")).toBeInTheDocument();
  });

  it("displays title", () => {
    render(<CuadernilloCard {...mockProps} />);
    expect(screen.getByText("primera conjugación (-AR)")).toBeInTheDocument();
  });

  it("displays list of verbs", () => {
    render(<CuadernilloCard {...mockProps} />);
    expect(screen.getByText("Verbos: dibujar, buscar, hablar, bailar")).toBeInTheDocument();
  });

  it("displays description", () => {
    render(<CuadernilloCard {...mockProps} />);
    expect(screen.getByText("Aprende los verbos de la primera conjugación")).toBeInTheDocument();
  });

  it("includes Japanese download link with correct href", () => {
    render(<CuadernilloCard {...mockProps} />);
    const japaneseLink = screen.getByRole("link", { name: "📖 Descargar en Japonés" });
    expect(japaneseLink).toBeInTheDocument();
    expect(japaneseLink).toHaveAttribute("href", "/pdfs/japanese/cuadernillo-1-ja.pdf");
    expect(japaneseLink).toHaveAttribute("download");
  });

  it("includes English download link with correct href", () => {
    render(<CuadernilloCard {...mockProps} />);
    const englishLink = screen.getByRole("link", { name: "📖 Descargar en Inglés" });
    expect(englishLink).toBeInTheDocument();
    expect(englishLink).toHaveAttribute("href", "/pdfs/english/cuadernillo-1-en.pdf");
    expect(englishLink).toHaveAttribute("download");
  });

  it("handles different cuadernillo numbers correctly", () => {
    render(<CuadernilloCard {...mockProps} number={3} />);
    
    expect(screen.getByText("Cuadernillo 3")).toBeInTheDocument();
    
    const japaneseLink = screen.getByRole("link", { name: "📖 Descargar en Japonés" });
    expect(japaneseLink).toHaveAttribute("href", "/pdfs/japanese/cuadernillo-3-ja.pdf");
    
    const englishLink = screen.getByRole("link", { name: "📖 Descargar en Inglés" });
    expect(englishLink).toHaveAttribute("href", "/pdfs/english/cuadernillo-3-en.pdf");
  });

  it("matches snapshot", () => {
    const { container } = render(<CuadernilloCard {...mockProps} />);
    expect(container).toMatchSnapshot();
  });
});