import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# code
data = pd.read_excel(r'C:\Users\fabio\Desktop\script_tcc\input\aero_coord.xlsx')
data['BS'] = ''
data['ABS'] = ''
data['AVI'] = ''

driver = webdriver.Chrome(r'C:\Users\fabio\Desktop\script_tcc\input\chromedriver.exe')

i = 0
for i in range(0,data.shape[0]):
    print(i/data.shape[0])

    # colisao
    url = 'http://sistema.cenipa.aer.mil.br/cenipa/sigra/pesquisa_dadosExt?sigra=pesquisa&identificacao=&matricula=&ano_pesquisa=2020&data_inicial=&data_final=&ICAO={}&tipoReporte=colisão&classificacao_ocorrencia=&Parte_da_aeronave=&area_seguranca=&Especie=&aviacaoTipo=&Danos_Prejuizos=&anvOperador=&Efeito_no_voo=&codicoes_ceu=&tripulacao_alertada=&Fase_do_Voo=&parte_dia=&precipitacao=&funcao=&pg=1&Submit=Executar+pesquisa'.format(data['AERO'].iloc[i])
    try:
        driver.get(url)
        bird = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/div[2]/span[2]')
        data['BS'].iloc[i] = int(bird.text)
    except:
        data['BS'].iloc[i] = 'SEM DADO'

    # quase colisao
    url = 'http://sistema.cenipa.aer.mil.br/cenipa/sigra/pesquisa_dadosExt?sigra=pesquisa&identificacao=&matricula=&ano_pesquisa=2020&data_inicial=&data_final=&ICAO={}&tipoReporte=quase+colisão&classificacao_ocorrencia=&Parte_da_aeronave=&area_seguranca=&Especie=&aviacaoTipo=&Danos_Prejuizos=&anvOperador=&Efeito_no_voo=&codicoes_ceu=&tripulacao_alertada=&Fase_do_Voo=&parte_dia=&precipitacao=&funcao=&pg=1&Submit=Executar+pesquisa'.format(data['AERO'].iloc[i])
    try:
        driver.get(url)
        bird = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/div[2]/span[2]')
        data['ABS'].iloc[i] = int(bird.text)
    except:
        data['ABS'].iloc[i] = 'SEM DADO'

    # avistamento
    url = 'http://sistema.cenipa.aer.mil.br/cenipa/sigra/pesquisa_dadosExt?sigra=pesquisa&identificacao=&matricula=&ano_pesquisa=2020&data_inicial=&data_final=&ICAO={}&tipoReporte=avistamento&classificacao_ocorrencia=&Parte_da_aeronave=&area_seguranca=&Especie=&aviacaoTipo=&Danos_Prejuizos=&anvOperador=&Efeito_no_voo=&codicoes_ceu=&tripulacao_alertada=&Fase_do_Voo=&parte_dia=&precipitacao=&funcao=&pg=1&Submit=Executar+pesquisa'.format(data['AERO'].iloc[i])
    try:
        driver.get(url)
        bird = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/div[2]/span[2]')
        data['AVI'].iloc[i] = int(bird.text)
    except:
        data['AVI'].iloc[i] = 'SEM DADO'

data.to_excel(r'C:\Users\fabio\Desktop\script_tcc\output\aero_coord_bs.xlsx',index=False)
