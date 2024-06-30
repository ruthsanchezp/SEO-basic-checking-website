from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from urllib.parse import urlparse
import time

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL de tu sitio
url = 'https://www.tusitio.com/palabra'

# Función para verificar elementos SEO
def check_seo_elements(url):
    start_time = time.time()
    driver.get(url)
    load_time = time.time() - start_time

    print(f"Tiempo de carga del servidor: {load_time:.2f} segundos")

    # Verificar el título
    title = driver.title
    if title:
        print(f"Título encontrado: {title}")
    else:
        print("No se encontró título.")

    # Verificar meta descripción
    try:
        meta_description = driver.find_element(By.NAME, 'description').get_attribute('content')
        if meta_description:
            print(f"Meta descripción encontrada: {meta_description}")
        else:
            print("No se encontró meta descripción.")
    except:
        print("No se encontró meta descripción.")

    # Verificar etiquetas alt en imágenes y nombres de archivo
    path_word = urlparse(url).path.strip('/').split('/')[-1]
    images = driver.find_elements(By.TAG_NAME, 'img')
    svg_count = 0

    for img in images:
        alt_text = img.get_attribute('alt')
        src = img.get_attribute('src')

        if alt_text:
            print(f"Etiqueta alt encontrada: {alt_text}")
        else:
            print(f"Imagen sin etiqueta alt: {src}")

        if path_word.lower() in src.lower():
            print(f"Nombre de imagen contiene la palabra de la URL: {src}")
        else:
            print(f"Nombre de imagen no contiene la palabra de la URL: {src}")

        if src.endswith('.svg'):
            svg_count += 1
        else:
            try:
                img_response = requests.head(src, allow_redirects=True)
                img_size_kb = int(img_response.headers.get('Content-Length', 0)) / 1024
                if img_size_kb > 1024:
                    print(f"Advertencia: La imagen {src} pesa {img_size_kb:.2f} KB, excede 1 MB.")
            except requests.RequestException as e:
                print(f"Error al verificar la imagen: {src} ({e})")

    print(f"Se encontraron {svg_count} imágenes SVG.")

    # Verificar enlaces rotos
    links = driver.find_elements(By.TAG_NAME, 'a')
    internal_links = 0
    for link in links:
        href = link.get_attribute('href')
        if href and href.startswith('http'):
            if url in href:
                internal_links += 1
            try:
                response = requests.head(href, allow_redirects=True)
                if response.status_code >= 400:
                    print(f"Enlace roto encontrado: {href} (Status: {response.status_code})")
            except requests.RequestException as e:
                print(f"Error al verificar enlace: {href} ({e})")

    # Verificar que haya al menos dos enlaces internos
    if internal_links >= 2:
        print(f"Se encontraron {internal_links} enlaces internos.")
    else:
        print("No se encontraron al menos 2 enlaces internos.")

    # Análisis básico de palabras clave
    body_text = driver.find_element(By.TAG_NAME, 'body').text
    keywords = ['tu-palabra-clave1', 'tu-palabra-clave2']
    for keyword in keywords:
        count = body_text.lower().count(keyword.lower())
        print(f"La palabra clave '{keyword}' aparece {count} veces.")

    # Verificar encabezados H1
    h1_tags = driver.find_elements(By.TAG_NAME, 'h1')
    h1_found = False
    for h1 in h1_tags:
        print(f"Encabezado H1 encontrado: {h1.text}")
        if path_word.lower() in h1.text.lower():
            h1_found = True
    
    if h1_found:
        print(f"La palabra '{path_word}' de la URL está presente en el H1.")
    else:
        print(f"La palabra '{path_word}' de la URL no se encontró en el H1.")

    # Verificar la presencia de un favicon
    try:
        favicon = driver.find_element(By.XPATH, "//link[@rel='icon']")
        print(f"Favicon encontrado: {favicon.get_attribute('href')}")
    except:
        print("No se encontró favicon.")

    # Verificar el tamaño de la página
    page_source = driver.page_source
    page_size_kb = len(page_source.encode('utf-8')) / 1024
    if page_size_kb > 2048:
        print(f"Advertencia: El tamaño de la página es {page_size_kb:.2f} KB, lo que excede los 2 MB.")
    else:
        print(f"El tamaño de la página es {page_size_kb:.2f} KB.")

    print("Verificación SEO completa.")

# Ejecutar la verificación
check_seo_elements(url)

# Cerrar el navegador
driver.quit()
