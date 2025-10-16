'''
Reduce - Faz a redução de um iterável em um valor

'''

import os
from functools import reduce

os.system('color 1f')

produtos = [
    
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
    
]

total = 0

total_reduce = reduce(funcao_do_reduce, produtos, 0)

print('\n******************************\n')

for produto in produtos:
    
    total += produto['preco']
    
print(total)

print('\n******************************\n')

print(sum([p['preco'] for p in produtos]))

print('\n******************************\n')

print('Total: R$', total_reduce)

print('\n******************************\n')

os.system('pause')
os.system('cls')