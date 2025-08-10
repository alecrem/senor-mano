# Cuadernillos de español

Ejercicios de español para niños que reciben su educación principalmente en japonés o inglés. Niños que van a la escuela en japonés o inglés, pero saben bastante español porque lo escuchan en casa. Niños que saben leer y escribir en japonés o inglés pero en español todavía es un poco difícil para ellos.

## 🌐 Sitio web

**[Acceso directo a los cuadernillos](website/)** - Sitio web en español para facilitar la descarga de PDFs sin necesidad de conocimientos técnicos.

El sitio web incluye:

- Descripción completa del proyecto en español
- Descarga directa de todos los PDFs organizados por idioma de instrucciones
- Interfaz responsive optimizada para móviles y escritorio
- Información detallada sobre cómo usar los cuadernillos

## Estructura del proyecto

El proyecto contiene ejercicios de español organizados por unidades y cuadernillos.

### Estructura del repositorio

```
ejercicios-src/
├── assets/                # Recursos (logos, imágenes)
├── markdown/              # Archivos fuente organizados por unidad
│   ├── present-tense/     # Ejercicios de tiempo presente
│   ├── past-tense/        # Ejercicios de tiempo pasado
│   └── [otras-unidades]/  # Unidades adicionales
│       └── cuadernillo-[N]-[tipo]-verbs/
│           ├── cuadernillo.yaml  # Metadatos del cuadernillo
│           ├── japanese/         # Páginas con instrucciones en japonés
│           └── english/          # Páginas con instrucciones en inglés
└── scripts/               # Herramientas de generación de PDF

website/                   # Sitio web para acceso fácil
├── app/                   # Aplicación web
│   ├── components/        # Componentes React
│   ├── data/              # Datos copiados para preview web
│   └── routes/            # Páginas del sitio
└── public/pdfs/          # PDFs generados
    ├── japanese/
    └── english/
```

**Nota**: Los ejercicios de español son idénticos en ambas versiones (japonés, inglés), solo cambian las instrucciones y encabezados.

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

```bash
./generate_pdfs.sh
```

### Archivos generados

Los PDFs se generan en formato DIN A5 (148 × 210 mm) optimizado para niños:

- **Ubicación**: Directorio `website/public/pdfs/`
- **Nombres**:
  - Japonés: `cuadernillo-1-present-tense-ja.pdf`, etc.
  - Inglés: `cuadernillo-1-present-tense-en.pdf`, etc.
- **Formato**: A5 con texto grande y espaciado amplio
- **Contenido**: 6 páginas por cuadernillo (diálogo, conjugación, elección, transformación, ordenar, corrección)
- **Idiomas**: Los ejercicios en español son idénticos, solo cambian las instrucciones y encabezados

### Estructura de cada cuadernillo

Cada PDF contiene 6 páginas. Típicamente:

1. **Página 1 - Diálogo**: Conversación contextualizada usando los verbos del cuadernillo
2. **Página 2 - Conjugación**: Tabla de conjugación y ejercicios de completar
3. **Página 3 - Elección**: Ejercicios de opción múltiple
4. **Página 4 - Transformación**: Cambios de persona y preguntas-respuestas
5. **Página 5 - Ordenar**: Ejercicios de ordenamiento de palabras con traducción
6. **Página 6 - Corrección**: Ejercicios de identificar errores y corregir

### Personalización

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
ls -la ejercicios-src/markdown/cuadernillo-1-ar-verbs/japanese/
ls -la ejercicios-src/markdown/cuadernillo-1-ar-verbs/english/
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

## Licencias

Este proyecto utiliza un sistema de doble licencia:

### Software (MIT License)

Los componentes de software (generador de PDFs, sitio web, scripts de construcción) están licenciados bajo la **MIT License**. Esto incluye:

- Scripts de generación de PDF (`ejercicios-src/scripts/`)
- Código del sitio web (`website/`)
- Archivos de configuración (`package.json`, `tsconfig.json`, etc.)
- Scripts de configuración y despliegue

Ver [LICENSE](LICENSE) para más detalles.

### Contenido educativo (CC BY-SA 4.0)

Los materiales educativos están licenciados bajo **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. Esto incluye:

- Todos los ejercicios de español (`ejercicios-src/markdown/`)
- Ilustraciones y materiales visuales
- PDFs generados (obras derivadas del contenido educativo)
- Documentación de metodología educativa

Ver [LICENSE-CC-BY-SA-4.0](LICENSE-CC-BY-SA-4.0) para más detalles.

Esta estructura permite el uso libre del software técnico mientras garantiza que las mejoras al contenido educativo se compartan con la comunidad.
