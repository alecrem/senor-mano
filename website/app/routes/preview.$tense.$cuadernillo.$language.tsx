import type { LoaderFunctionArgs, MetaFunction } from "@remix-run/node";
import { json } from "@remix-run/node";
import { useLoaderData, Link } from "@remix-run/react";
import { readFileSync } from "fs";
import { join } from "path";
import Layout from "~/components/Layout";
import DialoguePreview from "~/components/DialoguePreview";
import ConjugationPreview from "~/components/ConjugationPreview";
import ChoicePreview from "~/components/ChoicePreview";
import TransformationPreview from "~/components/TransformationPreview";
import OrderingPreview from "~/components/OrderingPreview";
import EvaluationPreview from "~/components/EvaluationPreview";

export const meta: MetaFunction<typeof loader> = ({ data }) => {
  if (!data) {
    return [{ title: "Preview not found" }];
  }

  const { tense, cuadernillo, language } = data;
  const tenseTitle = tense === "present-tense" ? "Presente" : "Pasado";
  const languageTitle = language === "japanese" ? "Japonés" : "Inglés";
  
  return [
    { 
      title: `Vista previa - Cuadernillo ${cuadernillo} ${tenseTitle} (${languageTitle}) - Señor Mano` 
    },
    {
      name: "description",
      content: `Vista previa del Cuadernillo ${cuadernillo} de ${tenseTitle} en ${languageTitle} con todos los ejercicios de español.`,
    },
  ];
};

interface CuadernilloContent {
  dialogue: string;
  conjugation: string;
  choice: string;
  transformation: string;
  ordering: string;
  evaluation: string;
}

export async function loader({ params }: LoaderFunctionArgs) {
  const { tense, cuadernillo, language } = params;

  if (!tense || !cuadernillo || !language) {
    throw new Response("Missing parameters", { status: 400 });
  }

  if (!["present-tense", "past-tense"].includes(tense)) {
    throw new Response("Invalid tense", { status: 400 });
  }

  if (!["1", "2", "3", "4"].includes(cuadernillo)) {
    throw new Response("Invalid cuadernillo", { status: 400 });
  }

  if (!["japanese", "english"].includes(language)) {
    throw new Response("Invalid language", { status: 400 });
  }

  const basePath = join(process.cwd(), "app", "data", "markdown", tense);
  const cuadernilloMap: Record<string, string> = {
    "1": "cuadernillo-1-ar-verbs",
    "2": "cuadernillo-2-er-verbs", 
    "3": "cuadernillo-3-ir-verbs",
    "4": "cuadernillo-4-mixed-verbs"
  };

  const cuadernilloDir = cuadernilloMap[cuadernillo];
  const contentDir = join(basePath, cuadernilloDir, language);

  try {
    const content: CuadernilloContent = {
      dialogue: readFileSync(join(contentDir, "pagina-1-dialogo.md"), "utf-8"),
      conjugation: readFileSync(join(contentDir, "pagina-2-conjugacion-completar.md"), "utf-8"),
      choice: readFileSync(join(contentDir, "pagina-3-eleccion.md"), "utf-8"),
      transformation: readFileSync(join(contentDir, "pagina-4-transformacion.md"), "utf-8"),
      ordering: readFileSync(join(contentDir, "pagina-5-ordenar.md"), "utf-8"),
      evaluation: readFileSync(join(contentDir, "pagina-6-bien-mal.md"), "utf-8"),
    };

    const startYear = 2025;
    const currentYear = new Date().getFullYear();
    const copyrightYear =
      currentYear === startYear
        ? `${startYear}`
        : `${startYear} - ${currentYear}`;

    return json({ 
      content, 
      tense, 
      cuadernillo, 
      language, 
      copyrightYear,
      cuadernilloDir 
    });
  } catch (error) {
    throw new Response("Content not found", { status: 404 });
  }
}

const styles = {
  container: {
    maxWidth: "800px",
    margin: "0 auto",
    padding: "2rem 1rem",
  },
  header: {
    textAlign: "center" as const,
    marginBottom: "2rem",
    padding: "2rem",
    backgroundColor: "#fff",
    borderRadius: "12px",
    boxShadow: "0 1px 3px rgba(0, 0, 0, 0.1)",
  },
  title: {
    fontSize: "2rem",
    fontWeight: "700",
    marginBottom: "1rem",
    color: "#1a1a1a",
    fontFamily: "'Delius', system-ui, sans-serif",
  },
  subtitle: {
    fontSize: "1.25rem",
    color: "#6b7280",
    marginBottom: "1rem",
  },
  actions: {
    display: "flex",
    gap: "1rem",
    justifyContent: "center",
    flexWrap: "wrap" as const,
  },
  button: {
    padding: "0.75rem 1.5rem",
    borderRadius: "8px",
    textDecoration: "none",
    fontWeight: "600",
    transition: "all 0.2s ease",
  },
  primaryButton: {
    backgroundColor: "#6AAD2F",
    color: "#fff",
  },
  secondaryButton: {
    backgroundColor: "#f3f4f6",
    color: "#374151",
    border: "1px solid #d1d5db",
  },
  section: {
    backgroundColor: "#fff",
    borderRadius: "12px",
    padding: "2rem",
    marginBottom: "2rem",
    boxShadow: "0 1px 3px rgba(0, 0, 0, 0.1)",
  },
};

export default function PreviewPage() {
  const { content, tense, cuadernillo, language, copyrightYear, cuadernilloDir } = useLoaderData<typeof loader>();

  const tenseTitle = tense === "present-tense" ? "Presente de indicativo" : "Pasado de indicativo";
  const languageTitle = language === "japanese" ? "Japonés" : "Inglés";
  const pdfUrl = `/pdfs/${language}/cuadernillo-${cuadernillo}-${tense}-${language === "japanese" ? "ja" : "en"}.pdf`;

  const conjugationTitles: Record<string, string> = {
    "1": "primera conjugación (-AR)",
    "2": "segunda conjugación (-ER)", 
    "3": "tercera conjugación (-IR)",
    "4": "todos los verbos regulares"
  };

  return (
    <Layout copyrightYear={copyrightYear}>
      <div style={styles.container}>
        <div style={styles.header}>
          <h1 style={styles.title}>
            Cuadernillo {cuadernillo}: {conjugationTitles[cuadernillo]}
          </h1>
          <p style={styles.subtitle}>
            {tenseTitle} - Instrucciones en {languageTitle}
          </p>
          <div style={styles.actions}>
            <a
              href={pdfUrl}
              download
              style={{
                ...styles.button,
                ...styles.primaryButton,
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.backgroundColor = "#5A9426";
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.backgroundColor = "#6AAD2F";
              }}
            >
              📄 Descargar PDF
            </a>
            <Link
              to="/"
              style={{
                ...styles.button,
                ...styles.secondaryButton,
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.backgroundColor = "#e5e7eb";
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.backgroundColor = "#f3f4f6";
              }}
            >
              ← Volver al inicio
            </Link>
          </div>
        </div>

        <div style={styles.section}>
          <DialoguePreview content={content.dialogue} />
        </div>

        <div style={styles.section}>
          <ConjugationPreview content={content.conjugation} />
        </div>

        <div style={styles.section}>
          <ChoicePreview content={content.choice} />
        </div>

        <div style={styles.section}>
          <TransformationPreview content={content.transformation} />
        </div>

        <div style={styles.section}>
          <OrderingPreview content={content.ordering} />
        </div>

        <div style={styles.section}>
          <EvaluationPreview content={content.evaluation} />
        </div>
      </div>
    </Layout>
  );
}