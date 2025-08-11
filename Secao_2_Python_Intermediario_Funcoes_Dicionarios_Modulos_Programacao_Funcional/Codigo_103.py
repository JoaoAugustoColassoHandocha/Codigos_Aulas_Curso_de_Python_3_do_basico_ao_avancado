'''
Generator expression, Iterables e Iterators em Python

Iterável: Tem a responsabilidade de ter os valores sequencialmente.
Iterator: Tem a responsabilidade de entregar um valor por vez.

Under: __

'''

import os

os.system('color 1f')

print('\n##############################\n')

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # Tem __iter__ e __next__

print(next(iterator)) # Saber o próximo valor

print('\n##############################\n')

iterator = iter(iterable) # Tem __iter__ e __next__

print('\n##############################\n')

os.system('pause')
os.system('cls')