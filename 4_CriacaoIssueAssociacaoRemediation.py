import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select #dropdown
import pandas as pd
from time import sleep

# importar/visualizar a base de dados
table_create_issue = pd.read_excel('4_Input_CreateIssue.xlsx')
print(table_create_issue)

table_create_issue['Issue Name']
table_create_issue['Description	Type']	
table_create_issue['Severity']
table_create_issue['Status']
table_create_issue['Comment']
table_create_issue['Context Segment']
table_create_issue['WLS_U']
table_create_issue['Object Type']
table_create_issue['Related Object for Issue']	
table_create_issue['Requires Remediation']
table_create_issue['Impact Cost']
table_create_issue['Likelyhood of Recurrence']	
table_create_issue['Remediation Cost']
table_create_issue['Source']
table_create_issue['Remediation Plan']
table_create_issue['User Name (Security assignment)']




# Abrir Navegador
PATH = 'C:\Program Files (x86)\chromedriver.exe'
nav = webdriver.Chrome(PATH)
nav.get('https://fa-eueu-dev1-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/FuseWelcome?_adf.ctrl-state=7pv5r1sdr_5&fnd=%3B%3B%3B%3Bfalse%3B256%3B%3B%3B&_afrLoop=4691137915934643')
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

# NAVEGACAO PARA AREA DE RISCO - ISSUES
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
## Clicar no segundo icone do menu lateral
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:_FOTsdiIssueManage_itemNode::icon'))).click()
except: 
	print('erro 2')

time.sleep(5)

## esperar página carregar
## Clicar no mais +
try:
	WebDriverWait(nav, 30).until(EC.presence_of_element_located
	((By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:_FOTr1:1:up1:UPsp1:ls1:AT1:_ATp:create::icon'))).click()
except: 
	print('erro 2')

time.sleep(5)

# CADASTRO
##  name
elemento = nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb1:it1::content')
elemento.clear()
elemento.send_keys('teste')

##  description
elemento = nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb1:it2::content')
elemento.clear()
elemento.send_keys('teste_001')

## dropdown type
dropDownSelect = Select(nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb1:soc1::content')) 
dropDownSelect.selectByVisibleText('OPERATIONAL')

## dropdown severity
dropDownSelect = Select(nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb1:soc2::content')) 
dropDownSelect.selectByVisibleText('Minor Deficiency')

## dropdown status
dropDownSelect = Select(nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb1:soc5::content')) 
dropDownSelect.selectByVisibleText('Open')

## comment
elemento = nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb1:it3::content')
elemento.clear()
elemento.send_keys('teste')

## dropdown content segment

## dropdown WES_U

## click related record
nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb3:PCEcil6::icon').click()

## dropdown object type

## click +
nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:pb3:AT2:_ATp:ctb12::icon').click()


## type to search
elemento = nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:2:up1:UPsp1:ls2:_LSSF::content')
elemento.clear()
elemento.send_keys('teste')


## select option

## voltar
nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:2:up1:UPsp1:SPdonei::icon').click()

## submit
nav.find_element(By.ID, 'pt1:_FOr1:1:_FOSritemNode_financial_reporting_compliance_issues:0:MAnt2:1:up1:UPsp1:cmi3').click()

# OUTRO
# clicar no que foi criado


