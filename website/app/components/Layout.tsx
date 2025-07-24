/*
 * Copyright (c) 2025 alecrem
 * Licensed under the MIT License. See LICENSE file for details.
 */

import { Link } from "@remix-run/react";

interface LayoutProps {
  copyrightYear: string;
  children: React.ReactNode;
}

export default function Layout({ copyrightYear, children }: LayoutProps) {
  return (
    <>
      <header
        style={{
          backgroundColor: "transparent",
          padding: "1rem 0",
        }}
      >
        <div
          style={{
            maxWidth: "1200px",
            margin: "0 auto",
            padding: "0 1rem",
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
            <img
              src="/logo-200.png"
              alt="Señor Mano Logo"
              style={{ width: "80px", height: "80px" }}
            />
            <Link
              to="/"
              style={{
                fontSize: "2rem",
                fontWeight: "700",
                color: "#1a1a1a",
                textDecoration: "none",
              }}
            >
              Señor Mano
            </Link>
          </div>
        </div>
      </header>

      <main style={{ flex: 1, padding: "2rem 0" }}>
        <div
          style={{
            maxWidth: "1200px",
            margin: "0 auto",
            padding: "0 1rem",
          }}
        >
          {children}
        </div>
      </main>

      <footer
        style={{
          backgroundColor: "#6aad2f",
          borderTop: "1px solid #e5e5e5",
          padding: "2rem 0",
          textAlign: "center" as const,
          color: "#ffffff",
        }}
      >
        <div
          style={{
            maxWidth: "1200px",
            margin: "0 auto",
            padding: "0 1rem",
          }}
        >
          <p style={{ marginTop: "1rem", fontSize: "0.75rem" }}>
            © {copyrightYear} Señor Mano
            {" · "}
            Contenido educativo bajo licencia{" "}
            <a
              href="https://creativecommons.org/licenses/by-sa/4.0/"
              target="_blank"
              rel="noopener noreferrer"
              style={{ color: "#ffffff", textDecoration: "underline" }}
            >
              CC BY-SA 4.0
            </a>
            {" · "}
            <a
              href="https://github.com/alecrem/ejercicios-espanol"
              target="_blank"
              rel="noopener noreferrer"
              style={{ color: "#ffffff", textDecoration: "underline" }}
            >
              Código fuente
            </a>
          </p>
        </div>
      </footer>
    </>
  );
}
