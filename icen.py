from bs4 import BeautifulSoup
import requests

import pandas as pd
import seaborn as sbn # 2
import matplotlib.pyplot as plt
#-------------------------------------------
url = "http://met.igp.gob.pe/datos/icen.txt"

# Obtener el contenido
content = requests.get(url).content
print(content)

# extraer datos y convetir a lista

# plotear ICEN 
