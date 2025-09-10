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

num = int(input('Digite um número: '))

soma_com_cinco = executa(soma, 5, num)
multiplica_por_dez = executa(multiplica, 10, num)
 
print(f'A soma de 5 + {num} é {soma_com_cinco}')
print(f'A multiplicação de 10 * {num} é {multiplica_por_dez}')

print('\n******************************\n')

os.system('pause')
os.system('cls')