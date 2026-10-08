'''
Update Codigo_195.py

Funções decoradoras e decoradores com classes

'''

import os

def adiciona_repr(cls):
        
    def my_repr(self):
            
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

    cls.__repr__ = my_repr
    return cls
@adiciona_repr
class Time:
    
    def __init__(self, nome):
        
        self.nome = nome
        
@adiciona_repr
class Planeta:
    
    def __init__(self, nome):
        
        self.nome = nome

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print('\n------------------------------\n')

print(f'{brasil}\n')
print(f'{portugal}\n')
print(f'{terra}\n')
print(f'{marte}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')