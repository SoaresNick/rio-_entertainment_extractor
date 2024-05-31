import sys
sys.path.append("./app")
from app.__main__ import main,logger,show_config
from dateUts import *
from time import sleep
import pycron


#MOSTRA AS CONFIGURACOES ATUAIS
show_config()
#FUNCAO PARA MOSTRAR A DATA/HORA DA EXECUCAO
print_time = lambda:logger.info(f"SCHEDULLER -----------> {now(fmt='sql+hr')}")

#https://crontab.guru/

cron_scheduller = "30 08 * * mon"

while(1):
    sleep(1)

    if pycron.is_now(cron_scheduller):
        print_time()
        main()
        while pycron.is_now(cron_scheduller):pass


    