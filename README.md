# Script de Verificación SEO

Este script utiliza Selenium para realizar una serie de comprobaciones SEO en tu sitio web alojado en `hostingnet.cl`. Verifica varios elementos clave para asegurar un rendimiento óptimo en SEO.

## Funcionalidades

1. **Verificación de Título**: Comprueba si la página tiene un título y lo muestra.
2. **Meta Descripción**: Verifica la presencia de una meta descripción y la muestra.
3. **Atributos `alt` en Imágenes**: Asegura que todas las imágenes tengan atributos `alt` y señala las que no.
4. **Verificación de Nombre de Imagen**: Verifica que los nombres de las imágenes contengan al menos una palabra clave de la ruta URL.
5. **Enlaces Rotos**: Revisa todos los enlaces en la página e informa de cualquier enlace roto (código de estado HTTP 400 o superior).
6. **Enlaces Internos**: Confirma la presencia de al menos dos enlaces internos en el sitio.
7. **Análisis de Palabras Clave**: Cuenta las ocurrencias de palabras clave especificadas en el cuerpo de la página.
8. **Encabezados H1**: Lista todos los `H1` encontrados y verifica que la palabra de la ruta URL esté presente en al menos un `H1`.
9. **Favicon**: Comprueba la existencia de un favicon en el sitio.
10. **Tamaño de la Página**: Verifica el tamaño de la página y alerta si excede los 2 MB.

## Cómo Usar

1. **Clona el repositorio** y navega al directorio del proyecto.
2. **Instala las dependencias requeridas**:
   ```bash
   pip install selenium webdriver-manager requests
