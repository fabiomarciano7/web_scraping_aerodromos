import pandas as pd
import time
import pyautogui as auto

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# code
data = pd.read_excel(r'C:\Users\fabio\Desktop\script_tcc\input\aero_coord_bs.xlsx')
data['FUSO'] = ''

driver = webdriver.Chrome(r'C:\Users\fabio\Desktop\script_tcc\input\chromedriver.exe')

url = 'http://rcn.montana.edu/resources/Converter.aspx'
driver.get(url)

i = 1
for i in range(0,data.shape[0]):
    print(i/data.shape[0])

    lat = driver.find_element_by_xpath('//*[@id="decimalLatitude"]')
    lat.clear()
    lat.send_keys(data['Latitude'].iloc[i])

    long = driver.find_element_by_xpath('//*[@id="decimalLongitude"]')
    long.clear()
    long.send_keys(data['Longitude'].iloc[i])

    click = driver.find_element_by_xpath('//*[@id="fullpane"]/content/div[3]/div/input[1]')
    click.click()

    # zone
    zone = driver.find_element_by_xpath('//*[@id="utmZone"]')
    data['FUSO'].iloc[i] = zone.get_attribute('value')

data.to_excel(r'C:\Users\fabio\Desktop\script_tcc\output\aero_coord_bs_zone.xlsx',index=False)
