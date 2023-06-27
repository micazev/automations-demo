import time
from numpy import column_stack
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select #dropdown
import pandas as pd
from time import sleep


# importar/visualizar a base de dados
tabela_remediation = pd.read_excel('3_Input_RemediationPlanCreation.xlsx')
# print(tabela_remediation)


# get first row
# do the navigation

for row in tabela_remediation:
    # Navegação
    print(tabela_remediation['Remediation Plan Name'])
tabela_remediation['Remediation Plan Name']
tabela_remediation['Description']
tabela_remediation['Start Date']
tabela_remediation['Estimated Completion Date']	
tabela_remediation['Cost']
tabela_remediation['Progress']
tabela_remediation['Priority']	
tabela_remediation['Status']
tabela_remediation['Due Date']	
tabela_remediation['Comment']	
tabela_remediation['Remediation Task (Name)']	
tabela_remediation['Start Date']
tabela_remediation['Estimated Completion Date']	
tabela_remediation['Priority']
tabela_remediation['Progress']	
tabela_remediation['Status']
tabela_remediation['Due Date']	
tabela_remediation['Description']	
tabela_remediation['Comment']
tabela_remediation['User Name (Security assignment)']



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

time.sleep(10)

# NAVEGACAO PARA AREA DE RISCO
##esperar página carregar
## Clicar em Risk Management
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.ID, 'groupNode_risk_management'))).click()
except: 
	print('erro 1')

## esperar página carregar
## Clicar em Issues
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.LINK_TEXT, 'Issues'))).click()
except: 
	print('erro 2')

time.sleep(5)

## esperar página carregar
## Clicar no terceiro ícone do menu lateral
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:_FOTsdiRemediationManage_itemNode::icon'))).click()
except: 
	print('erro 3')

time.sleep(5)

## esperar página carregar
## Clicar no ícone mais +
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:_FOTr2:1:up1:UPsp1:ls1:AT1:_ATp:create'))).click()
except: 
	print('erro 4')

time.sleep(5)

# INSERIR DADOS
## Name

elemento = 	WebDriverWait(nav, 30).until(EC.presence_of_element_located((By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb1:it4::content')))
elemento.clear()
elemento.send_keys('Remediation Plan_01')

elemento = nav.find_element(By.ID, 'userid')
elemento.clear()
elemento.send_keys('user.evope')

## Description
elemento = nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb1:it2::content')
elemento.clear()
elemento.send_keys('Description')

