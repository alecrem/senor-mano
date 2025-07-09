# Cuadernillos de español

Ejercicios de español para niños que reciben su educación principalmente en japonés o inglés. Niños que van a la escuela en japonés o inglés, pero saben bastante español porque lo escuchan en casa. Niños que saben leer y escribir en japonés o inglés pero en español todavía es un poco difícil para ellos.

## 🌐 Sitio web

**[Acceso directo a los cuadernillos](website/)** - Sitio web en español para facilitar la descarga de PDFs sin necesidad de conocimientos técnicos.

El sitio web incluye:
- Descripción completa del proyecto en español
- Descarga directa de todos los PDFs organizados por idioma de instrucciones
- Interfaz responsive optimizada para móviles y desktop
- Información detallada sobre cómo usar cada cuadernillo

## Estructura del proyecto

El proyecto contiene ejercicios de español organizados por unidades de conjugación:

- **Unidad 1**: Verbos de primera conjugación (-AR): dibujar, buscar, hablar, bailar
- **Unidad 2**: Verbos de segunda conjugación (-ER): comer, leer, aprender, beber
- **Unidad 3**: Verbos de tercera conjugación (-IR): vivir, escribir, abrir, subir

### Estructura del repositorio

El repositorio está organizado de la siguiente manera:

```
ejercicios-src/
├── markdown/              # Archivos fuente de los ejercicios
│   ├── unidad-1-ar-verbs/
│   │   ├── content/       # Contenido base en español
│   │   ├── japanese/      # Páginas con instrucciones en japonés
│   │   └── english/       # Páginas con instrucciones en inglés
│   ├── unidad-2-er-verbs/
│   │   └── (misma estructura)
│   └── unidad-3-ir-verbs/
│       └── (misma estructura)
└── scripts/               # Herramientas de generación de PDF
    ├── generate_pdf.py
    ├── generate_pdfs.sh
    ├── requirements.txt
    └── setup.sh

pdf-output/
├── japanese/              # PDFs generados con instrucciones en japonés
│   ├── unidad-1-ja.pdf
│   ├── unidad-2-ja.pdf
│   └── unidad-3-ja.pdf
└── english/               # PDFs generados con instrucciones en inglés
    ├── unidad-1-en.pdf
    ├── unidad-2-en.pdf
    └── unidad-3-en.pdf

website/                   # Sitio web Remix.js para acceso fácil
├── app/                   # Aplicación Remix
│   ├── components/        # Componentes React
│   ├── routes/            # Páginas del sitio
│   └── styles/            # Estilos CSS
├── public/
│   └── pdfs/             # PDFs servidos por el sitio web
│       ├── japanese/
│       └── english/
└── package.json
```

**Nota**: Los ejercicios de español son idénticos en ambas versiones, solo cambian las instrucciones y encabezados.

## Generación de PDFs

### Requisitos previos

- Python 3.11 o superior
- Sistema operativo macOS, Linux o Windows
- Acceso a línea de comandos

### Configuración inicial

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/ejercicios-espanol.git
   cd ejercicios-espanol
   ```

2. **Ejecutar el script de configuración**:
   ```bash
   cd ejercicios-src/scripts
   ./setup.sh
   ```
   
   Este script:
   - Crea un entorno virtual de Python en el directorio raíz del proyecto
   - Instala las dependencias necesarias (weasyprint, markdown, pyyaml)
   - Configura los permisos necesarios

   **Para usar una versión específica de Python**:
   ```bash
   PYTHON_VERSION=python3.11 ./setup.sh
   ```

### Generación de PDFs

#### Opción 1: Usar el script automatizado (recomendado)

```bash
# Generar todos los cuadernillos para ambos idiomas (japonés e inglés)
./generate_pdfs.sh

# Generar solo una unidad específica para ambos idiomas
./generate_pdfs.sh 1    # Solo unidad 1 (japonés e inglés)
./generate_pdfs.sh 2    # Solo unidad 2 (japonés e inglés)
./generate_pdfs.sh 3    # Solo unidad 3 (japonés e inglés)

# Generar para un idioma específico
./generate_pdfs.sh -l japanese        # Todos los cuadernillos en japonés
./generate_pdfs.sh -l english         # Todos los cuadernillos en inglés
./generate_pdfs.sh 1 -l english       # Solo unidad 1 en inglés
./generate_pdfs.sh 2 -l japanese      # Solo unidad 2 en japonés

# Ver todas las opciones disponibles
./generate_pdfs.sh --help
```

#### Opción 2: Uso manual

```bash
# Navegar al directorio de scripts
cd ejercicios-src/scripts

# Activar el entorno virtual
source ../../venv/bin/activate

# Generar todos los cuadernillos en japonés (por defecto)
python generate_pdf.py

# Generar todos los cuadernillos en inglés
python generate_pdf.py english

# Generar una unidad específica en japonés
python generate_pdf.py 1
python generate_pdf.py 1 japanese

# Generar una unidad específica en inglés
python generate_pdf.py 1 english
python generate_pdf.py 2 english
python generate_pdf.py 3 english

# Desactivar el entorno virtual
deactivate
```

### Archivos generados

Los PDFs se generan en formato DIN A5 (148 × 210 mm) optimizado para niños:

- **Ubicación**: Directorio `pdf-output/`
- **Nombres**: 
  - Japonés: `pdf-output/japanese/unidad-1-ja.pdf`, `unidad-2-ja.pdf`, `unidad-3-ja.pdf`
  - Inglés: `pdf-output/english/unidad-1-en.pdf`, `unidad-2-en.pdf`, `unidad-3-en.pdf`
- **Formato**: A5 con texto grande y espaciado amplio
- **Contenido**: 6 páginas por unidad (diálogo, conjugación, elección, transformación, ordenar, corrección)
- **Idiomas**: Los ejercicios en español son idénticos, solo cambian las instrucciones y encabezados

### Estructura de cada cuadernillo

Cada PDF contiene 6 páginas:

1. **Página 1 - Diálogo**: Conversación contextualizada usando los verbos de la unidad
2. **Página 2 - Conjugación**: Tabla de conjugación y ejercicios de completar
3. **Página 3 - Elección**: Ejercicios de opción múltiple
4. **Página 4 - Transformación**: Cambios de persona y preguntas-respuestas
5. **Página 5 - Ordenar**: Ejercicios de ordenamiento de palabras con traducción
6. **Página 6 - Corrección**: Ejercicios de identificar errores y corregir

### Personalización

#### Cambiar idioma de las instrucciones

Los scripts ahora soportan automáticamente ambos idiomas. No es necesario editar archivos:

```bash
# Generar en japonés (por defecto)
./generate_pdfs.sh

# Generar en inglés
./generate_pdfs.sh -l english

# Generar ambos idiomas
./generate_pdfs.sh -l both
```

#### Modificar el estilo del PDF

El estilo se puede personalizar editando la función `create_css_style()` en `ejercicios-src/scripts/generate_pdf.py`:

- **Tamaño de página**: Cambiar `size: A5` por `size: A4` o `size: letter`
- **Márgenes**: Modificar los valores en `margin: 10mm 8mm 15mm 8mm`
- **Fuentes**: Ajustar `font-size` y `font-family`
- **Colores**: Cambiar los códigos de color hexadecimales

### Resolución de problemas

#### Error: "command not found: python3.12"

Instala Python 3.12 o usa una versión disponible:
```bash
# Listar versiones disponibles
ls -1 /opt/homebrew/bin/python3* | grep -E "python3\.[0-9]+$"

# Usar una versión específica
PYTHON_VERSION=python3.11 ./setup.sh
```

#### Error: "No module named 'weasyprint'"

Reactiva el entorno virtual y reinstala las dependencias:
```bash
cd ejercicios-src/scripts
source ../../venv/bin/activate
pip install -r requirements.txt
```

#### Error: "Failed to load font"

En macOS, instala las fuentes del sistema:
```bash
brew install --cask font-noto-sans-cjk
```

#### PDFs no se generan correctamente

Verifica que los archivos markdown estén en la estructura correcta:
```bash
# Verificar estructura
ls -la ejercicios-src/markdown/unidad-1-ar-verbs/japanese/
ls -la ejercicios-src/markdown/unidad-1-ar-verbs/english/
```

### Desarrollo y contribución

Para contribuir al proyecto:

1. Crea una rama nueva para tu funcionalidad
2. Mantén la estructura multilingüe
3. Asegúrate de que los ejercicios en español sean idénticos en ambas versiones
4. Ejecuta las pruebas antes de enviar un pull request

### Soporte

Para reportar problemas o solicitar nuevas funcionalidades:
- Crea un issue en el repositorio de GitHub
- Incluye información sobre tu sistema operativo y versión de Python
- Proporciona el mensaje de error completo si es aplicable
