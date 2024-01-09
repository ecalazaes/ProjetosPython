# Passo a passo do projeto
import pyautogui as pg
import time
import pandas as pd

# Passo 1 - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
# Bibliotecas em Python
# PyAutoGui

# clicar -> pg.click
# escrever -> pg.write
# apertar -> pg.press
# atalho -> pg.hotkey
# scroll -> (rolar) -> pg.scroll

pg.PAUSE = 0.5

pg.press('win')
pg.write('opera')
pg.press('enter')
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pg.write(link)
pg.press('enter')

# Passo 2 - Fazer login
pg.click(x=-537, y=-1771)
pg.write('ecalazaes@gmail.com')
pg.press('tab')
pg.write('senha')
pg.click(x=-296, y=-1612)

# Passo 3 - Importar base de dados
tabela = pd.read_csv('produtos.csv')
# print(tabela)

for linha in tabela.index:
    # Passo 4 - Cadastrar um produtos
    pg.click(x=-536, y=-1889)
    # Codigo
    pg.write(str(tabela.loc[linha, 'codigo']))
    pg.press('tab')
    # Marca
    pg.write(str(tabela.loc[linha, 'marca']))
    pg.press('tab')
    # Tipo
    pg.write(str(tabela.loc[linha, 'tipo']))
    pg.press('tab')
    # Categoria
    pg.write(str(tabela.loc[linha, 'categoria']))
    pg.press('tab')
    # Preço_Unitário
    pg.write(str(tabela.loc[linha, 'preco_unitario']))
    pg.press('tab')
    # Custo
    pg.write(str(tabela.loc[linha, 'custo']))
    pg.press('tab')
    # Obs
    pg.write(str(tabela.loc[linha, 'obs']))
    pg.press('tab')

    pg.press('enter')
    pg.scroll(5000)


# Passo 5 - Repetir isso até acabar a base de dados

