'''
Update Codigo_197.py

Método especial __call__

callable é algo que pode ser executado com parênteses

Em classes normais, __call__ faz a instância de uma classe "callable".

'''

import os

class CallMe:
    
    def __init__(self, phone):
        
        self.phone = phone
        
call1 = CallMe('23945876545')

print('\n------------------------------\n')

call1()

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')