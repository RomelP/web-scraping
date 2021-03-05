# Cargando librerias 
from bs4 import BeautifulSoup
import requests
# importando la url
url = "http://met.igp.gob.pe/datos/icen.txt"
# Obtener el contenido
content = requests.get(url).content
content
