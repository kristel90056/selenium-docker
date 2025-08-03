<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configurar opciones del navegador
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Conectarse al contenedor Selenium
driver = webdriver.Remote(
    command_executor='http://selenium-chrome:4444/wd/hub',
    options=options
)

try:
    driver.get("https://example.com")
    time.sleep(2)  # Espera para que cargue
    title = driver.title
    print("Título de la página:", title)

    # Buscar un texto por etiqueta
    elem = driver.find_element(By.TAG_NAME, "h1")
    print("Texto encontrado:", elem.text)

    # Tomar una captura de pantalla
    driver.save_screenshot("screenshot.png")

finally:
    driver.quit()
=======
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

for attempt in range(10):
    try:
        driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            options=chrome_options
        )
        break
    except Exception as e:
        print(f"Esperando a Selenium... ({attempt + 1}/10)")
        time.sleep(2)
else:
    raise Exception("No se pudo conectar con Selenium")

driver.get("https://www.google.com")
time.sleep(2)

element = driver.find_element(By.NAME, "q")
print("Elemento encontrado:", element.tag_name)

driver.save_screenshot("/tmp/resultado.png")
driver.quit()

>>>>>>> 503b3d935c39c18c2f8a4141f125437b27bbdbfa
