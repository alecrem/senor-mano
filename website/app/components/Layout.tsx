import { Link } from "@remix-run/react";

interface LayoutProps {
  children: React.ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  return (
    <>
      <header className="header">
        <div className="container">
          <div className="header-content">
            <Link to="/" className="logo">
              Cuadernillos de español
            </Link>
          </div>
        </div>
      </header>

      <main className="main">
        <div className="container">
          {children}
        </div>
      </main>

      <footer className="footer">
        <div className="container">
          <p>
            Cuadernillos de español para niños · Formato DIN A5 optimizado para impresión
          </p>
          <p style={{ marginTop: "0.5rem", fontSize: "0.875rem" }}>
            Los ejercicios están disponibles con instrucciones en japonés e inglés
          </p>
        </div>
      </footer>
    </>
  );
}