import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select #dropdown
import pandas as pd
from time import sleep

# Abrir Navegador
PATH = 'C:\Program Files (x86)\chromedriver.exe'
nav = webdriver.Chrome(PATH)
nav.get('https://...')
print(nav.title)


# # LOGIN
## user name
elemento = nav.find_element(By.ID, 'userid')
elemento.clear()
elemento.send_keys('')

## password
elemento = nav.find_element(By.ID, 'password')
elemento.clear()
elemento.send_keys('')

## enter
nav.find_element(By.ID, 'btnActive').send_keys(Keys.RETURN)

time.sleep(5)

# NAVEGACAO PARA AREA DE RISCO
##esperar página carregar
## Clicar em Risk Management
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.ID, 'groupNode_risk_management'))).click()
except: 
	print('erro 1')

## esperar página carregar
## Clicar em Risk Management
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.LINK_TEXT, 'Risks'))).click()
except: 
	print('erro 2')

time.sleep(5)

# # Clicar na caixa de erro, se ela aparecer
# caixaErro  = nav.find_element(By.iD , 'd1::msgDlg::cancel')).is_displayed()
# print(caixaErro) 
# if caixaErro == True:
# 	nav.find_element(By.ID, 'd1::msgDlg::cancel').click()

## Clicar na maleta do menu lateral
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_risks:0:_FOTsdi__GRC_RISKMANAGEMENT_itemNode::disAcr'))
	).click()
except: 
	print('erro 3')

time.sleep(5)

## Fluxo de escolher o risco
# Rodar Linha por Linha
# table_id = nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_risks:0:_FOTr1:1:up1:UPsp1:ls1:AT1:_ATp:ATt1')
table_id = nav.find_element(By.TAG_NAME, 'tbody')
rows = table_id.find_elements(By.TAG_NAME, 'tr') 

for row in rows:
    # Get the columns (all the column 2)        
    col = row.find_elements(By.TAG_NAME, 'td')[3] # coluna status
    print(col.text) #prints text from the element

