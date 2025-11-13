'''
Problema dos parâmetros mutáveis em funções Python

'''

import os

os.system('color 1f')

def adiciona_clientes(nome, lista = []):
    
    lista.append(nome)
    return lista

clientes = adiciona_clientes(input('Nome: '))

os.system('cls')

print('\n******************************\n')

print(clientes)

print('\n******************************\n')

os.system('pause')
os.system('cls')