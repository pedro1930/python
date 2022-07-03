import glob
import pandas as pd
import time
import numpy as np



def cria_arquivos(tamanho,caminho_inicial):
    aux = 0
    tamanho=int(tamanho)
    for i in range(0,tamanho):
        aux=pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=['coluna_1','coluna_2','coluna_3','coluna_4'])
        aux.to_csv(caminho_inicial + f'\dataframe{i}.csv')


def junta_arquivos(caminho_inicial,caminho_final):
    lista=glob.glob(caminho_inicial+'\*.csv')
    aux = pd.DataFrame()
    for arquivo in lista:
        df=pd.read_csv(arquivo)
        aux=aux.append(df)
    aux.to_csv(caminho_final+ f'\DataframeFinal.csv')

        



    