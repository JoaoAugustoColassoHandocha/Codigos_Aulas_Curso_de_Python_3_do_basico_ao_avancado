'''
List comprehension em Python

List comprehension é uma forma rápida para criar listas a partir de iteráveis.

------------------

print(list(range(10))) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

------------------

lista - []

for numero in range(10):

    lista.append(numero)
    
print(lista) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

------------------

lista = [variável for vareavel range(10)]

'''

import os

os.system('color 1f')

print('\n##############################\n')

lista = [numero for numero in range(10)]
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('\n##############################\n')

lista = [numero * 2 for numero in range(10)]
print(lista) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print('\n##############################\n')

os.system('pause')
os.system('cls')