'''
MAP - Para mapear dados

'''

import os

from functools import partial

os.system('color 1f')

def print_iter(iterator):
    
    print(*list(iterator), sep = '\n')
    
def aumentar_porcentagem(valor, porcentagem):
    
    return round(valor * porcentagem, 2)

def muda_preco_de_produtos(produto):

    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem = 1.1)
     
produtos = [
    
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
    
]

novos_produtos = [{**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos]

novos_produtos_map = map(muda_preco_de_produtos, produtos)

print('\n******************************\n')

print_iter(produtos)
print('\n-x-x-x-x-x-x-x-x-x-x-x-x-x-\n')
print_iter(novos_produtos)
print('\n-x-x-x-x-x-x-x-x-x-x-x-x-x-\n')
print_iter(novos_produtos_map)

print('\n******************************\n')

print(list(map(lambda x: x * 3, [1, 2, 3, 4])))

print('\n******************************\n')

os.system('pause')
os.system('cls')