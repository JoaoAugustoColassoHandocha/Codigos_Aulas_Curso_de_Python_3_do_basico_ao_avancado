'''
Update Codigo_188.py

Notas das exceptions em Python (add_notes, __notes__)

https://docs.python.org/3/library/exceptions.html

Levantando (raise) / Lançando (throw) exceções

Relançando exceções

'''

import os

class MyError(Exception): ...
    
class OtherError(Exception): ...
    
def levantar():
    
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    
    raise exception_

print('\n------------------------------\n')

try:
    
    levantar() # MyError: ('a', 'b', 'c')
    1 / 0 # ZeroDivisionError: ('division by zero')
    
except (MyError, ZeroDivisionError) as error:
    
    print(f'{error.__class__.__name__}: {error.args}')
    
    exception_ = OtherError('Vou lançar de novo.')
    exception_.add_note('Mais uma nota')
    exception_.__notes__ += error.__notes__.copy()
    
    raise exception_ from error

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')