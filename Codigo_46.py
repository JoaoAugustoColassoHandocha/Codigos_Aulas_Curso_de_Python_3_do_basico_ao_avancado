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

lista = [10, 20, 30, 40] # Lista.

# Visualização da lista inteira e do item que está no índice 2.
print(f'\n{lista}\n')
print(f'{lista[2]}\n')
print('=' * 30 + '\n')

# Modificando o índice 2 da lista e imprimindo na tela a lista modificada.
lista[2] = 300

print(f'{lista}\n')
print('=' * 30 + '\n')

# Deletando o item do índice 2 da lista e imprimindo a lista modificada.
del lista[2]

print(f'{lista}\n')
print('=' * 30 + '\n')

# Modificando o índice 2 e adicionando um item na lista, onde esse adicionamento é posicionado no final da mesma, e imprimindo a lista modificada na tela.
lista[2] = 30
lista.append(40)

print(f'{lista}\n')
print('=' * 30 + '\n')

# Removendo o último item da lista e imprimindo na tela a lista modificada.
lista.pop()

print(f'{lista}\n')
print('=' * 30 + '\n')

# Removendo o item do índice 0 da lista e imprimindo na tela a lista modificada.

lista.pop(0)

print(f'{lista}\n')
print('=' * 30 + '\n')

os.system('pause')
os.system('cls')