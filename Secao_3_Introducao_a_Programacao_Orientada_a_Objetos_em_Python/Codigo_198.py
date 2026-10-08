'''
Update Codigo_198.py

Classes decoradoras (Decorator classes)

'''

import os

class Multiplicar:
    
    def __init__(self, func):
        
        self.func = func
        self._multiplicador = 10
        
    def __call__(self, *args, **kwargs):
        
        print(args, kwargs)
        
        resultado = self.func(*args, **kwargs)
        
        return resultado

@Multiplicar
def soma(x, y):
    
    return x + y

dois_mais_dois = soma(2, 2)

print('\n------------------------------\n')

print(dois_mais_dois)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')