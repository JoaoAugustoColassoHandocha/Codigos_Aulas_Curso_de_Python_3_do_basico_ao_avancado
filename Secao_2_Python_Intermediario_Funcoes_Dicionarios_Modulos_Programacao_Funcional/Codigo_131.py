'''
Combinations, Permutations e Product - Itertools

Combinação - Ordem não importa - iterável + tamanho do grupo

Permutação - Ordem importa

Produto - Ordem importa e repete valores únicos

'''

import os
from itertools import combinations

os.system('color 1f')

pessoas = ['João', 'Joana', 'Luiz', 'Letícia']

camisetas = [['preta', 'branca'],]

print('\n******************************\n')

# Combinations
for combinar in list(combinations(pessoas, 2)):
        
    print(f'{combinar[0]} - {combinar[1]}')   
    

print('\n******************************\n')

os.system('pause')
os.system('cls')