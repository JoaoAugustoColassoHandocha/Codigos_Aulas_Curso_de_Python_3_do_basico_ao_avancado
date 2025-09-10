'''
EXERCÍCIO

* Adiando execução de funções

funções, clojure

77, 76

'''

import os

os.system('color 1f')

print('\n******************************\n')

def soma(x, y):
    
    return x + y

def multiplica(x, y):
    
    return x * y

def executa(funcao, *args):
    
    return funcao(*args)

num1 = int(input('Digite um número: '))

soma_com_cinco_1 = executa(soma, 5, num1)
multiplica_por_dez_1 = executa(multiplica, 10, num1)
 
print(f'A soma de 5 + {num1} é {soma_com_cinco_1}')
print(f'A multiplicação de 10 * {num1} é {multiplica_por_dez_1}')

print('\n******************************\n')

os.system('pause')
os.system('cls')