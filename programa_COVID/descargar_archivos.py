import requests
from bs4 import BeautifulSoup

url = 'https://www.argentina.gob.ar/coronavirus/informes-diarios/reportes/marzo2020'

source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

articles = soup.find('div', class_='row row-flex')
for article in articles:
    article = article.find('a', class_='btn btn-primary btn-sm')
    url_file = article['href']
    file_name = url_file.split('/')[-1]

    r = requests.get(url_file, allow_redirects=True)
    with open(file_name, 'wb') as f:
        f.write(r.content)
