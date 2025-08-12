'''
Introdução ás Generator functions em Python

generator = (numero for numero in range(100))

yield: Pausa a execução

'''

import os

os.system('color 1f')

print('\n##############################\n')

def generator(numero = 0):
    
    yield 1
    return 'Acabou'

gen = generator(numero = 0)
print(next(gen))
print('\n')
print(iter(gen))

print('\n##############################\n')

os.system('pause')
os.system('cls')