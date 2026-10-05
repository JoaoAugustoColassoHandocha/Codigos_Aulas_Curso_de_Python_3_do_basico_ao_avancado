'''
Update Codigo_194.py

Context Manager com função - Criando e Usando gerenciadores de contexto

'''

import os
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    
    print('Abrindo arquivo!')
    arquivo = open(caminho_arquivo, modo, encoding = 'UTF8')
    yield arquivo
    

print('\n------------------------------\n')

with my_open('Secao_3_Introducao_a_Programacao_Orientada_a_Objetos_em_Python//Codigo_193.txt', 'w') as arquivo:
    
    arquivo.write('Linha 1\n')
    # arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')