from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from urllib.parse import urlparse

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL de tu sitio
url = 'https://www.hostingnet.cl/web-hosting'

# Función para verificar elementos SEO
def check_seo_elements(url):
    driver.get(url)

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

    # Verificar etiquetas alt en imágenes
    images = driver.find_elements(By.TAG_NAME, 'img')
    for img in images:
        alt_text = img.get_attribute('alt')
        if alt_text:
            print(f"Etiqueta alt encontrada: {alt_text}")
        else:
            print(f"Imagen sin etiqueta alt: {img.get_attribute('src')}")

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
    path_word = urlparse(url).path.strip('/').split('/')[-1]
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

    print("Verificación SEO completa.")

# Ejecutar la verificación
check_seo_elements(url)

# Cerrar el navegador
driver.quit()
