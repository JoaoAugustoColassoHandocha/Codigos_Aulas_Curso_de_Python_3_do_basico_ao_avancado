'''
Update Codigo_187.py

https://docs.python.org/3/library/exceptions.html

Levantando (raise) / Lançando (throw) exceções

Relançando exceções

Adicionando notas em exceções (3.11.0)

'''

import os

class MyError(Exception): ...
    
class OtherError(Exception): ...
    
def levantar():
    
    exception_ = MyError('a', 'b', 'c')
    
    raise exception_

print('\n------------------------------\n')

try:
    
    levantar() # MyError: ('a', 'b', 'c')
    1 / 0 # ZeroDivisionError: ('division by zero')
    
except (MyError, ZeroDivisionError) as error:
    
    print(f'{error.__class__.__name__}: {error.args}')
    
    exception_ = OtherError()
    
    raise 

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')