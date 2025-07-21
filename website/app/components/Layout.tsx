import { Link } from "@remix-run/react";

interface LayoutProps {
  children: React.ReactNode;
}

export default function Layout({ children }: LayoutProps) {
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
              style={{ width: "40px", height: "40px" }}
            />
            <Link
              to="/"
              style={{
                fontSize: "1.25rem",
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
          <p>Señor Mano · Formato DIN A5 optimizado para impresión</p>
          <p style={{ marginTop: "0.5rem", fontSize: "0.875rem" }}>
            Los ejercicios están disponibles con instrucciones en japonés e
            inglés
          </p>
        </div>
      </footer>
    </>
  );
}
