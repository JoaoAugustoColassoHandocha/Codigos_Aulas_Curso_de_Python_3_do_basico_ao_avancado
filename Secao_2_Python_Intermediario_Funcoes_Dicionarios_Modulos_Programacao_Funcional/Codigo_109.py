'''
Raise - lançando exceções (erros)

'''

import os

os.system('color 1f')

print('\n##############################\n')

print(123)
# raise ValueError('Deu erro') # ValueError: Deu erro
print(456)

print('\n##############################\n')

def divide(n, d):
    
    try:
        
        return n / d
    
    except Exception:
        
        print('Erro!')
        
        raise

print(divide(8, 0))

print('\n##############################\n')

def divide(n, d):
    
    if n or d == 0:
        
        raise ZeroDivisionError('Você está tentando dividir por 0!')
          
    return n / d

print(divide(8, 0))

print('\n##############################\n')

def erro_divide_por_zero(n, d):
    
    if n or d == 0:
        
        raise ZeroDivisionError('Você está tentando dividir por 0!')
    
    return True

def divide(n, d):
    
    erro_divide_por_zero(n, d)      
    
    return n / d

print(divide(8, 0))

print('\n##############################\n')

os.system('pause')
os.system('cls')