'''
Empacotamento e desempacotamento de dicionários

'''

import os

os.system('color 1f')

a, b = 1, 2
a, b = b, a

print(f'\n{a, b}\n')

################################

pessoa = {
    
    'nome': 'Aline',
    'sobrenome': 'Souza',
    
}

a, b = pessoa

print(f'{a, b}')

os.system('pause')
os.system('exit')