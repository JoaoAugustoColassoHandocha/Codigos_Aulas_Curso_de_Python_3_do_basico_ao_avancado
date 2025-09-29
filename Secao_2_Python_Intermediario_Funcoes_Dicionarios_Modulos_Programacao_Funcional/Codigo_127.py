'''
RESOLUÇÃO

Unir listas

Crie uma função zipper (como o zipper de roupas)

O trabalho dessa função será unir duas listas na ordem.

Use todos os valores da menor lista.

Ex.:

['Salvador', 'Ubatuba', 'Belo Horizonte'] ['BA', 'SP', 'MG', 'RJ']

Resultado

[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

'''

import os
from itertools import zip_longest

os.system('color 1f')

print('\n******************************\n')

def zipper(lista1, lista2):
    
    intervalo_maximo = min(len(lista1),len(lista2))
    return [(lista1[i], lista2[i]) for i in range(intervalo_maximo)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

for lista_cidade_estado in zipper(l1, l2):
    
    print(f'{lista_cidade_estado[0]} - {lista_cidade_estado[1]}')

print('\n******************************\n')

for c_e in list(zip(l1, l2)):
    
    print(f'{c_e[0]} - {c_e[1]}')

print('\n******************************\n')

for cid_est in list(zip_longest(l1, l2, fillvalue = '-Sem Cidade-')):
    
    print(f'{cid_est[0]} - {cid_est[1]}')

print('\n******************************\n')

os.system('pause')
os.system('cls')