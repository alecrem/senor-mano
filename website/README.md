# Sitio Web - Cuadernillos de Español

Sitio web en Remix.js para facilitar el acceso y descarga de los cuadernillos de español en formato PDF.

## Características

- **Interfaz en español** - Diseñado para padres y tutores que manejan español
- **Descarga directa** - Acceso inmediato a PDFs organizados por idioma de instrucciones
- **Responsive** - Funciona perfectamente en móviles y desktop
- **Optimizado** - Carga rápida y experiencia de usuario fluida

## Estructura

- **Página principal** (`/`) - Información del proyecto y tarjetas de cuadernillos con descarga directa
- **Página de descargas** (`/descargas`) - Vista completa de todos los PDFs disponibles

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

### Generar PDFs

Los PDFs se generan automáticamente desde el directorio raíz del proyecto:

```bash
# Desde la raíz del proyecto
./generate_pdfs.sh -l both
```

Esto creará los PDFs tanto en `pdf-output/` como en `website/public/pdfs/` para que estén disponibles en el sitio web.

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
│   │   ├── Layout.tsx          # Layout principal con header/footer
│   │   └── CuadernilloCard.tsx # Tarjeta de cuadernillo con botones de descarga
│   ├── routes/
│   │   ├── _index.tsx          # Página principal
│   │   └── descargas.tsx       # Página de descargas
│   ├── styles/
│   │   └── global.css          # Estilos CSS globales
│   └── root.tsx                # Componente raíz de la app
├── public/
│   └── pdfs/                   # PDFs servidos estáticamente
│       ├── japanese/
│       └── english/
├── package.json
├── remix.config.js
├── vercel.json                 # Configuración de deployment
└── README.md
```

## Notas técnicas

- Los PDFs se sirven estáticamente desde `public/pdfs/`
- La generación de PDFs actualiza automáticamente los archivos del sitio web
- El CSS está optimizado para accesibilidad y responsive design
- Las meta tags están configuradas para SEO básico