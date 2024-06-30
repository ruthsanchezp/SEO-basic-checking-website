# Script de Verificación SEO

Este script utiliza Selenium para realizar una serie de comprobaciones SEO en tu sitio web alojado en `hostingnet.cl`. Verifica varios elementos clave para asegurar un rendimiento óptimo en SEO.

## Funcionalidades

1. **Verificación de Título**: Comprueba si la página tiene un título y lo muestra.
2. **Meta Descripción**: Verifica la presencia de una meta descripción y la muestra.
3. **Atributos `alt` en Imágenes**: Asegura que todas las imágenes tengan atributos `alt` y señala las que no.
4. **Verificación de Nombre de Imagen**: Verifica que los nombres de las imágenes contengan al menos una palabra clave de la ruta URL.
5. **Tamaño de Imágenes**: Informa si alguna imagen pesa más de 1 MB.
6. **Conteo de Imágenes SVG**: Cuenta cuántas imágenes en formato SVG hay en la página.
7. **Enlaces Rotos**: Revisa todos los enlaces en la página e informa de cualquier enlace roto (código de estado HTTP 400 o superior).
8. **Enlaces Internos**: Confirma la presencia de al menos dos enlaces internos en el sitio.
9. **Análisis de Palabras Clave**: Cuenta las ocurrencias de palabras clave especificadas en el cuerpo de la página.
10. **Encabezados H1**: Lista todos los `H1` encontrados y verifica que la palabra de la ruta URL esté presente en al menos un `H1`.
11. **Favicon**: Comprueba la existencia de un favicon en el sitio.
12. **Tamaño de la Página**: Verifica el tamaño de la página y alerta si excede los 2 MB.
13. **Verificación de Videos**: Busca videos en la página, permite especificar la extensión, y alerta si el video excede los 15 MB.

## Cómo Usar

1. **Clona el repositorio** y navega al directorio del proyecto.
2. **Instala las dependencias requeridas**:
   ```bash
   pip install selenium webdriver-manager requests
