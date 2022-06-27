import glob
import pandas as pd
import os
import time
import numpy as np


def cria_arquivos(tamanho):
    lista_dataframes=[]
    for i in range(0,tamanho):
        lista_dataframes.append(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=['coluna_1','coluna_2','coluna_3','coluna_4']))
    return lista_dataframes

def salva_arquivos(lista_dataframes,caminho):
    for i in range(0,len(lista_dataframes)):
        pd.to_csv(f'{caminho}\df{i}.csv')

def junta_arquivos(caminho):
    aux=pd.DataFrame()


    