'''
Dicionários em Python (tipo dict)

Dicionários são estruturas de dados do tipo par de "chave" e "valor".

Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.

O valor pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves - {} - ou a classe dict para criar dicionários.

Imutáveis: str, int, float, bool, tuple
Mutável: dict, list

pessoa = {

    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    
    ],

}

É possível criar lista dessa forma, mas é pouco usada:

pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

'''

import os

os.system('color 1f')

pessoa = {

    'nome': 'João Augusto',
    'sobrenome': 'Colasso Handocha',
    'idade': 27,
    'altura': 1.75,
    'endereços': [
        
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    
    ],

}

print(f'\n{pessoa}\n')

os.system('pause')
os.system('cls')

print('\n')
print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['endereços'])
print('\n')

os.system('pause')
os.system('cls')

print('\n')

for chave in pessoa:
    
    print(f'{chave}: {pessoa[chave]}')
    
print('\n')

os.system('pause')
os.system('cls')