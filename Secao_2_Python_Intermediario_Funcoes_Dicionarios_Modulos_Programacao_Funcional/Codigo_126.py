'''
EXERCÍCIO

Unir listas

Crie uma função zipper (como o zipper de roupas)

O trabalho dessa função será unir duas listas na ordem.

Use todos os valores da menor lista.

Ex.:

['Salvador', 'Ubatuba', 'Belo Horizonte'] ['BA', 'SP', 'MG', 'RJ']

Resultado

[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

98, 99,

'''

import os

os.system('color 1f')

print('\n******************************\n')

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado  = ['BA', 'SP', 'MG', 'RJ']

combinados = zip(cidade, estado)

print('\n******************************\n')

os.system('pause')
os.system('cls')