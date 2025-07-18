'''
Métodos úteis dos dicionários em Python

len - quantas chaves
keys - iterável com as chaves
values - iteráveç com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro

'''

import os

os.system('color 1f')

pessoa = {
    
    'nome': 'João Augusto',
    'idade': 27,
    
}

print('\n')

# Quantidade de chaves
print(len(pessoa))

# Lista os nomes das chaves (Pode ser transformada como list ou tuple) (Pode utilizar também o for de duas formas para conseguiur o nome das chaves)
print(pessoa.keys())
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))

print('\n')
for chave in pessoa.keys():
    
    print(chave)
    
print('\n')

print('\n')
for chave in pessoa:
    
    print(chave)
    
print('\n')

os.system('pause')
os.system('cls')