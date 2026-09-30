'''
Update Codigo_191.py

Exemplo de uso de dunder methods (métodos mágicos)

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
__str__(self) - str
__repr__(self) - str

'''

import os

class Ponto:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
    def __repr__(self):
        
        class_name = type(self).__name__
        return f'{class_name}(x = {self.x!r}, y = {self.y!r})'
    
    def __add__(self, other):
        
        return 'Bola'

print('\n------------------------------\n')

if __name__ == '__main__':
    
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)
    p3 = p1 + p2
    print(p3)
    # print('P1 é maior que P2', p1 > p2)
    # print('P2 é maior que P1', p2 > p1)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')