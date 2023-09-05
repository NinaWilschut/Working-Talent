print('Start van de scraping applicatie')

from bs4 import BeautifulSoup
import requests as rq

pagina = rq.get('https://www.bitcoinmeester.nl/')

helehtml = BeautifulSoup(pagina.content, 'html.parser')

table = helehtml.find('tbody')
print(table.prettify())
