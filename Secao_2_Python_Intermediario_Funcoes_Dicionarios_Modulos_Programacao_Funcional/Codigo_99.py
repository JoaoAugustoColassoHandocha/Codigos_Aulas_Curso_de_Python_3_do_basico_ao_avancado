'''
Dictionary comprehension e Set comprehension

'''

import os

os.system('color 1f')

produto = {
    
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritrio',
    
}

print('\n##############################\n')

print(produto.items()) # dict_items([('nome', 'Caneta Azul'), ('preco', 2.5), ('categoria', 'Escritrio')])

print('\n##############################\n')

for chave, valor in produto.items():
    
    print(chave, valor) # nome Caneta Azul preco 2.5 categoria Escritrio

print('\n##############################\n')

dc = {
    
    
    
}

print('\n##############################\n')

os.system('pause')
os.system('cls')