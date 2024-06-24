# Passo a passo do processo

# Passo 1: Entrar no sistema da empresa
    ## https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de produtos para cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim 


import pyautogui as pg
import time
import pandas as pd

pg.PAUSE = 1

pg.press("win")

pg.write("chrome")

pg.press("enter")

pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")
time.sleep(3)

pg.click(x=685, y=451)
pg.write("pythonimpressionador@gmail.com")

pg.press("tab")
pg.write("0000")
pg.click(x=995, y=638)
time.sleep(3)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    pg.clik(x=653, y=294)
    codigo= tabela.loc[linha, "codigo"] # informar a linha e a coluna da tabela

    pg.write(str(codigo)) # transforma em texto para o método write aceitar

    pg.press("tab")
    pg.write(str(tabela.loc[linha, "marca"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "tipo"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "categoria"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "preco_unitario"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "custo"]))
    pg.press("tab")
    obs= tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pg.write(obs)   
    pg.press("tab")
    pg.press("enter")

    pg.scroll(5000) # dar scroll na página
