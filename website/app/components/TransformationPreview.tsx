interface TransformationPreviewProps {
  content: string;
}

const styles = {
  exercise: {
    marginBottom: "1.5rem",
    fontSize: "1rem",
    lineHeight: "1.6",
  },
  exerciseNumber: {
    fontWeight: "600",
    color: "#1a1a1a",
  },
  transformation: {
    backgroundColor: "#f0f8f0",
    padding: "1rem",
    borderRadius: "8px",
    marginTop: "0.5rem",
  },
  arrow: {
    fontWeight: "bold",
    color: "#6AAD2F",
    margin: "0 0.5rem",
  },
  blank: {
    fontWeight: "bold",
    textDecoration: "underline",
    color: "#6b7280",
  },
  section: {
    marginBottom: "2rem",
  },
  sectionTitle: {
    fontSize: "1.3rem",
    fontWeight: "600",
    marginBottom: "1rem",
    color: "#374151",
    borderBottom: "2px solid #e5e7eb",
    paddingBottom: "0.5rem",
  },
};

function parseTransformationExercises(content: string) {
  const lines = content.split('\n').filter(line => line.trim());
  
  let title = "";
  let transformationExercises: Array<{ number: string; text: string }> = [];
  let dialogueExercises: Array<{ number: string; text: string }> = [];
  
  let currentSection = "";
  
  for (const line of lines) {
    if (line.startsWith('#')) {
      if (line.startsWith('# ')) {
        title = line.replace('# ', '');
      } else if (line.startsWith('## ')) {
        currentSection = line.replace('## ', '');
      }
      continue;
    }
    
    // Parse exercises
    const exerciseMatch = line.match(/^\*\*(\d+)\.\*\*\s*(.*)/);
    if (exerciseMatch) {
      const number = exerciseMatch[1];
      const text = exerciseMatch[2];
      
      // Determine which section based on content or section title
      if (currentSection.includes('対話') || currentSection.includes('diálogo') || currentSection.includes('dialogue') || 
          text.includes('?') || text.includes('¿')) {
        dialogueExercises.push({ number, text });
      } else {
        transformationExercises.push({ number, text });
      }
    }
  }
  
  return { title, transformationExercises, dialogueExercises };
}

function renderTransformation(text: string) {
  // Handle transformations like "Yo verb → Nosotros **___**" or with [SHORT_LINE]
  if (text.includes('→')) {
    const [before, after] = text.split('→').map(s => s.trim());
    const processedAfter = after
      .replace(/\*\*([^*]+)\*\*/g, '$1')
      .replace(/\[SHORT_LINE\]/g, '______');
    
    return (
      <div style={styles.transformation}>
        <span>{before}</span>
        <span style={styles.arrow}>→</span>
        <span>{processedAfter}</span>
      </div>
    );
  }
  
  // Handle other transformations with blanks
  return text
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\[SHORT_LINE\]/g, '______');
}

export default function TransformationPreview({ content }: TransformationPreviewProps) {
  const { title, transformationExercises, dialogueExercises } = parseTransformationExercises(content);
  
  return (
    <div>
      <h2 style={{ 
        fontSize: "1.5rem", 
        fontWeight: "700", 
        marginBottom: "1rem",
        fontFamily: "'Delius', system-ui, sans-serif",
      }}>
        {title}
      </h2>
      
      {transformationExercises.length > 0 && (
        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>Transformaciones</h3>
          {transformationExercises.map((exercise, index) => (
            <div key={index} style={styles.exercise}>
              <span style={styles.exerciseNumber}>{exercise.number}.</span>{' '}
              {renderTransformation(exercise.text)}
            </div>
          ))}
        </div>
      )}
      
      {dialogueExercises.length > 0 && (
        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>Preguntas y respuestas</h3>
          {dialogueExercises.map((exercise, index) => (
            <div key={index} style={styles.exercise}>
              <span style={styles.exerciseNumber}>{exercise.number}.</span>{' '}
              <span>{exercise.text.replace(/\*\*([^*]+)\*\*/g, '$1').replace(/\[SHORT_LINE\]/g, '______')}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}