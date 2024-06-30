# Script de Verificación SEO

Este script utiliza Selenium para realizar una serie de comprobaciones SEO, son básicas, pero de mucha utilidad cuando se sube un nuevo artículo o un nuevo producto a tu tienda ecommerce. Básicamente, verifica varios elementos que son iniciales, pero claves, para asegurar un rendimiento óptimo en SEO. Al ejecutar el script se utilizan muy pocos recusos del servidor, es prácticamente despreciable.

## Funcionalidades

1. **Tiempo de Carga del Servidor**: Mide el tiempo que tarda el servidor en responder.
2. **Verificación de Título**: Comprueba si la página tiene un título y lo muestra.
3. **Meta Descripción**: Verifica la presencia de una meta descripción y la muestra.
4. **Atributos `alt` en Imágenes**: Asegura que todas las imágenes tengan atributos `alt` y señala las que no.
5. **Verificación de Nombre de Imagen**: Verifica que los nombres de las imágenes contengan al menos una palabra clave de la ruta URL.
6. **Tamaño de Imágenes**: Informa si alguna imagen pesa más de 1 MB.
7. **Conteo de Imágenes SVG**: Cuenta cuántas imágenes en formato SVG hay en la página.
8. **Enlaces Rotos**: Revisa todos los enlaces en la página e informa de cualquier enlace roto (código de estado HTTP 400 o superior).
9. **Enlaces Internos**: Confirma la presencia de al menos dos enlaces internos en el sitio.
10. **Análisis de Palabras Clave**: Cuenta las ocurrencias de palabras clave especificadas en el cuerpo de la página.
11. **Encabezados H1**: Lista todos los `H1` encontrados y verifica que la palabra de la ruta URL esté presente en al menos un `H1`.
12. **Favicon**: Comprueba la existencia de un favicon en el sitio.
13. **Tamaño de la Página**: Verifica el tamaño de la página y alerta si excede los 2 MB.

## Cómo Usar

1. **Clona el repositorio** y navega al directorio del proyecto.
2. **Instala las dependencias requeridas**:
   ```bash
   pip install selenium webdriver-manager requests
