import os
from iniUts import *

#===================== POPULA AS CLASSES DE CONFIGURACAO 
ini =  IniUts("./app/Config/configs_prd.ini","./app/Config/configs_dev.ini",in_prd=os.getenv("MODE","DEV")=="PRD")

@ini.link("BOT")
class BotConfig(): 
    NAME    : str

@ini.link("SELENIUM")
class SeleniumConfig(): 
    USE_SELENOID : bool