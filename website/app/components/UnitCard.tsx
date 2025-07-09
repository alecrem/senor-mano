interface UnitCardProps {
  number: number;
  title: string;
  verbs: string[];
  description: string;
}

export default function UnitCard({ number, title, verbs, description }: UnitCardProps) {
  return (
    <div className="unit-card">
      <div className="unit-number">Unidad {number}</div>
      <h3 className="unit-title">{title}</h3>
      <div className="unit-verbs">
        Verbos: {verbs.join(", ")}
      </div>
      <p className="unit-content">
        {description}
      </p>
      <div className="download-buttons">
        <a
          href={`/pdfs/japanese/unidad-${number}-ja.pdf`}
          className="download-btn download-btn-primary"
          download
        >
          📖 Descargar en Japonés
        </a>
        <a
          href={`/pdfs/english/unidad-${number}-en.pdf`}
          className="download-btn download-btn-secondary"
          download
        >
          📖 Descargar en Inglés
        </a>
      </div>
    </div>
  );
}