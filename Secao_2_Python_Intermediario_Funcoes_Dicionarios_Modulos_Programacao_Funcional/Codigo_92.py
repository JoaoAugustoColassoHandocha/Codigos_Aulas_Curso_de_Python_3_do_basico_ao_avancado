'''
Funçao lmbda em Pyhton

A funçãol lambda é uma função como qualquer outra em Pyhton.

Porém, são funções anônimas que contém apenas uma linha.

Ou seja, tudo deve ser contido dentro de uma única expressão.

'''

import os

os.system('color 1f')

lista = [4, 32, 1, 34, 5, 6, 6, 21]

lista.sort() # Ordena a lista, podendo mudar de crescente para decrescente (lista.sort(reverse = true))

print(f'\n{lista}\n')

###############################

lista_com_dicionarios = [
    
    {'nome': 'João', 'sobrenome': 'Augusto'},
    {'nome': 'Maria', 'sobrenome': 'Pires'},
    {'nome': 'Ana', 'sobrenome': 'Ribeiro'},
    {'nome': 'Carlos', 'sobrenome': 'Gomes'},
    
]

def ordena(item):
    
    return item['nome']

lista.sort(key = ordena)

for item in lista:
    
    print(f'{item}\n')

os.system('pause')
os.system('cls')