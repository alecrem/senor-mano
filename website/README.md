# Sitio Web - Cuadernillos de Español

Sitio web en Remix.js para facilitar el acceso y descarga de los cuadernillos de español en formato PDF.

## Características

- **Interfaz en español** - Diseñado para padres y tutores que manejan español
- **Vista previa web** - Permite ver el contenido completo de los cuadernillos antes de descargar
- **Descarga directa** - Acceso inmediato a PDFs organizados por idioma de instrucciones
- **Responsive** - Funciona perfectamente en móviles y desktop
- **Optimizado** - Carga rápida y experiencia de usuario fluida

## Estructura

- **Página principal** (`/`) - Información del proyecto, vista previa y descarga de cuadernillos
- **Páginas de vista previa** (`/preview/[tense]/[cuadernillo]/[language]`) - Vista completa del contenido de ejercicios

## Desarrollo

### Requisitos

- Node.js 18+
- pnpm

### Instalación

```bash
cd website
pnpm install
```

### Desarrollo local

```bash
pnpm dev
```

El sitio estará disponible en `http://localhost:3000`

### Generar PDFs y datos de vista previa

Los PDFs y los datos de vista previa se generan automáticamente desde el directorio raíz del proyecto:

```bash
# Desde la raíz del proyecto
./generate_pdfs.sh
```

Esto creará:
- PDFs en `website/public/pdfs/` para descarga
- Archivos markdown en `website/app/data/markdown/` para vistas previas web

### Build de producción

```bash
pnpm build
pnpm start
```

## Deployment

El sitio está configurado para desplegarse en Vercel:

1. Conecta el repositorio a Vercel
2. Configura el directorio raíz como `website/`
3. Vercel detectará automáticamente la configuración de Remix

### Variables de entorno

No se requieren variables de entorno para el funcionamiento básico.

## Estructura de archivos

```
website/
├── app/
│   ├── components/
│   │   ├── Layout.tsx              # Layout principal con header/footer
│   │   ├── CuadernilloCard.tsx     # Tarjeta de cuadernillo con botones
│   │   ├── DialoguePreview.tsx     # Componente de vista previa de diálogos
│   │   ├── ConjugationPreview.tsx  # Componente de vista previa de conjugaciones
│   │   ├── ChoicePreview.tsx       # Componente de vista previa de elección múltiple
│   │   ├── TransformationPreview.tsx # Componente de vista previa de transformaciones
│   │   ├── OrderingPreview.tsx     # Componente de vista previa de ordenamiento
│   │   └── EvaluationPreview.tsx   # Componente de vista previa de evaluación
│   ├── data/
│   │   └── markdown/               # Archivos markdown para vistas previas
│   │       ├── present-tense/
│   │       └── past-tense/
│   ├── routes/
│   │   ├── _index.tsx              # Página principal
│   │   └── preview.$tense.$cuadernillo.$language.tsx # Rutas dinámicas de vista previa
│   ├── styles/
│   └── root.tsx                    # Componente raíz de la app
├── public/
│   └── pdfs/                       # PDFs servidos estáticamente
│       ├── japanese/
│       └── english/
├── copy-markdown.js                # Script para copiar archivos markdown
├── package.json
└── README.md
```

## Notas técnicas

- Los PDFs se sirven estáticamente desde `public/pdfs/`
- Los datos de vista previa se cargan desde `app/data/markdown/`
- La generación de PDFs actualiza automáticamente tanto PDFs como datos de vista previa
- El sistema de vista previa convierte placeholders markdown a elementos web interactivos
- El CSS está optimizado para accesibilidad y responsive design
- Las meta tags están configuradas para SEO básico
- Las rutas de vista previa son dinámicas y soportan todos los cuadernillos, tiempos e idiomas