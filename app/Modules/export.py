from Config.loguru import logger
from Libs.loguru import logger_class
from dateUts import today
import pandas as pd

@logger_class()
class Export():
    
    def SAVE(self,dados):
        #CRIAR UM DATAFRAME COM OS DADOS EXTRAÍDOS
        df = pd.DataFrame(dados)
        #TRANSCREVER OS DADOS PARA A PLANILHA
        df.to_excel(f'./output/MKT_Acompanhamento Page_Eventos Mais Vistos 24h_{today("brz").replace("/","")}.xlsx', index=False)
        
        
    def SALVA_DADOS(self,dados):
        logger.info("\tSALVANDO DADOS")
        self.SAVE(dados)