# selenium-docker
# 🧪 Automatización con Selenium y Docker

Este proyecto demuestra cómo ejecutar pruebas web automatizadas utilizando Selenium dentro de un contenedor Docker.

El script de prueba en Python abre una página web, busca un elemento en el DOM y toma una captura de pantalla, todo desde un entorno aislado usando `selenium/standalone-chrome` y `docker-compose`.

- Inicia un contenedor con Chrome y Selenium.
- Ejecuta un script Python que:
  - Abre `https://example.com`
  - Extrae el título y un texto `<h1>`
  - Toma una captura de pantalla (`screenshot.png`)

Estructura del proyecto:

selenium-docker
  --> docker-compose.yml
   --> Dockerfile
   --> test_script.py
 

