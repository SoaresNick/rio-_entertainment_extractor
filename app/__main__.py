from Config import logger,show_config
from Libs.loguru import logger_start
from Modules.admin import Sympla
from Modules.export import Export
from Config import *


@logger_start
def main():
    sympla = Sympla()
    export = Export()

    logger.success("STEP_SYMPLA")
    dados = sympla.EXTRAI_DADOS()
   
    
    logger.success("STEP_EXPORT")
    export.SALVA_DADOS(dados)


if __name__ ==  "__main__":
    show_config()
    main()



    

    
    


