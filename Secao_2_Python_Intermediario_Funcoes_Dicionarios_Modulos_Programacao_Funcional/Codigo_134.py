'''
Filter é um filtro funcional

'''

import os

os.system('color 1f')

def print_iter(iterator):
    
    print(*list(iterator), sep = '\n')
    
def filtrar_preco(produto):
    
    return produto['preco'] >= 10
    
produtos = [
    
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
    
]

novos_produtos = [p for p in produtos if p['preco'] > 10]

novos_produtos_filter = filter(filtrar_preco, produtos)

print('\n******************************\n')

print_iter(produtos)
print('\n-x-x-x-x-x-x-x-x-x-x-x-x-x-\n')
print_iter(novos_produtos)
print('\n-x-x-x-x-x-x-x-x-x-x-x-x-x-\n')
print_iter(novos_produtos_filter)

print('\n******************************\n')

os.system('pause')
os.system('cls')