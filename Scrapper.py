from email import parser
from bs4 import BeautifulSoup
import requests

url = 'https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php/buscador-primo.html'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
list = soup.find_all('a')
print(list)

'''
Passo 1: Codigo pegar todos os resultados e links
-> selenium para aumentar para 50?
Passo 2: Navegar pelas paginas até chegar na ultima
PROBLEMA: url dinamica do site, ao pesquisar não se gera uma url 
diferente mas de alguma maneira o html dentro muda, logo
Beautiful soup não vai tankar fazer isso (será)

'''
