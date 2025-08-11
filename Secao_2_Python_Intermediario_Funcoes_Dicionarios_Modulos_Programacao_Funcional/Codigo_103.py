'''
Generator expression, Iterables e Iterators em Python

Iterável: Tem a responsabilidade de ter os valores sequencialmente.
Iterator: Tem a responsabilidade de entregar um valor por vez.

'''

import os

os.system('color 1f')

print('\n##############################\n')

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # Tem __iter__ e __next__

print(next(iterator))

print('\n##############################\n')

os.system('pause')
os.system('cls')