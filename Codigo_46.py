'''
Listas em Python

Tipo list - Mutável

Suporta vários valores de qualquer tipo

Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis: append, insert, pop, del, clear, extend, +

CRUD:

Create Read Update Delete

Criar, ler, alterar , apagar = lista[i] (CRUD)

* Para apagar um item da lista, opte em transferir esse item para o final da lista para apagar.

'''

import os

os.system('color 1f')

lista = [10, 20, 30, 40]

print(f'\n{lista}\n')
print(f'{lista[2]}\n')
print('=' * 30 + '\n')

lista[2] = 300

print(f'{lista}\n')
print('=' * 30 + '\n')

del lista[2]

print(f'{lista}\n')
print('=' * 30 + '\n')

os.system('pause')
os.system('cls')