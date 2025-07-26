interface CuadernilloCardProps {
  number: number;
  title: string;
  verbs: string[];
  description: string;
}

export default function CuadernilloCard({ number, title, verbs, description }: CuadernilloCardProps) {
  return (
    <div className="cuadernillo-card">
      <div className="cuadernillo-number">Cuadernillo {number}</div>
      <h3 className="cuadernillo-title">{title}</h3>
      <div className="cuadernillo-verbs">
        Verbos: {verbs.join(", ")}
      </div>
      <p className="cuadernillo-content">
        {description}
      </p>
      <div className="download-buttons">
        <a
          href={`/pdfs/japanese/cuadernillo-${number}-ja.pdf`}
          className="download-btn download-btn-primary"
          download
        >
          📖 Descargar en Japonés
        </a>
        <a
          href={`/pdfs/english/cuadernillo-${number}-en.pdf`}
          className="download-btn download-btn-secondary"
          download
        >
          📖 Descargar en Inglés
        </a>
      </div>
    </div>
  );
}