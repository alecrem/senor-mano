interface EvaluationPreviewProps {
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
  sentence: {
    backgroundColor: "#f9fafb",
    padding: "1rem",
    borderRadius: "8px",
    marginTop: "0.5rem",
    marginBottom: "0.5rem",
    border: "1px solid #e5e7eb",
  },
  evaluationBox: {
    display: "inline-block",
    width: "60px",
    height: "30px",
    border: "2px solid #d1d5db",
    borderRadius: "4px",
    marginLeft: "1rem",
    backgroundColor: "#fff",
  },
  correction: {
    color: "#6b7280",
    fontWeight: "500",
    marginTop: "0.5rem",
    borderBottom: "1px solid #e5e7eb",
    paddingBottom: "0.5rem",
  },
  correctionLine: {
    borderBottom: "2px solid #6b7280",
    height: "1.5rem",
    marginTop: "0.25rem",
  },
};

function parseEvaluationExercises(content: string) {
  const lines = content.split('\n').filter(line => line.trim());
  
  let title = "";
  let subtitle = "";
  let exercises: Array<{ 
    number: string; 
    sentence: string;
    hasCorrection: boolean;
  }> = [];
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    if (line.startsWith('#')) {
      if (line.startsWith('# ')) {
        title = line.replace('# ', '');
      } else if (line.startsWith('## ')) {
        subtitle = line.replace('## ', '');
      }
      continue;
    }
    
    // Parse exercises
    const exerciseMatch = line.match(/^\*\*(\d+)\.\*\*\s*(.*)/);
    if (exerciseMatch) {
      const number = exerciseMatch[1];
      let sentence = exerciseMatch[2];
      
      // Remove evaluation blank (___) from sentence
      sentence = sentence.replace(/\s*___$/, '');
      
      // Check if next line has correction
      let hasCorrection = false;
      if (i + 1 < lines.length) {
        const nextLine = lines[i + 1];
        hasCorrection = nextLine.includes('Corrección:') || nextLine.includes('Correction:') || nextLine.includes('修正:');
      }
      
      exercises.push({ number, sentence, hasCorrection });
    }
  }
  
  return { title, subtitle, exercises };
}

export default function EvaluationPreview({ content }: EvaluationPreviewProps) {
  const { title, subtitle, exercises } = parseEvaluationExercises(content);
  
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
      
      {subtitle && (
        <h3 style={{
          fontSize: "1.2rem",
          fontWeight: "600", 
          marginBottom: "1.5rem",
          color: "#4b5563",
        }}>
          {subtitle}
        </h3>
      )}
      
      {exercises.map((exercise, index) => (
        <div key={index} style={styles.exercise}>
          <div>
            <span style={styles.exerciseNumber}>{exercise.number}.</span>
          </div>
          
          <div style={styles.sentence}>
            {exercise.sentence}
            <span style={styles.evaluationBox}></span>
          </div>
          
          {exercise.hasCorrection && (
            <div style={styles.correction}>
              Corrección:
              <div style={styles.correctionLine}></div>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}