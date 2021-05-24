from bs4 import BeautifulSoup

import requests
import time
import webbrowser

precioDeseado = int(input("¿Cual es su precio deseado?: "))
print("Accediendo a la web..")
time.sleep(2)
print("Verificando el precio..")
time.sleep(2)
print("Aguarde por favor...")
time.sleep(1)



url = requests.get("https://www.mercadolibre.com.ar/procesador-amd-ryzen-5-5600x-100-100000065box-de-6-nucleos-y-46ghz-de-frecuencia/p/MLA16328466?pdp_filters=category:MLA1648#searchVariation=MLA16328466&position=2&search_layout=stack&type=product&tracking_id=e980ae62-39a7-4116-bf59-821b67fd970d")


soup = BeautifulSoup(url.content, "html.parser")

resultado = soup.find("span", {"class":"price-tag-fraction"})

precioInicio_text = resultado.text

precioInicial = float(precioInicio_text)

precioDeseado = precioDeseado


if precioInicial < precioDeseado:
    print("Hay oferta")
else:
    print("No hay oferta")
