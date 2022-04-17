import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# code
data = pd.read_excel(r'C:\Users\fabio\Desktop\script_tcc\input\AERO.xlsx')
data['COOD'] = ""

driver = webdriver.Chrome(r'C:\Users\fabio\Desktop\script_tcc\input\chromedriver.exe')

i = 0
for i in range(36,data.shape[0]):
    print(i/data.shape[0])

    time.sleep(1)
    url = 'https://aisweb.decea.mil.br/?i=aerodromos&codigo={}'.format(data['AERO'].iloc[i])

    try:
        driver.get(url)
        coord = driver.find_element_by_xpath('//*[@id="rotaer"]/table/tbody/tr[1]/td[2]')
        data['COOD'].iloc[i] = coord.text
    except:
        data['COOD'].iloc[i] = 'SEM COORD'

data.to_excel(r'C:\Users\fabio\Desktop\script_tcc\output\aero_coord.xlsx',index=False)
