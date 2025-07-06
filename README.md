# Cuadernillos de español para niños

Este repositorio contiene ejercicios de español diseñados especialmente para niños entre 7 y 16 años que reciben su educación en japonés pero hablan español en casa. Los materiales se enfocan en proporcionar estructura formal al conocimiento intuitivo del idioma que ya poseen los estudiantes.

## Descripción del proyecto

Los estudiantes objetivo de estos materiales:
- Escuchan español en casa y tienen vocabulario amplio
- Usan gramática natural pero necesitan estructura formal
- Saben leer y escribir, aunque en español les resulta un poco difícil
- Requieren práctica con conjugaciones verbales regulares

## Estructura del contenido

### Unidades disponibles

**Unidad 1: Primera conjugación (-AR)**
- Verbos: dibujar, buscar, hablar, bailar
- Enfoque en verbos regulares terminados en -ar

**Unidad 2: Segunda conjugación (-ER)**
- Verbos: comer, leer, aprender, beber
- Enfoque en verbos regulares terminados en -er

**Unidad 3: Tercera conjugación (-IR)**
- Verbos: vivir, escribir, abrir, subir
- Enfoque en verbos regulares terminados en -ir

### Estructura de cada unidad

Cada unidad contiene 6 páginas de ejercicios:

1. **Diálogo** - Conversación contextualizada entre personajes
2. **Conjugación y completar** - Tabla de conjugación y ejercicios de completar
3. **Elección múltiple** - Ejercicios de selección de la forma correcta
4. **Transformación** - Cambios de persona y ejercicios de preguntas/respuestas
5. **Ordenar palabras** - Construcción de oraciones a partir de palabras desordenadas
6. **Bien/Mal** - Corrección de oraciones incorrectas

## Formatos disponibles

### PDFs imprimibles
- Formato DIN A5 optimizado para impresión
- Texto grande y espacios amplios para escribir a mano
- Máximo 12 líneas por página, máximo 10 palabras por línea

### Versiones en diferentes idiomas
Los ejercicios están disponibles con instrucciones en:
- **Japonés** (日本語) - Para estudiantes en Japón
- **Inglés** (English) - Para estudiantes internacionales
- **Español** (Español) - Para profesores hispanohablantes

### Página web (GitHub Pages)
Acceso en línea a todos los ejercicios en formato HTML con descarga de PDFs.

## Instalación y uso

### Requisitos del sistema
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Configuración inicial

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/ejercicios-espanol.git
cd ejercicios-espanol
```

2. Configura el entorno virtual:
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

3. Activa el entorno virtual:
```bash
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate  # En Windows
```

### Generación completa

Para generar todos los materiales (PDFs y sitio web):
```bash
./scripts/build_all.sh
```

### Generación de PDFs

Para generar todos los PDFs en todos los idiomas:
```bash
python generators/generate_pdf_multilang.py --all-languages
```

Para generar PDFs de una unidad específica:
```bash
python generators/generate_pdf_multilang.py --unit 1 --language ja
```

Parámetros disponibles:
- `--unit`: Número de unidad (1, 2, 3)
- `--language`: Código de idioma (ja, en, es)
- `--output`: Directorio de salida (por defecto: output/pdfs/)
- `--all-languages`: Generar en todos los idiomas

### Generación de sitio web

Para generar el sitio web GitHub Pages:
```bash
python generators/generate_html.py
```

Para vista previa local:
```bash
python generators/generate_html.py --preview
cd docs && python -m http.server 8000
```

### Estructura de directorios

```
ejercicios-espanol/
├── content/                    # Contenido principal
│   ├── units/                  # Ejercicios por unidad
│   │   ├── unit-1/            # Unidad 1: verbos -AR
│   │   ├── unit-2/            # Unidad 2: verbos -ER
│   │   └── unit-3/            # Unidad 3: verbos -IR
│   └── translations/          # Traducciones de instrucciones
│       ├── ja.yaml            # Japonés
│       ├── en.yaml            # Inglés
│       └── es.yaml            # Español
├── generators/                # Herramientas de generación
│   ├── generate_pdf.py        # Generador de PDFs
│   └── generate_html.py       # Generador para web
├── output/                    # Archivos generados
│   ├── pdfs/                  # PDFs por idioma
│   └── html/                  # Archivos HTML
├── docs/                      # Sitio web GitHub Pages
├── scripts/                   # Scripts de configuración
└── legacy/                    # Archivos de versiones anteriores
```

## Desarrollo y contribución

### Añadir nuevo contenido

1. **Nuevas unidades**: Crea un directorio `unit-N` en `content/units/`
2. **Traducciones**: Añade entradas a los archivos YAML en `content/translations/`
3. **Ejercicios**: Sigue la estructura de 6 páginas por unidad

### Formato de archivos

- **Contenido**: Markdown (.md)
- **Metadatos**: YAML (.yaml)
- **Configuración**: Python (.py)

### Comandos de desarrollo

Verificar formato de archivos:
```bash
python scripts/validate_content.py
```

Generar vista previa:
```bash
python generators/generate_html.py --preview
```

Ejecutar tests:
```bash
python -m pytest tests/
```

## Características pedagógicas

### Progresión del aprendizaje

1. **Exposición** (Página 1) - Diálogo natural con verbos en contexto
2. **Reconocimiento** (Página 2) - Tabla de conjugación y ejemplos
3. **Selección** (Página 3) - Elección entre formas correctas e incorrectas
4. **Transformación** (Página 4) - Cambio activo de formas verbales
5. **Construcción** (Página 5) - Formación de oraciones completas
6. **Corrección** (Página 6) - Identificación y corrección de errores

### Principios de diseño

- **Contextos familiares**: Casa, escuela, familia, actividades cotidianas
- **Vocabulario apropiado**: Adaptado a niños de 7-16 años
- **Progresión gradual**: De exposición pasiva a producción activa
- **Práctica variada**: Diferentes tipos de ejercicios para reforzar el aprendizaje

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto y soporte

Para preguntas, sugerencias o reportar problemas:
- Abre un issue en este repositorio
- Consulta la documentación en la página web del proyecto

## Agradecimientos

Este proyecto fue desarrollado para apoyar a familias hispanohablantes en Japón y otros países donde el español es lengua minoritaria en el hogar.
