'''
Decoradores com parâmetros

'''

import os

os.system('color 1f')

print('\n******************************\n')

def decoradora(func):
    
    print('Decoradora 1')
    
    def aninhada(*args, **kwargs):
        
        print('Aninhada')
        
        res = func(*args, **kwargs)
        
        return res
    
    return aninhada

@decoradora
def soma(x, y):
    
    return x + y

print('\n******************************\n')

os.system('pause')
os.system('cls')