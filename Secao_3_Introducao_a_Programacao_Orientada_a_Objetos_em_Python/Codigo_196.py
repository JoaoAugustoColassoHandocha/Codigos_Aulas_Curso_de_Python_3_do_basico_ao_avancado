'''
Update Codigo_196.py

Funções decoradoras e decoradores com classes

'''

import os

def my_repr(self):
            
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):

    cls.__repr__ = my_repr
    return cls

def meu_planeta(metodo):
    
    def interno(self, *args, **kwargs)

@adiciona_repr
class Time:
    
    def __init__(self, nome):
        
        self.nome = nome
        
@adiciona_repr
class Planeta:
    
    def __init__(self, nome):
        
        self.nome = nome
        
    def falar_nome(self):
        
        return f'O planeta é {self.nome}'

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print('\n------------------------------\n')

print(f'{brasil}\n')
print(f'{portugal}\n')
print(f'{terra}\n')
print(f'{marte}\n')
print(f'{terra.falar_nome()}\n')
print(f'{marte.falar_nome()}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')