'''
__new__ e __init__ em classes Python

__new__ é o método responsável por criar e retornar o novo objeto.

Por isso, new recebe cls.

__new__ ❗️DEVE retornar o novo objeto❗️

__init__ é o método responsável por inicializar a instância.

Por isso, init recebe self.

__init__ ❗️NÃO DEVE retornar nada (None)❗️

object é a super classe de uma classe

'''

import os

class A:
    
    def __new__(cls, y):
        
        print('Antes de criar a inst')
        
        instancia = super().__new__(cls)
        
        print('Depois de criar a inst')
        
        instancia.x = 213
        
        return instancia
    
    def __init__(self, y):
        
        self.y = y
        print('Sou o init')
        
    def __repr__(self):
        
        return 'A()'

print('\n------------------------------\n')

a = A(123)
print(a.x)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')