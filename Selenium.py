import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
RESULTADOS = 10
''' 
Modelando ideia:

1) Para cada pagina
    2) Para cada artigo
        3)Titulo
        4)Descrićão DOI
'''
artigos = {}
busca = 'weather nowcasting'

#entrar no site
driver = webdriver.Firefox()
url = "https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php?"
driver.get(url)


#esperar carregar -> clicar no botao de pesquisar -> escrever a palavra chave
driver.implicitly_wait(10)
driver.find_element(By.ID,"btn-busca-primo").send_keys(" "+ busca + Keys.ENTER)



contador_paginas = 1

while contador_paginas <= total_paginas:

    

    #descer a tela ate a divisoria
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 550)") 


    #entrar na frame de dentro
    driver.switch_to.frame('busca_primo')

    titulos = []
    links = []

    # xpath do frame de cada resultado
    n = 1
    while n <= RESULTADOS:


        inicio = "/html/body/primo-explore/div/prm-explore-main/ui-view/prm-search/div/md-content/div[1]/prm-search-result-list/div/div[1]/div/div["
        final = "]/prm-brief-result-container/div[1]/div[3]/prm-brief-result/h3/a/span/prm-highlight/span"
        xpath_titulo = inicio + str(n) + final

        driver.implicitly_wait(60)
        titulos.append(driver.find_element(By.XPATH, xpath_titulo).text)  #encontra div

        
        inicio = "/html/body/primo-explore/div/prm-explore-main/ui-view/prm-search/div/md-content/div[1]/prm-search-result-list/div/div[1]/div/div["
        final = "]/prm-brief-result-container/div[1]/div[3]/prm-brief-result/h3/a"
        xpath_link = inicio + str(n) + final

        driver.implicitly_wait(10)
        links.append(driver.find_element(By.XPATH, xpath_link).get_attribute("href")) #pegar os links
        
        n+=1

    doi = []
    descricao = []

    for link in links:

        driver.get(link)

        xpath_DOI = "/html/body/primo-explore/div/prm-full-view-page/prm-full-view-cont/md-content/div[2]/prm-full-view/div/div/div/div[1]/div/div[5]/div/prm-full-view-service-container/div[2]/div/prm-service-details/div/div"
        driver.implicitly_wait(20)
        resultado = driver.find_element(By.XPATH, xpath_DOI).find_elements(By.TAG_NAME,"span")

        
        for contador ,elemento in enumerate(resultado):

            if elemento.text == "Descrição":
                descricao.append(resultado[contador + 2].text)

            if "DOI" in elemento.text:
                doi.append(elemento.text)

    contador_paginas +=1

for i in range(RESULTADOS):
    artigos[doi[i]] = [titulos[i],descricao[i]]


driver.close()