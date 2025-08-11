'''
Generator expression, Iterables e Iterators em Python

Iterable: Tem a responsabilidade de ter os valores sequencialmente.
Iterator: Tem a responsabilidade de entregar um valor por vez.

Under: __xxx__

Generator expression: São funções que sabem pausar em determinada ocasião.

'''

import os

os.system('color 1f')

print('\n##############################\n')

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [numero for numero in range(100)]
generator = (numero for numero in range(100))

print('\n##############################\n')

os.system('pause')
os.system('cls')