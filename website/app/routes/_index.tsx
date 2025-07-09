import type { MetaFunction } from "@remix-run/node";
import Layout from "~/components/Layout";

export const meta: MetaFunction = () => {
  return [
    { title: "Cuadernillos de español para niños" },
    { 
      name: "description", 
      content: "Ejercicios de español para niños que reciben su educación principalmente en japonés o inglés. Cuadernillos organizados por conjugaciones verbales con formato DIN A5 optimizado para impresión." 
    },
  ];
};

const units = [
  {
    number: 1,
    title: "primera conjugación (-AR)",
    verbs: ["dibujar", "buscar", "hablar", "bailar"],
    description: "Aprende los verbos de primera conjugación con ejercicios de diálogo, conjugación, elección múltiple, transformaciones, ordenamiento de palabras y corrección de errores."
  },
  {
    number: 2,
    title: "segunda conjugación (-ER)",
    verbs: ["comer", "leer", "aprender", "beber"],
    description: "Practica los verbos de segunda conjugación a través de actividades variadas que refuerzan el aprendizaje de estas formas verbales esenciales."
  },
  {
    number: 3,
    title: "tercera conjugación (-IR)",
    verbs: ["vivir", "escribir", "abrir", "subir"],
    description: "Domina los verbos de tercera conjugación con ejercicios estructurados que consolidan el conocimiento de estas importantes formas verbales."
  }
];

export default function Index() {
  return (
    <Layout>
      <section style={{
        textAlign: 'center' as const,
        padding: '4rem 0',
        backgroundColor: '#fff',
        borderRadius: '12px',
        marginBottom: '3rem'
      }}>
        <h1 style={{
          fontSize: '3rem',
          fontWeight: '800',
          marginBottom: '1rem',
          color: '#1a1a1a'
        }}>
          Cuadernillos de español para niños
        </h1>
        <p style={{
          fontSize: '1.25rem',
          color: '#6b7280',
          marginBottom: '2rem'
        }}>
          Ejercicios de conjugación verbal organizados por unidades
        </p>
        <div style={{
          maxWidth: '800px',
          margin: '0 auto',
          textAlign: 'left' as const
        }}>
          <p>
            Estos cuadernillos están diseñados específicamente para niños de 7-16 años que reciben 
            su educación principalmente en japonés o inglés, pero que necesitan reforzar sus 
            conocimientos formales de español. Los niños ya tienen buena comprensión auditiva y 
            uso natural de la gramática española, pero necesitan estructura formal en lectura y escritura.
          </p>
          <p style={{ marginTop: "1rem" }}>
            Cada cuadernillo contiene 6 páginas de ejercicios: diálogo contextualizado, conjugación 
            y completado, ejercicios de elección múltiple, transformaciones, ordenamiento de palabras 
            y corrección de errores. Formato DIN A5 con texto grande y espaciado amplio, optimizado 
            para niños.
          </p>
        </div>
      </section>

      <section>
        <h2 style={{ 
          fontSize: "2rem", 
          fontWeight: "700", 
          textAlign: "center", 
          marginBottom: "2rem",
          color: "#1a1a1a"
        }}>
          Descargar cuadernillos
        </h2>
        
        <div style={{ 
          display: "grid", 
          gap: "2rem"
        }}>
          {units.map((unit) => (
            <div key={unit.number} style={{
              background: "#fff",
              borderRadius: "12px",
              padding: "2rem",
              boxShadow: "0 1px 3px rgba(0, 0, 0, 0.1)",
              border: "1px solid #e5e5e5"
            }}>
              <div style={{ 
                display: "flex", 
                justifyContent: "space-between", 
                alignItems: "flex-start",
                flexWrap: "wrap",
                gap: "1rem"
              }}>
                <div style={{ flex: "1", minWidth: "250px" }}>
                  <h3 style={{ 
                    fontSize: "1.5rem", 
                    fontWeight: "700", 
                    marginBottom: "0.5rem" 
                  }}>
                    Unidad {unit.number}: {unit.title}
                  </h3>
                  <p style={{ 
                    color: "#6b7280", 
                    marginBottom: "1rem" 
                  }}>
                    Verbos: {unit.verbs.join(", ")}
                  </p>
                  <p style={{ 
                    color: "#4b5563", 
                    fontSize: "0.95rem",
                    lineHeight: "1.6"
                  }}>
                    {unit.description}
                  </p>
                </div>
                
                <div style={{ 
                  display: "flex", 
                  flexDirection: "column",
                  gap: "0.75rem",
                  minWidth: "200px"
                }}>
                  <a
                    href={`/pdfs/japanese/unidad-${unit.number}-ja.pdf`}
                    download
                    style={{ 
                      textAlign: "center" as const,
                      display: 'block',
                      padding: '0.75rem 1.5rem',
                      backgroundColor: '#3b82f6',
                      color: '#fff',
                      textDecoration: 'none',
                      borderRadius: '8px',
                      fontWeight: '600',
                      fontSize: '0.875rem',
                      transition: 'all 0.2s ease'
                    }}
                    onMouseOver={(e) => {
                      e.currentTarget.style.backgroundColor = '#2563eb';
                    }}
                    onMouseOut={(e) => {
                      e.currentTarget.style.backgroundColor = '#3b82f6';
                    }}
                  >
                    📖 Versión en japonés (PDF)
                  </a>
                  <a
                    href={`/pdfs/english/unidad-${unit.number}-en.pdf`}
                    download
                    style={{ 
                      textAlign: "center" as const,
                      display: 'block',
                      padding: '0.75rem 1.5rem',
                      backgroundColor: '#3b82f6',
                      color: '#fff',
                      textDecoration: 'none',
                      borderRadius: '8px',
                      fontWeight: '600',
                      fontSize: '0.875rem',
                      transition: 'all 0.2s ease'
                    }}
                    onMouseOver={(e) => {
                      e.currentTarget.style.backgroundColor = '#2563eb';
                    }}
                    onMouseOut={(e) => {
                      e.currentTarget.style.backgroundColor = '#3b82f6';
                    }}
                  >
                    📖 Versión en inglés (PDF)
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
        
        <div style={{ 
          background: "#fef3c7", 
          border: "1px solid #f59e0b", 
          borderRadius: "8px", 
          padding: "1rem",
          marginTop: "2rem"
        }}>
          <h3 style={{ 
            color: "#92400e", 
            fontWeight: "600", 
            marginBottom: "0.5rem" 
          }}>
            📋 Información de impresión
          </h3>
          <p style={{ color: "#92400e", fontSize: "0.9rem" }}>
            Los PDFs están optimizados para formato DIN A5 (148 × 210 mm). 
            Para imprimir en papel A4 estándar, selecciona la opción "2 páginas por hoja" 
            en tu impresora para obtener el tamaño de texto correcto para niños.
          </p>
        </div>
      </section>

      <section style={{ 
        textAlign: "center", 
        padding: "3rem 0", 
        background: "#f9fafb", 
        borderRadius: "12px",
        marginTop: "2rem"
      }}>
        <h3 style={{ 
          fontSize: "1.5rem", 
          fontWeight: "700", 
          marginBottom: "1rem",
          color: "#1a1a1a"
        }}>
          ¿Cómo usar estos cuadernillos?
        </h3>
        <div style={{ 
          maxWidth: "800px", 
          margin: "0 auto", 
          textAlign: "left",
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
          gap: "2rem",
          marginTop: "2rem"
        }}>
          <div>
            <h4 style={{ fontWeight: "600", marginBottom: "0.5rem", color: "#2563eb" }}>
              1. Selecciona el idioma
            </h4>
            <p style={{ color: "#4b5563", fontSize: "0.95rem" }}>
              Elige entre instrucciones en japonés o inglés según el idioma de educación del niño.
            </p>
          </div>
          <div>
            <h4 style={{ fontWeight: "600", marginBottom: "0.5rem", color: "#2563eb" }}>
              2. Descarga e imprime
            </h4>
            <p style={{ color: "#4b5563", fontSize: "0.95rem" }}>
              Imprime en formato DIN A5 para obtener el tamaño de texto optimizado.
            </p>
          </div>
          <div>
            <h4 style={{ fontWeight: "600", marginBottom: "0.5rem", color: "#2563eb" }}>
              3. Practica y aprende
            </h4>
            <p style={{ color: "#4b5563", fontSize: "0.95rem" }}>
              Completa los 6 tipos de ejercicios para reforzar cada conjugación verbal.
            </p>
          </div>
        </div>
      </section>
    </Layout>
  );
}