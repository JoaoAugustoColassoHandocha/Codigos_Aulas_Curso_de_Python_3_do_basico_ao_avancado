'''
Generator expression, Iterables e Iterators em Python

Iterable: Tem a responsabilidade de ter os valores sequencialmente.
Iterator: Tem a responsabilidade de entregar um valor por vez.

Under: __xxx__

Generator expression: São funções que sabem pausar em determinada ocasião.

A diferença da lista para o generator expression é que a lista está toda na memória e o generator está esperando pedir um valor.

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

print(next(generator)) # 0
print(next(generator)) # 1
print(next(generator)) # 2

print('\n##############################\n')

for numero in generator:
    
    print(numero)

print('\n##############################\n')

print([numero for numero in generator])

print('\n##############################\n')

os.system('pause')
os.system('cls')