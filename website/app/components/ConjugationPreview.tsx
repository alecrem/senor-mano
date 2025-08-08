interface ConjugationPreviewProps {
  content: string;
}

const styles = {
  table: {
    width: "100%",
    borderCollapse: "collapse" as const,
    marginBottom: "1.5rem",
    fontSize: "1rem",
  },
  tableCell: {
    padding: "0.75rem",
    border: "1px solid #d1d5db",
    textAlign: "left" as const,
  },
  tableHeader: {
    backgroundColor: "#f9fafb",
    fontWeight: "600",
  },
  exercise: {
    marginBottom: "0.75rem",
    fontSize: "1rem",
    lineHeight: "1.6",
  },
  exerciseNumber: {
    fontWeight: "600",
    color: "#1a1a1a",
  },
  blank: {
    display: "inline-block",
    borderBottom: "2px solid #6b7280",
    minWidth: "80px",
    height: "1.2em",
    margin: "0 4px",
  },
  example: {
    fontWeight: "600",
    marginBottom: "1.5rem",
    padding: "1rem",
    backgroundColor: "#f0f8f0",
    borderRadius: "8px",
    fontSize: "1rem",
  },
};

function parseConjugation(content: string) {
  const lines = content.split('\n').filter(line => line.trim());
  
  let title = "";
  let subtitle = "";
  let example = "";
  let tableRows: Array<{ pronoun: string; conjugation: string; pronoun2?: string; conjugation2?: string }> = [];
  let exercises: Array<{ number: string; text: string }> = [];
  
  let inTable = false;
  let inExercises = false;
  
  for (const line of lines) {
    if (line.startsWith('#')) {
      if (line.startsWith('# ')) {
        title = line.replace('# ', '');
      } else if (line.startsWith('## ') && !line.includes('正しい形で')) {
        subtitle = line.replace('## ', '');
      } else if (line.includes('正しい形で') || line.includes('Complete') || line.includes('Completa')) {
        inExercises = true;
        continue;
      }
      continue;
    }
    
    // Parse example
    if (line.startsWith('**例文:**') || line.startsWith('**Ejemplo:**') || line.startsWith('**Example:**')) {
      example = line.replace(/\*\*[^*]+:\*\*\s*/, '');
      continue;
    }
    
    // Parse table rows
    if (line.includes('|') && !line.startsWith('|---')) {
      const cells = line.split('|').map(cell => cell.trim()).filter(cell => cell);
      if (cells.length >= 2) {
        if (cells.length === 4) {
          tableRows.push({
            pronoun: cells[0],
            conjugation: cells[1],
            pronoun2: cells[2],
            conjugation2: cells[3],
          });
        } else {
          tableRows.push({
            pronoun: cells[0],
            conjugation: cells[1],
          });
        }
      }
      continue;
    }
    
    // Parse exercises
    if (inExercises && line.match(/^\*\*\d+\.\*\*/)) {
      const exerciseMatch = line.match(/^\*\*(\d+)\.\*\*\s*(.*)/);
      if (exerciseMatch) {
        exercises.push({
          number: exerciseMatch[1],
          text: exerciseMatch[2]
        });
      }
    }
  }
  
  return { title, subtitle, example, tableRows, exercises };
}

function renderTextWithBlanks(text: string) {
  // Replace [SHORT_LINE] with visual blanks
  return text.split(/(\[SHORT_LINE\])/).map((part, index) => {
    if (part === '[SHORT_LINE]') {
      return <span key={index} style={styles.blank}></span>;
    }
    return part;
  });
}

export default function ConjugationPreview({ content }: ConjugationPreviewProps) {
  const { title, subtitle, example, tableRows, exercises } = parseConjugation(content);
  
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
      
      {tableRows.length > 0 && (
        <table style={styles.table}>
          <tbody>
            {tableRows.map((row, index) => (
              <tr key={index}>
                <td style={{...styles.tableCell, ...styles.tableHeader}}>
                  {row.pronoun}
                </td>
                <td style={styles.tableCell}>
                  {row.conjugation}
                </td>
                {row.pronoun2 && (
                  <>
                    <td style={{...styles.tableCell, ...styles.tableHeader}}>
                      {row.pronoun2}
                    </td>
                    <td style={styles.tableCell}>
                      {row.conjugation2}
                    </td>
                  </>
                )}
              </tr>
            ))}
          </tbody>
        </table>
      )}
      
      {example && (
        <div style={styles.example}>
          {example}
        </div>
      )}
      
      {exercises.length > 0 && (
        <div>
          {exercises.map((exercise, index) => (
            <div key={index} style={styles.exercise}>
              <span style={styles.exerciseNumber}>{exercise.number}.</span>{' '}
              {renderTextWithBlanks(exercise.text)}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}