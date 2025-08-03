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
