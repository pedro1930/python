import glob
import pandas as pd
import time
import sys
from funcoes import cria_arquivos
from funcoes import junta_arquivos

inicio = time.time()
#argumentos
arg_list = sys.argv
print(sys.argv)
caminho_inicial = arg_list[1]
print(caminho_inicial,"\n")
caminho_final = arg_list[2]
print(caminho_final,"\n")
tamanho = arg_list[3]
print(tamanho,"\n")
##

cria_arquivos(tamanho,caminho_inicial)
junta_arquivos(caminho_inicial,caminho_final)

print("Tempo de execução :", round(time.time() - inicio,3))