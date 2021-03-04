from bs4 import BeautifulSoup
import requests

url = "http://met.igp.gob.pe/datos/icen.txt"

# Obtener el contenido
content = requests.get(url).content
print(content)
# extrae datos y convetir a lista 
