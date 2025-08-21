'''
Raise - lançando exceções (erros)

* https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

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

# print(divide(8, 0))

print('\n##############################\n')

def divide(n, d):
    
    if n == 0 or d == 0:
        
        raise ZeroDivisionError('Você está tentando dividir por 0!')
          
    return n / d

# print(divide(8, 0))

print('\n##############################\n')

def erro_divide_por_zero(n, d):
    
    if n == 0 or d == 0:
        
        raise ZeroDivisionError('Você está tentando dividir por 0!')
    
    return True

def divide(n, d):
    
    erro_divide_por_zero(n, d)      
    
    return n / d

# print(divide(8, 0))

print('\n##############################\n')

def int_or_float(n):
    
    type_n = type(n)
    
    if not isinstance(n, (float, int)):
        
        raise TypeError(
            
            f'"{n}" deve ser inteiro ou flutuante! '
            f'"{type_n.__name__}" enviado.'
            
            )

def erro_divide_por_zero(n, d):
    
    if n == 0 or d == 0:
        
        raise ZeroDivisionError('Você está tentando dividir por 0!')
    
    return True

def divide(n, d):
    
    int_or_float(n)
    int_or_float(d)
    
    erro_divide_por_zero(n, d)      
    
    return n / d

# print(divide(8, 0))

print('\n##############################\n')

os.system('pause')
os.system('cls')