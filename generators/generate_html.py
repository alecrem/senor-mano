#!/usr/bin/env python3
"""
Generate HTML files for GitHub Pages from Spanish exercise markdown files.
Creates a web interface for accessing exercises and downloading PDFs.
"""

import os
import sys
import argparse
from pathlib import Path
import markdown
import yaml
from jinja2 import Template


def load_translations(language='ja'):
    """Load translation strings for the specified language."""
    translation_file = Path(f"content/translations/{language}.yaml")
    
    if not translation_file.exists():
        print(f"Warning: Translation file {translation_file} not found, using Japanese as fallback")
        translation_file = Path("content/translations/ja.yaml")
    
    try:
        with open(translation_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error: Could not load translations: {e}")
        return {}


def load_unit_metadata(unit_number):
    """Load metadata for a specific unit."""
    metadata_file = Path(f"content/units/unit-{unit_number}/metadata.yaml")
    
    if not metadata_file.exists():
        return {"title": f"Unidad {unit_number}", "verbs": [], "unit_number": unit_number}
    
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Warning: Could not read metadata for unit {unit_number}: {e}")
        return {"title": f"Unidad {unit_number}", "verbs": [], "unit_number": unit_number}


def generate_page_html(unit_number, page_type, translations):
    """Generate HTML content for a specific page."""
    content_file = Path(f"content/units/unit-{unit_number}/{page_type}.md")
    
    if not content_file.exists():
        return f"<p>Content not found: {content_file}</p>"
    
    # Read the markdown content
    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables', 'nl2br'])
    html_content = md.convert(content)
    
    # Add page header
    header_map = {
        'dialogue': translations.get('dialogue_header', '会話 (Diálogo)'),
        'conjugation': translations.get('conjugation_header', '動詞の活用と完成 (Conjugación y completar)'),
        'choice': translations.get('choice_header', '選択問題 (Ejercicios de elección)'),
        'transformation': translations.get('transformation_header', '変換練習 (Ejercicios de transformación)'),
        'ordering': translations.get('ordering_header', '語順並べ替え (Ejercicios de ordenar)'),
        'correction': translations.get('correction_header', '正しい・間違い (Bien / Mal)')
    }
    
    header = header_map.get(page_type, page_type.title())
    
    return f"""
    <div class="exercise-page" id="page-{page_type}">
        <h2>{header}</h2>
        {html_content}
    </div>
    """


def create_unit_page(unit_number, language='ja', output_dir='docs'):
    """Create HTML page for a specific unit."""
    translations = load_translations(language)
    metadata = load_unit_metadata(unit_number)
    
    # Generate content for each page
    page_types = ['dialogue', 'conjugation', 'choice', 'transformation', 'ordering', 'correction']
    pages_html = []
    
    for page_type in page_types:
        page_html = generate_page_html(unit_number, page_type, translations)
        pages_html.append(page_html)
    
    # HTML template for unit page
    unit_template = Template("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ unit_title }} - {{ language_name }}</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <h1><a href="../index.html">Cuadernillos de Español</a></h1>
            <div class="nav-links">
                <a href="../index.html">Inicio</a>
                <div class="language-selector">
                    <select onchange="switchLanguage(this.value)">
                        <option value="ja" {{ 'selected' if language == 'ja' else '' }}>日本語</option>
                        <option value="en" {{ 'selected' if language == 'en' else '' }}>English</option>
                        <option value="es" {{ 'selected' if language == 'es' else '' }}>Español</option>
                    </select>
                </div>
            </div>
        </div>
    </nav>

    <main class="container">
        <header class="unit-header">
            <h1>{{ unit_title }}</h1>
            <p class="unit-description">{{ unit_description }}</p>
            <div class="unit-verbs">
                <strong>Verbos:</strong> {{ verbs_list }}
            </div>
            <div class="download-section">
                <a href="../pdfs/{{ language }}/unidad-{{ unit_number }}.pdf" class="btn btn-primary" download>
                    📄 Descargar PDF
                </a>
            </div>
        </header>

        <div class="exercise-navigation">
            <h3>Páginas:</h3>
            <nav class="page-nav">
                <a href="#page-dialogue" class="nav-btn">1. {{ dialogue_header }}</a>
                <a href="#page-conjugation" class="nav-btn">2. {{ conjugation_header }}</a>
                <a href="#page-choice" class="nav-btn">3. {{ choice_header }}</a>
                <a href="#page-transformation" class="nav-btn">4. {{ transformation_header }}</a>
                <a href="#page-ordering" class="nav-btn">5. {{ ordering_header }}</a>
                <a href="#page-correction" class="nav-btn">6. {{ correction_header }}</a>
            </nav>
        </div>

        <div class="exercises-content">
            {% for page_html in pages_html %}
            {{ page_html }}
            {% endfor %}
        </div>
    </main>

    <footer>
        <p>&copy; 2024 Cuadernillos de Español. Diseñado para familias hispanohablantes.</p>
    </footer>

    <script>
        function switchLanguage(lang) {
            window.location.href = `../${lang}/unit-{{ unit_number }}.html`;
        }
        
        // Smooth scrolling for navigation
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                target.scrollIntoView({ behavior: 'smooth' });
            });
        });
    </script>
</body>
</html>
    """)
    
    # Render the template
    html_content = unit_template.render(
        unit_title=metadata['title'],
        unit_description=metadata.get('description', ''),
        unit_number=unit_number,
        language=language,
        language_name=translations.get('language_name', 'Japanese'),
        verbs_list=', '.join(metadata.get('verbs', [])),
        dialogue_header=translations.get('dialogue_header', '会話'),
        conjugation_header=translations.get('conjugation_header', '動詞の活用'),
        choice_header=translations.get('choice_header', '選択問題'),
        transformation_header=translations.get('transformation_header', '変換練習'),
        ordering_header=translations.get('ordering_header', '語順並べ替え'),
        correction_header=translations.get('correction_header', '正しい・間違い'),
        pages_html=pages_html
    )
    
    # Create output directory
    output_path = Path(output_dir) / language
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Write HTML file
    output_file = output_path / f"unit-{unit_number}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Generated {output_file}")
    return True


def create_index_page(output_dir='docs'):
    """Create main index page for all units and languages."""
    
    # Load metadata for all units
    units_data = []
    for unit_num in [1, 2, 3]:
        metadata = load_unit_metadata(unit_num)
        units_data.append(metadata)
    
    # Load translations for all languages
    translations_all = {}
    for lang in ['ja', 'en', 'es']:
        translations_all[lang] = load_translations(lang)
    
    index_template = Template("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cuadernillos de Español - Ejercicios para niños</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <h1>Cuadernillos de Español</h1>
        </div>
    </nav>

    <main class="container">
        <header class="hero">
            <h1>Ejercicios de Español para Niños</h1>
            <p class="hero-description">
                Materiales diseñados para niños que reciben educación en japonés pero hablan español en casa.
                Enfoque en conjugaciones verbales regulares con instrucciones en múltiples idiomas.
            </p>
        </header>

        <section class="language-selection">
            <h2>Elige el idioma de las instrucciones</h2>
            <div class="language-grid">
                <div class="language-card">
                    <h3>🇯🇵 日本語 (Japonés)</h3>
                    <p>Para estudiantes en Japón</p>
                    <a href="ja/" class="btn btn-primary">Ver ejercicios</a>
                </div>
                <div class="language-card">
                    <h3>🇺🇸 English (Inglés)</h3>
                    <p>For international students</p>
                    <a href="en/" class="btn btn-primary">View exercises</a>
                </div>
                <div class="language-card">
                    <h3>🇪🇸 Español</h3>
                    <p>Para profesores hispanohablantes</p>
                    <a href="es/" class="btn btn-primary">Ver ejercicios</a>
                </div>
            </div>
        </section>

        <section class="units-overview">
            <h2>Unidades disponibles</h2>
            <div class="units-grid">
                {% for unit in units_data %}
                <div class="unit-card">
                    <h3>{{ unit.title }}</h3>
                    <p class="unit-description">{{ unit.description }}</p>
                    <div class="unit-verbs">
                        <strong>Verbos:</strong> {{ unit.verbs | join(', ') }}
                    </div>
                    <div class="unit-actions">
                        <a href="ja/unit-{{ unit.unit_number }}.html" class="btn btn-outline">Ver en japonés</a>
                        <a href="en/unit-{{ unit.unit_number }}.html" class="btn btn-outline">View in English</a>
                        <a href="es/unit-{{ unit.unit_number }}.html" class="btn btn-outline">Ver en español</a>
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>

        <section class="features">
            <h2>Características</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <h3>📄 PDFs imprimibles</h3>
                    <p>Formato DIN A5 optimizado para imprimir en casa</p>
                </div>
                <div class="feature-card">
                    <h3>🌍 Multi-idioma</h3>
                    <p>Instrucciones en japonés, inglés y español</p>
                </div>
                <div class="feature-card">
                    <h3>📚 Progresión pedagógica</h3>
                    <p>6 páginas por unidad con dificultad gradual</p>
                </div>
                <div class="feature-card">
                    <h3>🎯 Enfoque específico</h3>
                    <p>Diseñado para niños bilingües español-japonés</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-content">
            <p>&copy; 2024 Cuadernillos de Español. Proyecto de código abierto para familias hispanohablantes.</p>
            <p>
                <a href="https://github.com/tu-usuario/ejercicios-espanol">GitHub</a> |
                <a href="#contacto">Contacto</a> |
                <a href="#licencia">Licencia MIT</a>
            </p>
        </div>
    </footer>
</body>
</html>
    """)
    
    # Render the template
    html_content = index_template.render(units_data=units_data)
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Write HTML file
    output_file = output_path / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Generated {output_file}")
    return True


def create_language_index(language, output_dir='docs'):
    """Create index page for a specific language."""
    translations = load_translations(language)
    units_data = []
    for unit_num in [1, 2, 3]:
        metadata = load_unit_metadata(unit_num)
        units_data.append(metadata)
    
    lang_index_template = Template("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cuadernillos de Español - {{ language_name }}</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <h1><a href="../index.html">Cuadernillos de Español</a></h1>
            <div class="nav-links">
                <a href="../index.html">Inicio</a>
                <span class="current-language">{{ language_name }}</span>
            </div>
        </div>
    </nav>

    <main class="container">
        <header class="language-hero">
            <h1>Ejercicios en {{ language_name }}</h1>
            <p>Selecciona una unidad para comenzar</p>
        </header>

        <section class="units-list">
            {% for unit in units_data %}
            <div class="unit-item">
                <div class="unit-info">
                    <h2><a href="unit-{{ unit.unit_number }}.html">{{ unit.title }}</a></h2>
                    <p class="unit-description">{{ unit.description }}</p>
                    <div class="unit-verbs">
                        <strong>Verbos:</strong> {{ unit.verbs | join(', ') }}
                    </div>
                </div>
                <div class="unit-actions">
                    <a href="unit-{{ unit.unit_number }}.html" class="btn btn-primary">Ver ejercicios</a>
                    <a href="../pdfs/{{ language }}/unidad-{{ unit.unit_number }}.pdf" class="btn btn-outline" download>Descargar PDF</a>
                </div>
            </div>
            {% endfor %}
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Cuadernillos de Español</p>
    </footer>
</body>
</html>
    """)
    
    # Render the template
    html_content = lang_index_template.render(
        language=language,
        language_name=translations.get('language_name', language),
        units_data=units_data
    )
    
    # Create output directory
    output_path = Path(output_dir) / language
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Write HTML file
    output_file = output_path / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Generated {output_file}")
    return True


def create_css():
    """Create CSS styles for the website."""
    css_content = """
/* CSS for Spanish Exercises Website */

:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --light-bg: #f8f9fa;
    --border-color: #dee2e6;
    --text-color: #333;
    --text-light: #666;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Hiragino Sans', 'Yu Gothic', 'Meiryo', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: #fff;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navigation */
.navbar {
    background-color: var(--primary-color);
    color: white;
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 100;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.navbar h1 a {
    color: white;
    text-decoration: none;
    font-size: 1.5rem;
}

.nav-links {
    display: flex;
    gap: 20px;
    align-items: center;
}

.nav-links a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.nav-links a:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

/* Buttons */
.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 500;
    text-align: center;
    transition: all 0.3s;
    border: 2px solid transparent;
}

.btn-primary {
    background-color: var(--secondary-color);
    color: white;
}

.btn-primary:hover {
    background-color: #2980b9;
}

.btn-outline {
    border-color: var(--secondary-color);
    color: var(--secondary-color);
    background: transparent;
}

.btn-outline:hover {
    background-color: var(--secondary-color);
    color: white;
}

/* Hero sections */
.hero, .language-hero, .unit-header {
    text-align: center;
    padding: 3rem 0;
    background-color: var(--light-bg);
    margin-bottom: 3rem;
    border-radius: 10px;
}

.hero h1, .language-hero h1, .unit-header h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: var(--primary-color);
}

.hero-description, .unit-description {
    font-size: 1.1rem;
    color: var(--text-light);
    max-width: 800px;
    margin: 0 auto 2rem;
}

/* Cards and grids */
.language-grid, .units-grid, .features-grid {
    display: grid;
    gap: 2rem;
    margin: 2rem 0;
}

.language-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.units-grid {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

.features-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.language-card, .unit-card, .feature-card {
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.language-card:hover, .unit-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}

.unit-verbs {
    margin: 1rem 0;
    font-size: 0.9rem;
    color: var(--text-light);
}

.unit-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

/* Exercise pages */
.exercise-page {
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 2rem;
    margin: 2rem 0;
}

.exercise-page h2 {
    color: var(--primary-color);
    border-bottom: 2px solid var(--secondary-color);
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

.page-nav {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin: 1rem 0;
}

.nav-btn {
    padding: 0.5rem 1rem;
    background-color: var(--light-bg);
    color: var(--text-color);
    text-decoration: none;
    border-radius: 6px;
    font-size: 0.9rem;
    transition: background-color 0.3s;
}

.nav-btn:hover {
    background-color: var(--secondary-color);
    color: white;
}

/* Units list */
.units-list {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.unit-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.unit-info h2 a {
    color: var(--primary-color);
    text-decoration: none;
}

.unit-info h2 a:hover {
    color: var(--secondary-color);
}

/* Language selector */
.language-selector select {
    padding: 0.5rem;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 4px;
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
}

th, td {
    border: 1px solid var(--border-color);
    padding: 0.75rem;
    text-align: left;
}

th {
    background-color: var(--light-bg);
    font-weight: 600;
}

/* Footer */
footer {
    background-color: var(--primary-color);
    color: white;
    padding: 2rem 0;
    text-align: center;
    margin-top: 3rem;
}

.footer-content a {
    color: white;
    text-decoration: none;
}

.footer-content a:hover {
    text-decoration: underline;
}

/* Responsive design */
@media (max-width: 768px) {
    .nav-container {
        flex-direction: column;
        gap: 1rem;
    }
    
    .unit-item {
        flex-direction: column;
        gap: 1rem;
        text-align: center;
    }
    
    .hero h1, .language-hero h1, .unit-header h1 {
        font-size: 2rem;
    }
    
    .container {
        padding: 0 15px;
    }
}

/* Print styles */
@media print {
    .navbar, footer, .nav-links, .download-section {
        display: none;
    }
    
    .exercise-page {
        page-break-after: always;
        border: none;
        box-shadow: none;
    }
}
"""
    
    # Create CSS directory
    css_dir = Path("docs/assets/css")
    css_dir.mkdir(parents=True, exist_ok=True)
    
    # Write CSS file
    css_file = css_dir / "style.css"
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print(f"✅ Generated {css_file}")
    return True


def main():
    """Main function to generate HTML files."""
    parser = argparse.ArgumentParser(description='Generate HTML files for GitHub Pages')
    parser.add_argument('--unit', type=int, choices=[1, 2, 3], help='Generate specific unit')
    parser.add_argument('--language', type=str, choices=['ja', 'en', 'es'], help='Generate specific language')
    parser.add_argument('--output', type=str, default='docs', help='Output directory')
    parser.add_argument('--preview', action='store_true', help='Generate for local preview')
    
    args = parser.parse_args()
    
    # Create CSS styles
    create_css()
    
    # Generate main index page
    create_index_page(args.output)
    
    languages = [args.language] if args.language else ['ja', 'en', 'es']
    units = [args.unit] if args.unit else [1, 2, 3]
    
    success_count = 0
    total_files = len(languages) * (len(units) + 1)  # +1 for language index
    
    print(f"Generating {total_files} HTML files...")
    
    for language in languages:
        # Create language index
        if create_language_index(language, args.output):
            success_count += 1
        
        # Create unit pages
        for unit_num in units:
            if create_unit_page(unit_num, language, args.output):
                success_count += 1
    
    print(f"\n🎉 Successfully generated {success_count + 1}/{total_files + 1} HTML files")
    
    if args.preview:
        print("\n🌐 To preview locally, run:")
        print(f"  cd {args.output} && python -m http.server 8000")
        print("  Then open http://localhost:8000")
    else:
        print(f"\n📁 Files ready for GitHub Pages in '{args.output}/' directory")


if __name__ == "__main__":
    main()