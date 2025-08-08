interface ChoicePreviewProps {
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
  choices: {
    backgroundColor: "#f0f8f0",
    padding: "0.5rem 1rem",
    borderRadius: "6px",
    display: "inline-block",
    margin: "0 0.5rem",
    fontWeight: "600",
  },
  writeLine: {
    borderBottom: "2px solid #6b7280",
    height: "2px",
    marginTop: "0.5rem",
    width: "100%",
  },
};

function parseChoiceExercises(content: string) {
  const lines = content.split('\n').filter(line => line.trim());
  
  let title = "";
  let subtitle = "";
  let exercises: Array<{ number: string; text: string; hasWriteLine: boolean }> = [];
  
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
      const text = exerciseMatch[2];
      
      // Check if next line has [LONG_LINE]
      const nextLine = i + 1 < lines.length ? lines[i + 1] : '';
      const hasWriteLine = nextLine.includes('[LONG_LINE]');
      
      exercises.push({ number, text, hasWriteLine });
    }
  }
  
  return { title, subtitle, exercises };
}

function renderTextWithChoices(text: string) {
  // Parse text with [option1 | option2] format
  return text.split(/(\[[^\]]+\])/).map((part, index) => {
    const choiceMatch = part.match(/\[([^|]+)\s*\|\s*([^\]]+)\]/);
    if (choiceMatch) {
      const [, option1, option2] = choiceMatch;
      return (
        <span key={index} style={styles.choices}>
          {option1.trim()} | {option2.trim()}
        </span>
      );
    }
    return part;
  });
}

export default function ChoicePreview({ content }: ChoicePreviewProps) {
  const { title, subtitle, exercises } = parseChoiceExercises(content);
  
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
            <span style={styles.exerciseNumber}>{exercise.number}.</span>{' '}
            {renderTextWithChoices(exercise.text)}
          </div>
          {exercise.hasWriteLine && (
            <div style={styles.writeLine}></div>
          )}
        </div>
      ))}
    </div>
  );
}