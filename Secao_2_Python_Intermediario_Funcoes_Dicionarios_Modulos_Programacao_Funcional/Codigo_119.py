'''
EXERCÍCIO

* Adiando execução de funções

funções, clojure

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

num = int(input('Digite um número: '))

soma_com_cinco = executa(soma, 5)

multiplica_por_dez = executa(multiplica, 10)

for numero in num:
    
    print(f'A soma de 5 + {num} é {soma_com_cinco(numero)}')
    print(f'A multiplicação de 10 * {num} é {multiplica_por_dez(numero)}')

print('\n******************************\n')

os.system('pause')
os.system('cls')