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

