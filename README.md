# Rio Entertainment Extractor

## 1 - Sobre
O Rio Entrainment Extractor é um robô de automação desenvolvido em Python com o objetivo de extrair dados de eventos do site da Sympla, filtrando apenas os eventos de entretenimento mais vistos nas últimas 24 horas na cidade do Rio de Janeiro. Os dados extraídos são salvos em uma planilha dentro de uma pasta compartilhada para análise posterior pela equipe responsável.


## 2 - Tecnologias Utilizadas
As tecnologias utilzadas no processo foram:
- python
    - selenium


## 3 - Instalação
requer python 3.11 para rodar.
Instale as dependencias usando:

```ssh
pip install -r requirements
```

Em seguida execute o processo com:
```ssh
python app
```

## 4 - Ambientes
A mudanca de ambiente é configurada na variavel de ambiente chamada `ENV` que pode ter os valores `PRD` ou `DEV`, as mudaças de ambiante impactam nas respectivas atividades:
- DEV
    - Selenium: é utilizado o browser local na maquina do desenvolvedor
- PRD
    - Selenium: é utilizado a conexão via selenoid

_Para fazer a mudançao de ambiente basta alterar a variável  `ENV` no arquivo `_.env`_

## 5 - Config
 No arquivo `Config/configs_prd.ini` é possível encontar todas as connfigurações necessarias para a execução do bot em produção:

- `BOT`: guarda dados sobre o processo
- `SELENIUM`: servidor do selenoid utilizado em produção
### scheduller
Para configurar o scheduller verifique o arquivo `scheduller.py` tem a função de programar o tempo de cada execução.

```py
#PROGRAMANDO A EXECUCÃO
cron_scheduller = "30 08 * * mon"
if pycron.is_now(cron_scheduller):
    print_time()
    main()
    while pycron.is_now(cron_scheduller):pass
```


## 6 - Execução em DEV
A execução em modo **DEV** esse modo e ativado de forma automática pelo template, esse template identifica quando estamos rodando no docker e muda a chave para **PRD** basta rodar o codigo naa sua maquia com o comando a baixo.
 
```ssh
python app
```





