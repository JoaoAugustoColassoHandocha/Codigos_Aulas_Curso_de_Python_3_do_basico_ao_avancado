'''


'''

import os, sys

sys.setrecursionlimit(1004)

os.system('color 1f')

def recursiva(inicio = 0, fim = 10):

    print(inicio, fim)
    
    # Caso Base
    if inicio >= fim:
        
        return fim
    
    # Caso recursivo - contar até chegar ao final
    inicio += 1
    
    return recursiva(inicio, fim)

####################################################

def factorial(n):
    
    

print('\n******************************\n')

recursiva(0, 1000)

print('\n******************************\n')

os.system('pause')
os.system('cls')