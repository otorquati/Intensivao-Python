# Criar navegador controlado pelo Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
driver = webdriver.Edge()

# Passo 1 - Pegar a cotação do dólar

driver.get('https://google.com')

element = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
element.send_keys('Cotação Dolar')
element.submit()
element = driver.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input')
cotacao_dolar = element.get_attribute('value')
driver.quit()
print(cotacao_dolar)
#time.sleep(5)

# Passo 2 - Pegar a cotação do euro
driver = webdriver.Edge()
driver.get('https://google.com')
element = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
element.send_keys('Cotação Euro')
element.submit()
element = driver.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input')
#time.sleep(5)
cotacao_euro = element.get_attribute('value')
driver.quit()
print(cotacao_euro)
#time.sleep(5)
# Passo 3 - Pegar a cotação do ouro
driver = webdriver.Edge()
driver.get('https://www.melhorcambio.com/ouro-hoje')

element = driver.find_element('xpath', '//*[@id="comercial"]')
cotacao_ouro = element.get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',','.')
print(cotacao_ouro)

#time.sleep(5)
driver.quit()

# Passo 4 - Importar a base de dados e atualizar a base
tabela = pd.read_excel(r'C:\Users\Dj Thor\Meus Projetos\Intensivao-Python\Aula 3\Produtos.xlsx')
print(tabela)
# Passo 5 - Recalcular os preços
tabela.loc[tabela['Moeda'] =='Dólar','Cotação']= float(cotacao_dolar)
tabela.loc[tabela['Moeda'] =='Euro','Cotação']= float(cotacao_euro)
tabela.loc[tabela['Moeda'] =='Ouro','Cotação']= float(cotacao_ouro)
# Recalcular os preços
tabela['Preço de Compra']=tabela['Cotação']*tabela['Preço Original']
tabela['Preço de Venda']=tabela['Preço de Compra']*tabela['Margem']
# Passo 6 - Exportar a base atualizada
tabela.to_excel(r'C:\Users\Dj Thor\Meus Projetos\Intensivao-Python\Aula 3\Produtos_Update.xlsx',index=False)
print(tabela)
