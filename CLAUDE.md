# Instrucciones para Claude Code - Cuadernillos de español

## Contexto del proyecto

Este repositorio contiene ejercicios de español para niños entre 7 y 16 años que reciben su educación en japonés. Niños que escuchan español en casa, tienen vocabulario amplio y usan gramática natural, pero necesitan estructura formal. Saben leer y escribir, aunque en español les resulta un poco difícil.

## Formato de los cuadernillos

- **Objetivo**: ejercicios para imprimir en DIN A5
- **Extensión**: 6 páginas por unidad
- **Tamaño del texto**: grande, máximo 12 líneas por página, máximo 10 palabras por línea
- **Formato**: markdown

## Estructura de archivos

Crear archivos separados para cada página con esta nomenclatura:

```
unidad-[N]/
├── pagina-1-dialogo.md
├── pagina-2-conjugacion-completar.md
├── pagina-3-eleccion.md
├── pagina-4-transformacion.md
├── pagina-5-ordenar.md
└── pagina-6-bien-mal.md
```

## Especificaciones por página

### Página 1: diálogo (pagina-1-dialogo.md)

- **Contenido**: diálogo contextualizado entre 2 personajes
- **Longitud**: 8-10 líneas de diálogo
- **Vocabulario**: simple y cotidiano, evitar palabras difíciles
- **Verbos de la unidad**: usar al menos 2 de los 4 verbos seleccionados
- **Otros verbos**: permitidos verbos básicos (ej: "haces" está bien)
- **Narrativa**: clara y fácil de seguir, situación familiar
- **Formato**: usar **Nombre:** para cada intervención

### Página 2: conjugación y completar (pagina-2-conjugacion-completar.md)

- **Tabla de conjugación**: un verbo representativo en formato tabla
- **Ejemplo**: una frase completa usando el verbo
- **Ejercicios**: 5 frases para completar con pronombres personales
- **Verbos**: usar los 4 verbos de la unidad, distribución equilibrada

### Página 3: elección (pagina-3-eleccion.md)

- **Contenido**: 6 frases de elección múltiple
- **Formato**: "sujeto [opción1 | opción2] resto de la frase"
- **Respuesta**: línea en blanco para escribir la frase completa
- **Sujetos**: usar nombres/sustantivos claros (no pronombres omitidos)

### Página 4: transformación (pagina-4-transformacion.md)

- **Transformaciones**: 4 ejercicios de cambio de persona
- **Preguntas y respuestas**: 2 ejercicios de diálogo
- **Formato**: "Yo verbo → Nosotros **\_\_\_**"

### Página 5: ordenar (pagina-5-ordenar.md)

- **Contenido**: 6 ejercicios de ordenar palabras
- **Formato línea 1**: "[palabra1 / palabra2 / palabra3 / palabra4 / palabra5]"
- **Formato línea 2**: traducción al japonés de la frase ordenada
- **Respuesta**: línea en blanco para escribir a mano la frase ordenada

### Página 6: bien / mal (pagina-6-bien-mal.md)

- **Contenido**: 6 frases para evaluar
- **Formato**: "frase. \_\_\_" (espacio para B/M)
- **Corrección**: "Corrección: **\_\_\_**" debajo de cada frase

## Verbos por unidad

### Unidad 1: Primera conjugación (-AR)

- dibujar, buscar, hablar, bailar

### Unidad 2: segunda conjugación (-ER)

- comer, leer, aprender, beber

### Unidad 3: tercera conjugación (-IR)

- vivir, escribir, abrir, subir

## Consideraciones importantes

1. **Evitar repetición excesiva**: conectar ejercicios sutilmente sin ser obvio
2. **Progresión de dificultad**: de exposición a producción activa
3. **Contextos familiares**: casa, escuela, familia, actividades cotidianas
4. **Vocabulario apropiado**: para niños de 7 a 16 años, evitar palabras complejas
5. **Verbos irregulares**: No conjugar verbos irregulares que sean parecidos a los que estamos estudiando (ej: evitar "juego", usar "jugar"; pero "soy" o "haces" están bien)
6. Los encabezados y enunciados deben estar en japonés, porque es difícil entender los enunciados en español
7. En los títulos y encabezados no se empiezan todas las palabras en mayúscula, sino normalmente solo la primera como en una frase normal

## Plantillas de encabezado

Cada archivo debe comenzar con:

```markdown
# [Título de la página]

## [Subtítulo si aplica]

[Contenido de la página]
```

## Tarea para Claude Code

Genera los 18 archivos markdown (6 páginas × 3 unidades) siguiendo estas especificaciones exactas. Usa los contenidos ya desarrollados en el directorio `./samples`.

Los contenidos ya desarrollados son válidos, pero adáptate a las nuevas reglas como "bien/mal" en vez de "verdadero/falso", o los encabezados y enunciados en japonés, o la inclusión de la traducción de la frase ordenada.
