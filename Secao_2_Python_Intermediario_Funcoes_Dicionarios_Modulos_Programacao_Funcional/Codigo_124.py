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
        
        res = func(*args, **kwargs) # soma(*args, **kwargs)
        
        return res
    
    return aninhada


def blablabla(a, b, c):
    
    print(a, b, c)

    return decoradora

@blablabla
def soma(x, y):
    
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

print('\n******************************\n')

os.system('pause')
os.system('cls')