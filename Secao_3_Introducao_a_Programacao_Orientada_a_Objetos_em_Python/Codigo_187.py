'''
Update Codigo_187.py

https://docs.python.org/3/library/exceptions.html

Levantando (raise) / Lançando (throw) exceções

Relançando exceções

Adicionando notas em exceções (3.11.0)

'''

import os

class MyError(Exception):
    
    ...
    
def levantar():
    
    raise MyError('A mensagem do meu erro.')

print('\n------------------------------\n')

levantar()

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')