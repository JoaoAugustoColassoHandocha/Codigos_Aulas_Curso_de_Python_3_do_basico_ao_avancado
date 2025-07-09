'''


'''

import os

os.system('color 1f')

# Empacotamento do que é enviado para função dentro de uma tupla.
def soma(*args):
    
    total = 0
    
    for numero in args:
        
        total += numero
        
    return total

soma_12345 = soma(1, 2, 3, 4, 5)
print(f'\nSoma de 1, 2, 3, 4 e 5 fica {soma_12345}.\n')

os.system('pause')
os.system('cls')

#########################

# Desempacotamento uma tupla para função.
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
outra_soma = soma(*numeros)

print(f'\n{outra_soma}\n')

print(f'{sum(numeros)}\n')

os.system('pause')
os.system('cls')