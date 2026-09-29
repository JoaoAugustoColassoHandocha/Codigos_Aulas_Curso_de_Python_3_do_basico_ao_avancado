'''
Update Codigo_190.py

Python Dunder Methods __repr__ e __str__

Dunder = Double Underscore = __dunder__

Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#specialnames

__lt__(self,other) - self < other
__le__(self,other) - self <= other
__gt__(self,other) - self > other
__ge__(self,other) - self >= other
__eq__(self,other) - self == other
__ne__(self,other) - self != other
__add__(self,other) - self + other
__sub__(self,other) - self - other
__mul__(self,other) - self * other
__truediv__(self,other) - self / other
__neg__(self) - -self
__str__(self) - str (Mais para representação de string)
__repr__(self) - str (Mais para desenvolvedor, passando como é que o objeto seja criado)

'''

import os

class Ponto:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

    def __str__(self):
        
        return f'({self.x}, {self.y})' # (1, 2) (978, 876)
    
    def __repr__(self):
        
        class_name = type(self).__name__ # Igual a self.__class__.__name__
        
        return f'{class_name}(x = {self.x}, y = {self.y})'
        
p1 = Ponto(1, 2)
p2 = Ponto(978, 876)

print('\n------------------------------\n')

print(p1)
print(p2)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')