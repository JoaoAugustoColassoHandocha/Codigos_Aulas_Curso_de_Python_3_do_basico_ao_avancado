'''
Update Codigo_183.py

abstractmethod para qualquer método já decorado (@property e setter)

É possível criar @property @property.setter @classmethod @staticmethod e métodos normais como abstratos, para isso use @abstractmethod como decorator mais interno.

Foo - Bar são palavras usadas como placeholder para palavras que podem mudar na programação.

'''

import os
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    
    def __init__(self, name):
        
        self.name = name
        
    @property
    def name(self):
        
        return 123
    
    @name.setter
    def name(self, name): ...
    
class Foo(AbstractFoo):
    
    def __init__(self, name):
        
        super().__init__(name)

foo = Foo('Bar')
print(foo.name)

print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')