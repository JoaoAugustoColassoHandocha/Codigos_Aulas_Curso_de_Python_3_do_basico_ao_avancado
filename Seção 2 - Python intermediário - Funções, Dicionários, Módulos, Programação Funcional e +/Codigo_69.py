'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

Refatorar - Editar o seu código.

'''

import os

os.system('color 1f')

def soma(x, y, z = None):
    
    if z is not None:
        
        print(f'\n{x = } + {y = } + {z = } = ', x + y + z)
        
    elif z is None:
        
        print(f'\n{x = } + {y = } = ', x + y)
        
    else:
        
        print('\nERRO! Favor contatar suporte!')
    
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)

print('\n')
os.system('pause')
os.system('cls')