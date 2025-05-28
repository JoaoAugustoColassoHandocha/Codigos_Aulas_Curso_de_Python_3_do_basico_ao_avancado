'''
Tipo tupla - Uma lista imutável

* Não é possível realizar a mudança de algum dado da lista

"nomes[1] = mudar" - Apresentará erro TypeError: 'tuple' object does not support item assignment.

tuple() - Função para transformar uma lista mutável em tupla.

list() - Função para transformar uma tupla em lista mutável.

'''

import os

os.system('color 1f')

nomes = ('Maria', 'Helena', 'Luiz')

print(f'\n{nomes}\n')
print(f'{nomes[1]}\n')

nome = ['Maria', 'Helena', 'Luiz']

print(f'{tuple(nome)}\n')

os.system('pause')
os.system('cls')