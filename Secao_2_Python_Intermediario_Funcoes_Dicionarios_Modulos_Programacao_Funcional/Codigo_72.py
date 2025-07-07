'''
args - Argumentos não nomeados

* - *args (empacotamento e desempacotamento)

'''

import os

os.system('color 1f')

# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    
    return x + y

os.system('pause')
os.system('cls')

###################

def soma(*args):
    
    args = list(args)
    print(args, type(args))
    
soma(1, 2, 3, 4, 5)

os.system('pause')
os.system('cls')

###################

