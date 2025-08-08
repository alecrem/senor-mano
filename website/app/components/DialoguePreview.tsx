interface DialoguePreviewProps {
  content: string;
}

const styles = {
  dialogue: {
    lineHeight: "1.8",
    fontSize: "1.1rem",
  },
  speaker: {
    fontWeight: "600",
    color: "#1a1a1a",
  },
  line: {
    marginBottom: "0.8rem",
  },
};

function parseDialogue(content: string) {
  const lines = content.split('\n').filter(line => line.trim());
  const dialogueLines: Array<{ speaker: string; text: string }> = [];
  
  let title = "";
  let subtitle = "";
  
  for (const line of lines) {
    // Skip markdown headers
    if (line.startsWith('#')) {
      if (line.startsWith('# ')) {
        title = line.replace('# ', '');
      } else if (line.startsWith('## ')) {
        subtitle = line.replace('## ', '');
      }
      continue;
    }
    
    // Parse dialogue lines with **Speaker:** format
    const speakerMatch = line.match(/\*\*([^*]+):\*\*\s*(.*)/);
    if (speakerMatch) {
      const [, speaker, text] = speakerMatch;
      dialogueLines.push({ speaker, text });
    }
  }
  
  return { title, subtitle, dialogueLines };
}

export default function DialoguePreview({ content }: DialoguePreviewProps) {
  const { title, subtitle, dialogueLines } = parseDialogue(content);
  
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
      
      <div style={styles.dialogue}>
        {dialogueLines.map((line, index) => (
          <div key={index} style={styles.line}>
            <span style={styles.speaker}>{line.speaker}:</span>{' '}
            <span>{line.text}</span>
          </div>
        ))}
      </div>
    </div>
  );
}