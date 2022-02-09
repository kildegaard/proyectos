# Otra forma de hacerlo, veamos si parsea mejor

import requests
import pdfplumber
import pandas as pd


def download_file(url):
    local_filename = url.split('/')[-1]

    with requests.get(url) as r:
        with open(local_filename, 'wb') as f:
            f.write(r.content)

    return local_filename


# ap_url = 'https://www.tabs3.com/support/sample/apreports.pdf'
ap_url = 'https://www.argentina.gob.ar/sites/default/files/5-03-2020-nuevo-coronavirus-covid-19-reporte-diario_1.pdf'

ap = download_file(ap_url)

with pdfplumber.open(ap) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

print(text)
