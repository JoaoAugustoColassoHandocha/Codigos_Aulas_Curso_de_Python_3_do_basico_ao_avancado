'''
Reduce - Faz a redução de um iterável em um valor

'''

import os
from functools import reduce

os.system('color 1f')

produtos = [
    
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
    
]

total = 0

total_reduce = reduce()

print('\n******************************\n')

for produto in produtos:
    
    total += produto['preco']
    
print(total)

print('\n******************************\n')

print(sum([p['preco'] for p in produtos]))

print('\n******************************\n')

os.system('pause')
os.system('cls')