'''
Retorno de valores das funções (return).

'''

import os

os.system('color 1f')

def soma(x, y):
    
    if x > 10:
        
        return 'Não foi possível somar, pois "X" é maior que 10'
    
    if y > 10:
        
        
    
    return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(f'\n{soma1 + soma2}\n')

os.system('pause')
os.system('cls')