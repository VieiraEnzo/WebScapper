import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


''' 
Modelando ideia:

1) Para cada pagina
    2) Para cada artigo
        3)Titulo
        4)Descrićão DOI
'''

busca = 'weather nowcasting'

#entrar no site
driver = webdriver.Firefox()
url = "https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php?"
driver.get(url)


#esperar carregar -> clicar no botao de pesquisar -> escrever a palavra chave
driver.implicitly_wait(10)
driver.find_element(By.ID,"btn-busca-primo").send_keys(" "+ busca + Keys.ENTER)


#descer a tela ate a divisoria
time.sleep(5)
driver.execute_script("window.scrollTo(0, 550)") 


#entrar na frame de dentro
driver.switch_to.frame('busca_primo')

def buscar_dados_das_divs():
    pass

#busca as divs classe list-item-wrapper
driver.implicitly_wait(10)
resultados = driver.find_elements(By.CLASS_NAME, "list-item-wrapper")
for div in resultados:
    buscar_dados_das_divs(div)
    






#class = list-item-wrapper first-in-page 
# 8x class = list-item-wrapper
#list-item-wrapper last-item





'''
#clicar em selecionar 10 općoes
driver.implicitly_wait(20)
quadrado = driver.find_element(By.CLASS_NAME, 'md-container').click()


#clicar em selecionar 50
driver.implicitly_wait(2)
driver.find_element(By.ID, 'chooseTopMax').click()



#clicar nos 3 pontinhos
#element = WebDriverWait(cursor, 20).until(
#EC.element_to_be_clickable((By.CLASS_NAME, 'md-primoExplore-theme')))
#element.click()

time.sleep(10)
driver.find_element(By.CLASS_NAME,"").click()


#clicar no Bibitex
driver.implicitly_wait(2)
driver.find_element(By.ID, 'BibTeXPushToButton').click()


#clicar no botao de codificaćao
driver.implicitly_wait(2)
driver.find_element(By.ID, 'select_886').click()


#clicar no UTF-8
driver.implicitly_wait(1)
driver.find_element(By.ID, 'select_option_892').click()


#GRANDIOSO DOWLOAD
driver.implicitly_wait(2)
driver.find_element(By.CLASS_NAME, 'button-with-icon button-large button-confirm md-button md-primoExplore-theme md-ink-ripple').click()


driver.close()
'''
