'''
Generator expression, Iterables e Iterators em Python

Iterable: Tem a responsabilidade de ter os valores sequencialmente.
Iterator: Tem a responsabilidade de entregar um valor por vez.

Under: __xxx__

Generator expression: São funções que sabem pausar em determinada ocasião.

'''

import os, sys

os.system('color 1f')

print('\n##############################\n')

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [numero for numero in range(100)]
generator = (numero for numero in range(100)) # Generator expression

# sys.getsizeof: Ver o tamanho da lista em bytes na memória

print(f'{sys.getsizeof(lista)} bytes') # 920 bytes
print('\n')
print(f'{sys.getsizeof(generator)} bytes') # 192 bytes

print('\n##############################\n')

os.system('pause')
os.system('cls')