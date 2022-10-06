from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

busca = 'weather nowcasting'

#Meu pczinho é lento por isso botei 5 sec de delay entre os carregamentos#

#entrar no site
cursor = webdriver.Firefox()
url = "https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php?"
cursor.get(url)


#esperar carregar -> clicar no botao de pesquisar -> escrever a palavra chave
cursor.implicitly_wait(10)
cursor.find_element(By.ID,"btn-busca-primo").send_keys(" "+ busca + Keys.ENTER)
cursor.implicitly_wait(30)


#descer a tela ate a divisoria
time.sleep(20)
cursor.execute_script("window.scrollTo(0, 600)") 


#entrar na frame de dentro
cursor.switch_to.frame('busca_primo')


#clicar em selecionar 10 općoes
quadrado = cursor.find_element(By.CLASS_NAME, 'md-container')
cursor.implicitly_wait(4)
time.sleep(3)

#clicar em selecionar 50
cursor.find_element(By.ID, 'chooseTopMax').click()
cursor.implicitly_wait(3)


#clicar nos 3 pontinhos
cursor.find_element(By.CLASS_NAME, 'md-icon-button has-bottom-arrow md-button md-primoExplore-theme md-ink-ripple').click()
cursor.implicitly_wait(1)


#clicar no Bibitex
cursor.find_element(By.ID, 'BibTeXPushToButton').click()
cursor.implicitly_wait(2)


#clicar no botao de codificaćao
cursor.find_element(By.ID, 'select_886').click()
cursor.implicitly_wait(1)


#clicar no UTF-8
cursor.find_element(By.ID, 'select_option_892').click()
cursor.implicitly_wait(1)


#GRANDIOSO DOWLOAD
cursor.find_element(By.CLASS_NAME, 'button-with-icon button-large button-confirm md-button md-primoExplore-theme md-ink-ripple').click()
cursor.implicitly_wait(10)



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
