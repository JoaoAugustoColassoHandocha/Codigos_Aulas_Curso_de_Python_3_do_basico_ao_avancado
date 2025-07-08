'''
args - Argumentos não nomeados

* - *args (empacotamento e desempacotamento)

'''

import os

os.system('color 1f')

# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(f'\n{x, y, resto}\n')

def soma_1(x, y):
    
    return x + y

os.system('pause')
os.system('cls')

###################

def soma_2(*args):
    
    args = list(args)
    print(args, type(args))
    
soma_2(1, 2, 3, 4, 5)

os.system('pause')
os.system('cls')

###################

def soma_3(*args):
    
    total = 0
    
    for numero in args:
        
        print(f'{total} + {numero}')
        total += numero
        print(f'Total: {total}')
        print('\n')

print('\n')
soma_3(1, 2, 3, 4, 5)

os.system('pause')
os.system('cls')