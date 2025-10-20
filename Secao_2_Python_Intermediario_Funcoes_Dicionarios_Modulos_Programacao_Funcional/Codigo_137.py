'''


'''

import os

os.system('color 1f')

def recursiva(inicio = 0, fim = 10):

    print(inicio, fim)
    
    # Caso Base
    if inicio >= fim:
        
        return fim
    
    # Caso recursivo - contar até chegar ao final
    inicio += 1
    
    return recursiva(inicio, fim)

print('\n******************************\n')

recursiva()

print('\n******************************\n')

os.system('pause')
os.system('cls')