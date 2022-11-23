import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
RESULTADOS = 10


artigos = {}
titulos = []
links = []
busca = 'weather nowcasting'

#entrar no site
driver = webdriver.Firefox()
url = "https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php?"
driver.get(url)


#esperar carregar -> clicar no botao de pesquisar -> escrever a palavra chave
driver.implicitly_wait(10)
driver.find_element(By.ID,"btn-busca-primo").send_keys(" "+ busca + Keys.ENTER)
    

#Entra em cada uma das paginas para pegar os links
var = True
while var:

    try:
        try:
            driver.switch_to.frame('busca_primo')
        except:
            pass
        
        n = 1
        while n <= RESULTADOS:

            #pega o titulo adicionando na lista titulos
            inicio = "/html/body/primo-explore/div/prm-explore-main/ui-view/prm-search/div/md-content/div[1]/prm-search-result-list/div/div[1]/div/div["
            final = "]/prm-brief-result-container/div[1]/div[3]/prm-brief-result/h3/a/span/prm-highlight/span"
            xpath_titulo = inicio + str(n) + final

            driver.implicitly_wait(60)
            titulos.append(driver.find_element(By.XPATH, xpath_titulo).text)  #encontra div

            #pega o link adicionando na lista links
            inicio = "/html/body/primo-explore/div/prm-explore-main/ui-view/prm-search/div/md-content/div[1]/prm-search-result-list/div/div[1]/div/div["
            final = "]/prm-brief-result-container/div[1]/div[3]/prm-brief-result/h3/a"
            xpath_link = inicio + str(n) + final

            driver.implicitly_wait(10)
            links.append(driver.find_element(By.XPATH, xpath_link).get_attribute("href")) #pegar os links
            
            n+=1

        
        #clicar no botão de proxima pagina
        xpath_troca_pagina = "/html/body/primo-explore/div/prm-explore-main/ui-view/prm-search/div/md-content/div[1]/prm-search-result-list/div/div[1]/prm-page-nav-menu/div/div/div[1]/div[3]/a"
        driver.implicitly_wait(20)
        element = driver.find_element(By.XPATH, xpath_troca_pagina)
        element.location_once_scrolled_into_view
        element.click()

    except:
        var = False

doi = []
descricao = []

#A partir de uma lista de links, pega o DOI e a descricao dos sites e adiciona na lista
for link in links:

    driver.get(link)
    #Pega os spans do site
    xpath_DOI = "/html/body/primo-explore/div/prm-full-view-page/prm-full-view-cont/md-content/div[2]/prm-full-view/div/div/div/div[1]/div/div[5]/div/prm-full-view-service-container/div[2]/div/prm-service-details/div/div"
    driver.implicitly_wait(20)
    resultado = driver.find_element(By.XPATH, xpath_DOI).find_elements(By.TAG_NAME,"span")

    #dentro da lista de spans localiza que tem DOI e a descricao
    for contador ,elemento in enumerate(resultado):

        if elemento.text == "Descrição":
            descricao.append(resultado[contador + 2].text)

        if "DOI" in elemento.text:
            doi.append(elemento.text)


#Adiciona dentro do dicionario
for i in range(RESULTADOS):
    artigos[doi[i]] = [titulos[i],descricao[i]]


driver.close()

with open("artigos.json", "w") as outfile:
    json.dump(artigos, outfile)
    
