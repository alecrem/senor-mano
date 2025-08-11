import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import DialoguePreview from "~/components/DialoguePreview";

describe("DialoguePreview", () => {
  const mockContent = `# Un día en casa

## Conversación entre Ana y Carlos

**Ana:** ¡Hola Carlos! ¿Cómo **estás** hoy?

**Carlos:** ¡Hola Ana! Estoy **muy bien**, gracias. ¿Y tú?

**Ana:** Yo también estoy bien. ¿Qué planes **tienes** para hoy?

**Carlos:** Voy a **estudiar** español. ¿Te gustaría estudiar conmigo?`;

  it("displays title from markdown header", () => {
    render(<DialoguePreview content={mockContent} />);
    expect(screen.getByRole("heading", { level: 2, name: "Un día en casa" })).toBeInTheDocument();
  });

  it("displays subtitle from markdown subheader", () => {
    render(<DialoguePreview content={mockContent} />);
    expect(screen.getByRole("heading", { level: 3, name: "Conversación entre Ana y Carlos" })).toBeInTheDocument();
  });

  it("parses and displays dialogue lines with speakers", () => {
    render(<DialoguePreview content={mockContent} />);
    
    expect(screen.getAllByText("Ana:")).toHaveLength(2);
    expect(screen.getAllByText("Carlos:")).toHaveLength(2);
    expect(screen.getByText(/¡Hola Carlos! ¿Cómo/)).toBeInTheDocument();
    expect(screen.getByText(/Voy a/)).toBeInTheDocument();
  });

  it("renders bold text correctly", () => {
    render(<DialoguePreview content={mockContent} />);
    
    expect(screen.getByText("estás")).toBeInTheDocument();
    expect(screen.getByText("muy bien")).toBeInTheDocument();
    expect(screen.getByText("tienes")).toBeInTheDocument();
    expect(screen.getByText("estudiar")).toBeInTheDocument();
  });

  it("handles content without subtitle", () => {
    const contentNoSubtitle = `# Solo título

**Ana:** Hola mundo.

**Carlos:** ¡Hola!`;

    render(<DialoguePreview content={contentNoSubtitle} />);
    
    expect(screen.getByRole("heading", { level: 2, name: "Solo título" })).toBeInTheDocument();
    expect(screen.queryByRole("heading", { level: 3 })).not.toBeInTheDocument();
  });

  it("handles empty content gracefully", () => {
    render(<DialoguePreview content="" />);
    
    // Should render without crashing - component will render an empty title
    const container = document.body;
    expect(container).toBeInTheDocument();
  });

  it("matches snapshot", () => {
    const { container } = render(<DialoguePreview content={mockContent} />);
    expect(container).toMatchSnapshot();
  });

  it("filters out empty lines", () => {
    const contentWithEmptyLines = `# Test Title


**Ana:** First line.



**Carlos:** Second line.


`;

    render(<DialoguePreview content={contentWithEmptyLines} />);
    
    // Should only show the two dialogue lines
    expect(screen.getAllByText("Ana:")).toHaveLength(1);
    expect(screen.getAllByText("Carlos:")).toHaveLength(1);
    expect(screen.getByText("First line.")).toBeInTheDocument();
    expect(screen.getByText("Second line.")).toBeInTheDocument();
  });
});