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

print('\n******************************\n')

for produto in produtos:
    
    total += produto['preco']
    
print(f'R$ {total:.2f}')

print('\n******************************\n')

print(f'R$ {sum([p['preco'] for p in produtos]):.2f}')

print('\n******************************\n')

def funcao_do_reduce(acumulador, produto):
    
    print(f'Acumulador: {acumulador}')
    print(f'Produto: {produto['nome']}')
    print(f'Preço: R$ {produto['preco']:.2f}')
    print('\n')
    return acumulador + produto['preco']

total_reduce = reduce(funcao_do_reduce, produtos, 0)

print(f'Total: R$ {total_reduce:.2f}')

print('\n******************************\n')



print('\n******************************\n')

os.system('pause')
os.system('cls')