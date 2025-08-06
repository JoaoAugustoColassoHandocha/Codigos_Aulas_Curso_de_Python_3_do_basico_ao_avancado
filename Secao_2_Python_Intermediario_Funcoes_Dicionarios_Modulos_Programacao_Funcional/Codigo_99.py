'''
Dictionary comprehension e Set comprehension

'''

import os

os.system('color 1f')

produto = {
    
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
    
}

print('\n##############################\n')

print(produto.items()) # dict_items([('nome', 'Caneta Azul'), ('preco', 2.5), ('categoria', 'Escritorio')])

print('\n##############################\n')

for chave, valor in produto.items():
    
    print(chave, valor) # nome Caneta Azul preco 2.5 categoria Escritrio

print('\n##############################\n')

# Dictionary comprehension

dc = {
    
    chave: valor
    for chave, valor
    in produto.items()
    
}

print(dc) # {'nome': 'Caneta Azul', 'preco': 2.5, 'categoria': 'Escritorio'}

print('\n##############################\n')

# Dictionary comprehension com upper

dc = {
    
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    
}

print(dc) # {'nome': 'CANETA AZUL', 'preco': 2.5, 'categoria': 'ESCRITORIO'}

print('\n##############################\n')

# Dictionary comprehension com upper de outra forma

dc2 = {
    
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items()
    
}

print(dc2) # {'nome': 'CANETA AZUL', 'preco': 2.5, 'categoria': 'ESCRITORIO'}

print('\n##############################\n')

# Dictionary comprehension a partir de uma lista

lista = [('a', 'valor a'), ('b', 'valor b'), ('c', 'valor c'),]

dc_list = {chave:valor for chave, valor in lista}

print(dc_list) # {'a': 'valor a', 'b': 'valor b', 'c': 'valor c'}

print('\n##############################\n')

print(dict(dc_list)) # {'a': 'valor a', 'b': 'valor b', 'c': 'valor c'}

print('\n##############################\n')

# Set comprehension

s1 = {}

print('\n##############################\n')

os.system('pause')
os.system('cls')