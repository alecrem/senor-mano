import React from "react";

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
  let sections: Array<{
    subtitle: string;
    example?: string;
    exercises: Array<{ number: string; text: string }>;
    tableRows?: Array<{ pronoun: string; conjugation: string; pronoun2?: string; conjugation2?: string }>;
  }> = [];
  
  let currentSection: { title: string; content: React.ReactNode } | null = null;
  let tableRows: Array<{ pronoun: string; conjugation: string; pronoun2?: string; conjugation2?: string }> = [];
  
  for (const line of lines) {
    if (line.startsWith('#')) {
      if (line.startsWith('# ')) {
        title = line.replace('# ', '');
      } else if (line.startsWith('## ')) {
        // Start new section
        if (currentSection) {
          if (tableRows.length > 0) {
            currentSection.tableRows = [...tableRows];
            tableRows = [];
          }
          sections.push(currentSection);
        }
        currentSection = {
          subtitle: line.replace('## ', ''),
          exercises: []
        };
      }
      continue;
    }
    
    // Parse example
    if (line.startsWith('**例文:**') || line.startsWith('**Ejemplo:**') || line.startsWith('**Example:**')) {
      if (currentSection) {
        currentSection.example = line.replace(/\*\*[^*]+:\*\*\s*/, '');
      }
      continue;
    }
    
    // Parse table rows (skip separator rows with dashes)
    if (line.includes('|') && !line.match(/^\|\s*[-\s|]+\s*\|?$/)) {
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
    if (line.match(/^\*\*\d+\.\*\*/)) {
      const exerciseMatch = line.match(/^\*\*(\d+)\.\*\*\s*(.*)/);
      if (exerciseMatch && currentSection) {
        currentSection.exercises.push({
          number: exerciseMatch[1],
          text: exerciseMatch[2]
        });
      }
    }
    
    // Handle standalone example/description lines
    if (line.trim() && !line.startsWith('**') && !line.includes('|') && currentSection && currentSection.exercises.length === 0 && !currentSection.example) {
      currentSection.example = line.trim();
    }
  }
  
  // Add final section
  if (currentSection) {
    if (tableRows.length > 0) {
      currentSection.tableRows = [...tableRows];
    }
    sections.push(currentSection);
  }
  
  return { title, sections };
}

function renderTextWithBlanks(text: string) {
  // Replace placeholders with visual blanks first
  const processedText = text
    .replace(/\[SHORT_LINE\]/g, '______')
    .replace(/\[LONG_LINE\]/g, '________________')
    .replace(/\[ONE_LETTER_LINE\]/g, '_');
  
  // Then handle markdown bold formatting
  const parts = processedText.split(/(\*\*[^*]+\*\*)/);
  return parts.map((part, index) => {
    if (part.startsWith('**') && part.endsWith('**')) {
      const boldText = part.slice(2, -2);
      return <strong key={index}>{boldText}</strong>;
    }
    return part;
  });
}

export default function ConjugationPreview({ content }: ConjugationPreviewProps) {
  const { title, sections } = parseConjugation(content);
  
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
      
      {sections.map((section, sectionIndex) => (
        <div key={sectionIndex} style={{ marginBottom: "2rem" }}>
          <h3 style={{
            fontSize: "1.2rem",
            fontWeight: "600", 
            marginBottom: "1.5rem",
            color: "#4b5563",
          }}>
            {section.subtitle}
          </h3>
          
          {section.example && (
            <div style={styles.example}>
              {renderTextWithBlanks(section.example)}
            </div>
          )}
          
          {section.tableRows && section.tableRows.length > 0 && (
            <table style={styles.table}>
              <tbody>
                {section.tableRows.map((row, index) => (
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
          
          {section.exercises.length > 0 && (
            <div>
              {section.exercises.map((exercise, index) => (
                <div key={index} style={styles.exercise}>
                  <span style={styles.exerciseNumber}>{exercise.number}.</span>{' '}
                  <span>{renderTextWithBlanks(exercise.text)}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}