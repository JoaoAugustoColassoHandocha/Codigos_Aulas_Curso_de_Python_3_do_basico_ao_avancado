'''
Combinations, Permutations e Product - Itertools

Combinação - Ordem não importa - iterável + tamanho do grupo

Permutação - Ordem importa

Produto - Ordem importa e repete valores únicos

'''

import os
from itertools import combinations, permutations, product

os.system('color 1f')

pessoas = ['João', 'Joana', 'Luiz', 'Letícia']

camisetas = [['preta', 'branca'],['P', 'M', 'G', 'GG', 'G1', 'G2', 'G3'],['Masculino', 'Feminino', 'Infantil'],['Algodão', 'Poliéster'],]

def print_iter(iterator):
    
    for separar in list(iterator):
        
        print(separar)

print('\n******************************\n')

# Combinations
print_iter(combinations(pessoas, 2))   
    
print('\n******************************\n')

# Permutations
print_iter(permutations(pessoas, 2))   

print('\n******************************\n')

print_iter(product(*camisetas))

print('\n******************************\n')

os.system('pause')
os.system('cls')