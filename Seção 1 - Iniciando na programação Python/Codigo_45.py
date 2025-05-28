'''
Listas em Python

Tipo list - Mutável

Suporta vários valores de qualquer tipo

Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis: append, insert, pop, del, clear, extend, +

'''

import os

os.system('color 1f')

string = 'ABCDE'

lista = [123, True, 'Joao', 1.2, []]

print(f'\n{lista[0]}')
print(f'\n{lista[1]}')
print(f'\n{lista[2]}')
print(f'\n{lista[3]}')
print(f'\n{lista[4]}')

print('\n' + '=' * 30 + '\n')

lista[2] = 'Maria'

print(f'{lista[2]}\n')

os.system('pause')
os.system('cls')