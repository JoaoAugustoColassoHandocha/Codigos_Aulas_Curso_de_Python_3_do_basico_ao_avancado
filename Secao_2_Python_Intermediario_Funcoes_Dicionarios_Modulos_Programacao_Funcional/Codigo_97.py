'''
Filtro de dados em list comprehension

'''

import os

os.system('color 1f')

print('\n##############################\n')

lista = [numeros for numeros in range(10) if numeros < 5]
print(lista)

print('\n##############################\n')

os.system('pause')
os.system('cls')