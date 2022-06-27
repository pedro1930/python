import glob
import pandas as pd
import os
import time
import numpy as np


def cria_arquivos(tamanho):
    lista_df=[]
    for i in range(0,tamanho):
        lista_df.append(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=['coluna_1','coluna_2','coluna_3','coluna_4']))
    return lista_df

def salva_arquivos(lista_df,caminho):
    for i in range(0,len(lista_df)):
        pd.to_csv(f'{caminho}\df{i}.csv')

def junta_arquivos(caminho,lista_df):
    aux=pd.DataFrame()
    for df in lista_df:
        aux=aux.merge(df)


    