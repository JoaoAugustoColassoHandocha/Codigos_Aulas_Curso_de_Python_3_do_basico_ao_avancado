'''
Retorno de valores das funções (return).

'''

import os

os.system('color 1f')

def soma(x, y):
    
    if x > 10:
        
        return '\nNão foi possível somar, pois "X" é maior que 10.\n'
    
    if y > 10:
        
        return '\nNão foi possível somar, pois "Y" é maior que 10.\n'
    
    else:
    
        return f'\n{x + y}\n'

soma1 = soma(2, 2)
soma2 = soma(11, 3)
soma3 = soma(4, 11)

print(soma1)
print(soma2)
print(soma3)

os.system('pause')
os.system('cls')