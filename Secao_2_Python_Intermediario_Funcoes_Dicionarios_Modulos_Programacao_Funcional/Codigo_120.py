'''
EXERCÍCIO

* Adiando execução de funções

'''

import os

os.system('color 1f')

print('\n******************************\n')

def soma(x, y):
    
    return x + y

def multiplica(x, y):
    
    return x * y

def executa(funcao, x):
    
    def interna(y):
        
        return funcao(x, y)
    
    return interna

num = int(input('Digite um número: '))

soma_com_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica, 10)

print(f'A soma de 5 + {num} é {soma_com_cinco(num)}')
print(f'A multiplicação de 10 * {num} é {multiplica_por_dez(num)}')

print('\n******************************\n')

os.system('pause')
os.system('cls')