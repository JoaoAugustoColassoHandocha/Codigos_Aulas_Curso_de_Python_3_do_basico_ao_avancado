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
    yield 2
    yield 3
    yield 4
    yield 5
    return 'Acabou' # Levanta uma excessão de StopIteration, quando é solicitado a execução do next() não tendo mais nada para executar, e exibe a mensagem inserida no return

gen = generator(numero = 0)
print(next(gen)) # 1
print(iter(gen)) # <generator object generator at 0x00000181753B5F00>

print('\n##############################\n')

for numero in gen:
    
    print(numero)

print('\n##############################\n')

os.system('pause')
os.system('cls')