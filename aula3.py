
from selenium import webdriver
from selenium import webdriver
import webbrowser
import pyautogui
import time
import numpy
import openpyxl
from selenium.webdriver.common.by import By
# Classe de espera
from selenium.webdriver.support.ui import WebDriverWait
# Classe de condição 
from selenium.webdriver.support import expected_conditions as EC
navegador = webdriver.Chrome('https://www.google.com/')
navegador.get('https://www.google.com/')
#navegador.find_element(By.XPATH,'//*[@id="hplogo"]').click()
#WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hplogo"]')))
#navegador.find_element_by_xpath().click()
import pandas as pd
tabela = pd.read_excel(r'C:\Users\marco\OneDrive\Área de Trabalho\studiespython\aula3\commodities.xlsx')
print(tabela)
for linha in tabela.index:
    produto= tabela.loc[linha,'Produto']
    produto=produto.replace('ó','o').replace('ã','a').replace('é','e').replace('í','i').replace('ú','u').replace('ç','c').replace('á','a')
    link=f'https://www.melhorcambio.com/{produto}-hoje'
    navegador.get(link)
    preco=navegador.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute('value')
    preco=preco.replace('.','').replace(',','.')
    WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="comercial"]')))
    tabela.loc[linha,'Preço Atual']=float(preco)
    tabela['Comprar']= tabela['Preço Atual'] < tabela['Preço Ideal']
print(tabela)
tabela.to_excel('commodities.xlsx',index=False)
