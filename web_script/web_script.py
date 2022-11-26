import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from secret_data import *

driver = webdriver.Firefox()

driver.get('https://intranet.univali.br/intranet/indexMural.php')

# make a login file with 'login' and 'password' string variables with the right variables

driver.find_element(By.XPATH, ('//*[@id="CorpoLogin"]/tbody/tr[1]/td/input')).send_keys(login)
driver.find_element(By.XPATH, ('//*[@id="CorpoLogin"]/tbody/tr[2]/td/input[1]')).send_keys(password)
driver.find_element(By.XPATH, '//*[@id="entrar"]').click()

driver.find_element(By.XPATH, '//*[@id="linkMenuId_109"]').click()
driver.find_element(By.LINK_TEXT, 'CIENCIA DA COMPUTACAO-ITAJAÍ - ITJ').click()
driver.find_element(By.LINK_TEXT, 'Notas').click()

gradesDirt = driver.find_element(By.XPATH, '/html/body/form/div[1]/div/div[4]/div/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr[8]/td/div/table/tbody/tr/td')

with open('grades.txt', 'w') as file:
        file.write(gradesDirt.text)

driver.close()

grades = []
with open('grades.txt', 'r') as file:
    for line in file:
        if line.isupper():
            grades.append(line)
        if re.search(r'\d{1,2},\d{1,2}', line):
            grades.append(line)

with open('grades.txt', 'w') as file:
    for grade in grades:
        file.write(grade)

with open('grades.txt', 'r') as file:
    for line in file: # if a umber or NA
        if re.search(r'\d{1,2},\d{1,2}', line) or re.search(r'ND', line):
            print(line)
        else:
            print(f'\n{line}')