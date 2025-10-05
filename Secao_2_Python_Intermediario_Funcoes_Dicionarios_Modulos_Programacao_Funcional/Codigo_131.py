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

for combinar in combinations(pessoas, 2):
    
    print(combinar)    
    

print('\n******************************\n')

os.system('pause')
os.system('cls')