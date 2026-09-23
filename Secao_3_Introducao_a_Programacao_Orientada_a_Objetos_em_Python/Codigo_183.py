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
        
        self._name = None
        self.name = name
    
    @property
    @abstractmethod    
    def name(self): ...
    
class Foo(AbstractFoo):
    
    def __init__(self, name):
        
        super().__init__(name)
        
    @property    
    def name(self):
        
        return self._name
    
    @name.setter
    def name(self, name):
        
        self._name = name

foo = Foo('Bar')

print('\n------------------------------\n')

print(foo.name)

print('\n------------------------------\n')
input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')