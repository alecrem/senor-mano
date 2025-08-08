import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Source and destination paths
const sourceBase = join(__dirname, '..', 'ejercicios-src', 'markdown');
const destBase = join(__dirname, 'app', 'data', 'markdown');

// Create destination directory if it doesn't exist
if (!existsSync(destBase)) {
  mkdirSync(destBase, { recursive: true });
}

const tenses = ['present-tense', 'past-tense'];
const cuadernillos = ['cuadernillo-1-ar-verbs', 'cuadernillo-2-er-verbs', 'cuadernillo-3-ir-verbs', 'cuadernillo-4-mixed-verbs'];
const languages = ['japanese', 'english'];
const pages = [
  'pagina-1-dialogo.md',
  'pagina-2-conjugacion-completar.md', 
  'pagina-3-eleccion.md',
  'pagina-4-transformacion.md',
  'pagina-5-ordenar.md',
  'pagina-6-bien-mal.md'
];

console.log('Copying markdown files...');

for (const tense of tenses) {
  for (const cuadernillo of cuadernillos) {
    for (const language of languages) {
      const sourceDir = join(sourceBase, tense, cuadernillo, language);
      const destDir = join(destBase, tense, cuadernillo, language);
      
      // Create destination directory
      if (!existsSync(destDir)) {
        mkdirSync(destDir, { recursive: true });
      }
      
      for (const page of pages) {
        const sourcePath = join(sourceDir, page);
        const destPath = join(destDir, page);
        
        try {
          const content = readFileSync(sourcePath, 'utf-8');
          writeFileSync(destPath, content);
          console.log(`✓ ${tense}/${cuadernillo}/${language}/${page}`);
        } catch (error) {
          console.error(`✗ Failed to copy ${sourcePath}:`, error.message);
        }
      }
    }
  }
}

console.log('Markdown files copied successfully!');