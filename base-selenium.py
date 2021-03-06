# by leandro falcao, libs using selenium and webdriver_manager, for update webdrives real time 
# usei o a biblioteca selenium e webdriver_manager, para atualização do webdriver, de qualquer navegador. base selenium 4 em diante..
# for install lib, with command line: pip install selenium; pip install webdriver_manager
# para instalar o selenium e webdriver_manager use o comando: pip install selenium; pip install selenium webdriver_manager
#
# my user https://github.com/leandro-falcao   date: BRa(11/06/2022) or EN (6/11/2022)
#report: https://github.com/leandro-falcao/base-selenium
#
#

import time as tempo

def baseSelenium(url):
  # será importado o webdrive do selenium
  from selenium import webdriver

  #será importado o webdriver_manager, qua atualizara os nossos webdrivers
  from webdriver_manager.chrome import ChromeDriverManager

  #importar um serviço que foi meio que ibutido no webdriver_manager
  from selenium.webdriver.chrome.service import Service

  #agora dentro do servico colocar a instalçaão do chrome	 sempre atualizada pelo sistema automatico
  service = Service(ChromeDriverManager().install())

  # vou falar que navegador é o chromedriver vindo do webdriver_manager, continua utilizando em todo código
  navegador = webdriver.Chrome(service=service)
  
  url = '' #url do site, here adress of site exemplo('https://www.github.com')

  navegador.get(url) #abre o site, open site
  
  tempo.sleep(1) #pausa de 1 segundo ate close no app

baseSelenium() #chamando a função, também pode sr chamada dentro de um código principal
