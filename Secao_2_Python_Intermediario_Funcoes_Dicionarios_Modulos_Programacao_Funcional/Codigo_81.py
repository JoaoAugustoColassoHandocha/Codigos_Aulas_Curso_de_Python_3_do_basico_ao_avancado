'''
Manipulando chaves e valores em dicionários.

'''

import os

os.system('color 1f')

pessoa = {
    
    'nome': 'João Augusto',
    'sobrenome': 'Colasso Handocha',
    'idade': 27,
    'altura': 1.80,
    'endereços': [
        
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 345},
        
    ],
        
}

print(f'\nNome e Sobrenome: {pessoa['nome']} {pessoa['sobrenome']}')
print(f'Idade: {pessoa['idade']}')
print(f'Altura: {pessoa['altura']}')
print(f'Endereços: {pessoa['endereços']}\n')

os.system('pause')
os.system('cls')

##############################

solicitar_nome = input('\nQual seu nome: ')
os.system('cls')



os.system('pause')
os.system('cls')