'''
EXERCÍCIO

Exiba os índices da lista

'''

import os

os.system('color 1f')

lista = ['Maria', 'Helena', 'Joao']

lista.append('Luiz')

indices = range(len(lista))

print('\n' + '=' * 30)

for indice in indices:
    
    print(f'\n{indice} - {lista[indice]}')
    print('\n' + '=' * 30)
    
print('\n')
    
os.system('pause')
os.system('cls')