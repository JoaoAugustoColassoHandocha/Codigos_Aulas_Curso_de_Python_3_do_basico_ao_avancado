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

print(f'\n{multiplicacao}\n')

os.system('pause')
os.system('cls')

######################

def par_impar(numero):
    
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        
        return f'{numero} é par'
    
    return f'{numero} é impar'

print(f'\n{par_impar(2)}\n')
print(f'{par_impar(3)}\n')
print(f'{par_impar(15)}\n')
print(f'{par_impar(16)}\n')

os.system('pause')
os.system('cls')