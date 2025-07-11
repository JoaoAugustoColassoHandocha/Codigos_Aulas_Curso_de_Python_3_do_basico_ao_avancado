'''
Exercícios com função

Crie uma função que multiplica todos os argumentos não nomeados recebidos.

Retorne o total para uma variável e mostre o valor da variável.

Crie uma função fala se um número é par ou ímpar.

Retorne se o número é par ou ímpar.

'''

import os

os.system('color 1f')

def multi(*args):
    
    total = 1
    
    for numero in args:
        
        total *= numero
    
    return total

def par_impar(multi_dados):
    
    if multi_dados % 2 == 0:
        
        return '"Par"'
    
    elif multi_dados % 2 != 0:
        
        return '"Impar"'
    
    else:
        
        return '(Erro ao processar!)'

multi_dados = multi(1, 2, 3, 4, 5)
par_ou_impar = par_impar(multi_dados)

print(f'\nA multiplicação de 1 X 2 X 3 X 4 X 5 = {multi_dados}, sendo {par_ou_impar}.\n')

os.system('pause')
os.system('cls')