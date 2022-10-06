from itertools import count
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

busca = 'weather nowcasting'

#Meu pczinho é lento por isso botei 5 sec de delay entre os carregamentos#

#entrar no site
cursor = webdriver.Firefox()
url = "https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php?"
cursor.get(url)


#esperar carregar -> clicar no botao de pesquisar -> escrever a palavra chave
cursor.implicitly_wait(10)
cursor.find_element(By.ID,"btn-busca-primo").send_keys(" "+ busca + Keys.ENTER)


#descer a tela ate a divisoria
time.sleep(5)
cursor.execute_script("window.scrollTo(0, 550)") 


#entrar na frame de dentro
cursor.switch_to.frame('busca_primo')


#clicar em selecionar 10 općoes
cursor.implicitly_wait(20)
quadrado = cursor.find_element(By.CLASS_NAME, 'md-container').click()


#clicar em selecionar 50
cursor.implicitly_wait(2)
cursor.find_element(By.ID, 'chooseTopMax').click()



#clicar nos 3 pontinhos
#element = WebDriverWait(cursor, 20).until(
#EC.element_to_be_clickable((By.CLASS_NAME, 'md-primoExplore-theme')))
#element.click()

time.sleep(10)
cursor.find_element(By.CLASS_NAME,"").click()


#clicar no Bibitex
cursor.implicitly_wait(2)
cursor.find_element(By.ID, 'BibTeXPushToButton').click()


#clicar no botao de codificaćao
cursor.implicitly_wait(2)
cursor.find_element(By.ID, 'select_886').click()


#clicar no UTF-8
cursor.implicitly_wait(1)
cursor.find_element(By.ID, 'select_option_892').click()


#GRANDIOSO DOWLOAD
cursor.implicitly_wait(2)
cursor.find_element(By.CLASS_NAME, 'button-with-icon button-large button-confirm md-button md-primoExplore-theme md-ink-ripple').click()


cursor.close()
''' 
Modelando ideia:
0)Aumentar o numero de artigos para 50
1)Usar selenium para pegar a url
2)Usar o Beautifulsoup para fazer lista de 'a'
3)Achar os 'a' especificos e extrair o href
4)Pegar a lista de nomes dos artigos correspondentes
5)Criar dicionario com nome do artigo e link (firula)
6)Mover para proxima pagina do site com Selenium
'''
