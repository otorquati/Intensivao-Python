# Criar navegador controlado pelo Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

# Passo 1 - Pegar a cotação do dólar

driver.get('https://google.com')

element = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
element.send_keys('Cotação Dolar')
element.submit()
element = driver.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input')
cotacao_dolar = element.get_attribute('value')
driver.quit()
print('Cotação do dolar: {}'.format(cotacao_dolar))
#time.sleep(5)
driver.quit()

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
print('Cotação Euro: {}'.format(cotacao_euro,'.2%f'))
time.sleep(5)
# Passo 3 - Pegar a cotação do ouro
driver = webdriver.Edge()
driver.get('https://www.melhorcambio.com/ouro-hoje')

element = driver.find_element('xpath', '//*[@id="comercial"]')
cotacao_ouro = element.get_attribute('value')
print('Cotação Ouro: {}'.format(cotacao_ouro,'.2%f'))

#time.sleep(5)
driver.quit()

# Passo 4 - Importar a base de dados e atualizar a base

# Passo 5 - Recalcular os preços

# Passo 6 - Exportar a base atualizada

