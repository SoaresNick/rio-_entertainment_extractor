from Libs.selenium import SeleniumLib
from Config import BotConfig,SeleniumConfig
from Config.loguru import logger
from Libs.loguru import logger_class
from dateUts import *
from datetime import datetime as dt
from selenium.webdriver.common.by import By

@logger_class()
class Sympla(SeleniumLib):

    def SETUP(self):
        #CONFIGURA O BROWSER LOCAL
        self.setupSelenium(host=None,name=BotConfig.NAME,use_selenoid=SeleniumConfig.USE_SELENOID)
        
    def ACESSA_PAGINA(self):
        #ABRE A PÁGINA
        self.open_page("https://www.sympla.com.br/eventos/rio-de-janeiro-rj/mais-vistos")
    #     #ESPERA A PÁGINA CARREGAR
        self.wait_xpath("//button[@id = 'btn-login']")
    #     #CLICA NO SELECT PARA ESCOLHER DETERMINADO ESTADO
    #     self.driver.find_element(By.XPATH, "//div[text() = 'Qualquer lugar']").click()
    #     #ESPERA A PÁGINA CARREGAR
    #     self.wait_xpath("//div[text() = 'Qualquer lugar']")
    #     #SELECIONA O ESTADO DO RIO DE JANEIRO
    #     self.driver.find_element(By.XPATH, "//div[text() = 'Rio de Janeiro']").click()
    #     #ESPERA A PÁGINA CARREGAR
    #     a = 1
    #     self.wait_xpath("//button[@id = 'btn-login']")
        
    def SCRAPPING(self):
        #OBTEM OS CARDS DOS EVENTOS
        events = self.driver.find_elements(By.XPATH, "//a[contains(@data-creative, '.matriz-collection-top-eventos.component-entretenimento-dia.response_type-event-card.sort-location-score.type-normal.')]")
        event_links = []
        dados =[]
        
        
        #EXTRAI O LINK DE ACESSO DOS 4 PRIMEIROS
        for e in events[:4]:
            event_links.append(e.get_attribute('href'))
        
        for x in event_links:
            dado = {}
            #ACESSA A PÁGINA
            self.open_page(x)
            
            #AGUARDA O CARREGAMENTO DA PÁGINA
            self.wait_xpath("//span[contains(text(), 'Fale com o produtor')]")
            
            #EXTRAI O NOME DO EVENTO 
            dado['Nome'] = self.driver.find_element(By.XPATH, "//h1[@class = 'sc-983ba91-0 fypPvW']").text
            
            #EXTRAI E TRATA A DATA DO EVENTO
            dado['Data'] = self.driver.find_element(By.XPATH, "//div[@class = 'sc-983ba91-1 cZLMzD']").text.split("•")[0].strip()
            
            #EXTRAI O LOCAL DO EVENTO
            dado['Local'] = self.driver.find_element(By.XPATH, "//div[@class = 'sc-983ba91-2 sc-983ba91-3 leDNYU']").text.split("em")[1].strip()
            
            #EXTRAI A DESCRIÇÃO DO EVENTO
            dado['Descrição'] = self.driver.find_element(By.XPATH, "//div[@class = 'sc-537fdfcb-0 bdUbUp']").text.replace('\n', ' ')
            
            #EXTRAI SOBRE O PRODUTOR
            dado['Sobre Produtor'] = self.driver.find_element(By.XPATH, "//p[@class = 'sc-93393ac5-4 jxkNXt']").text
            
             # ADICIONA OS DADOS DO EVENTO À LISTA DE DADOS
            dados.append(dado)
            
            # VOLTA PARA A PÁGINA ANTERIOR
            self.driver.back()
            
            #AGUARDA O CARREGAMENTO DA PÁGINA
            self.wait_xpath("//h1[contains(text(), 'Eventos mais vistos')]")

        return dados

    # ORQUESTRADOR
    def EXTRAI_DADOS(self):
        #CONFIGURA O SELENOID OU CHROMEDRIVER
        logger.info("\tCONFIGURANDO AMBIENTE")
        self.SETUP()
        
        #ACESSA O SITE DA SYMPLA
        logger.info("\tACESSANDO PÁGINA")
        self.ACESSA_PAGINA()
        
        #EXTRAI OS DADOS DOS EVENTOS
        logger.info("\tEXTRAINDO OS DADOS")
        return self.SCRAPPING()