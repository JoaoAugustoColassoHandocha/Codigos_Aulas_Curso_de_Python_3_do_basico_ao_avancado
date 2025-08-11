'''
Generator expression, Iterables e Iterators em Python

Iterable: Tem a responsabilidade de ter os valores sequencialmente.
Iterator: Tem a responsabilidade de entregar um valor por vez.

Under: __xxx__

'''

import os

os.system('color 1f')

print('\n##############################\n')

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # Tem __iter__ e __next__

print(iterator.__next__) # Saber o próximo valor

print('\n##############################\n')

# Outra forma

iterator = iter(iterable)
print(next(iterator)) # Eu
print(next(iterator)) # Tenho
print(next(iterator)) # __iter__

print('\n##############################\n')

os.system('pause')
os.system('cls')