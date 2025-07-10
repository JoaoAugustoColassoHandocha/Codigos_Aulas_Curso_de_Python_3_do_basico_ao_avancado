'''
Exercícios com função - RESOLUÇÂO

Crie uma função que multiplica todos os argumentos não nomeados recebidos.

Retorne o total para uma variável e mostre o valor da variável.

Crie uma função fala se um número é par ou ímpar.

Retorne se o número é par ou ímpar.

'''

import os

os.system('color 1f')

def multiplicar(*args):
    
    total = 1
    
    for numero in args:
        
        total *= numero
        
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)

print(f'\n{multiplicacao} - {}\n')

os.system('pause')
os.system('cls')