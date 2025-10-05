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

def print_iter(iterator):
    
    for separar in list(iterator):
        
        print(f'{separar[0]} - {separar[1]}')

print('\n******************************\n')

# Combinations
print_iter(combinations(pessoas, 2))   
    
print('\n******************************\n')

os.system('pause')
os.system('cls')