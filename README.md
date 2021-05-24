# webScrapping

En esta aplicación web utilizamos la técnica de webScrapping para extraer la información del precio de algún producto deseado
y luego con la API de Telegram programamos un Bot que nos avisa cuando un producto bajo de precio.

Esto lo hacemos gracias al WebScraping utilizando las siguientes librerias :

from bs4 import BeautifulSoup 
import requests
import time
import webbrowser
