interface OrderingPreviewProps {
  content: string;
}

const styles = {
  exercise: {
    marginBottom: "2rem",
    fontSize: "1rem",
    lineHeight: "1.6",
  },
  exerciseNumber: {
    fontWeight: "600",
    color: "#1a1a1a",
  },
  wordBox: {
    backgroundColor: "#f0f8f0",
    padding: "1rem",
    borderRadius: "8px",
    marginTop: "0.5rem",
    marginBottom: "0.5rem",
    border: "2px dashed #6AAD2F",
  },
  words: {
    display: "flex",
    flexWrap: "wrap" as const,
    gap: "0.5rem",
  },
  word: {
    backgroundColor: "#fff",
    padding: "0.5rem 1rem",
    borderRadius: "6px",
    border: "1px solid #d1d5db",
    fontWeight: "500",
  },
  translation: {
    color: "#6b7280",
    fontStyle: "italic",
    marginBottom: "0.5rem",
  },
  writeLine: {
    borderBottom: "2px solid #6b7280",
    height: "2rem",
    width: "100%",
    marginTop: "0.5rem",
  },
};

function parseOrderingExercises(content: string) {
  const lines = content.split('\n').filter(line => line.trim());
  
  let title = "";
  let subtitle = "";
  let exercises: Array<{ 
    number: string; 
    words: string[]; 
    translation: string;
    hasWriteLine: boolean;
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
    
    // Parse exercises with word arrays
    const exerciseMatch = line.match(/^\*\*(\d+)\.\*\*\s*\[([^\]]+)\]/);
    if (exerciseMatch) {
      const number = exerciseMatch[1];
      const wordsStr = exerciseMatch[2];
      const words = wordsStr.split('/').map(w => w.trim());
      
      // Look for translation in next non-empty line
      let translation = "";
      let hasWriteLine = false;
      
      for (let j = i + 1; j < lines.length; j++) {
        const nextLine = lines[j].trim();
        if (!nextLine) continue;
        
        if (nextLine.includes('[LONG_TALL_LINE]') || nextLine.includes('[LONG_LINE]')) {
          hasWriteLine = true;
          break;
        }
        
        if (nextLine.startsWith('**')) {
          // This is the next exercise
          break;
        }
        
        // This should be the translation
        translation = nextLine;
        break;
      }
      
      exercises.push({ number, words, translation, hasWriteLine });
    }
  }
  
  return { title, subtitle, exercises };
}

export default function OrderingPreview({ content }: OrderingPreviewProps) {
  const { title, subtitle, exercises } = parseOrderingExercises(content);
  
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
          <div style={{ display: "flex", alignItems: "flex-start", gap: "0.5rem" }}>
            <span style={styles.exerciseNumber}>{exercise.number}.</span>
            <div style={{ flex: "1" }}>
              <div style={styles.wordBox}>
                <div style={styles.words}>
                  {exercise.words.map((word, wordIndex) => (
                    <span key={wordIndex} style={styles.word}>
                      {word}
                    </span>
                  ))}
                </div>
              </div>
              
              {exercise.translation && (
                <div style={styles.translation}>
                  {exercise.translation}
                </div>
              )}
              
              {exercise.hasWriteLine && (
                <div style={styles.writeLine}></div>
              )}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}