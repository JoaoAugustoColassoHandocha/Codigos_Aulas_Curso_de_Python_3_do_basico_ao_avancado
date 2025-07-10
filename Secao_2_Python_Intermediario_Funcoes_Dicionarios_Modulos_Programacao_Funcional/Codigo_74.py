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
    par_ou_impar = ''
    
    for numero in args:
        
        total *= numero
        
        def par_impar(total, par_ou_impar):
            
            if total % 2 == 0:
                
                par_ou_impar = 'Par'
            
            elif total % 2 != 0:
                
                par_ou_impar = 'Impar'
                
        par_impar()
        
    return total, par_ou_impar

multi_dados = multi(1, 2, 3, 4, 5)
    
os.system('pause')
os.system('cls')