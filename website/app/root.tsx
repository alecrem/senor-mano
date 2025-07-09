import type { LinksFunction } from "@remix-run/node";
import {
  Links,
  LiveReload,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";

export const links: LinksFunction = () => [
  { rel: "preconnect", href: "https://fonts.googleapis.com" },
  {
    rel: "preconnect",
    href: "https://fonts.gstatic.com",
    crossOrigin: "anonymous",
  },
  {
    rel: "stylesheet",
    href: "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap",
  },
];

export default function App() {
  return (
    <html lang="es">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta
          name="description"
          content="Cuadernillos de español para niños que reciben su educación principalmente en japonés o inglés. Ejercicios de conjugación verbal organizados por unidades."
        />
        <Meta />
        <Links />
      </head>
      <body style={{
        margin: 0,
        padding: 0,
        boxSizing: 'border-box',
        lineHeight: 1.6,
        WebkitFontSmoothing: 'antialiased',
        fontFamily: "'Inter', system-ui, sans-serif",
        backgroundColor: '#fafafa',
        color: '#1a1a1a'
      }}>
        <div style={{ minHeight: '100vh' }}>
          <Outlet />
        </div>
        <ScrollRestoration />
        <Scripts />
        <LiveReload />
      </body>
    </html>
  );
}
