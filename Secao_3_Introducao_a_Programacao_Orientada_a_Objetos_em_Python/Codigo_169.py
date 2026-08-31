'''
@property + @setter - getter e setter no modo Pythônico

- como getter -> Obtendo valor
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo

Atributos que começar com um ou dois underlines não devem ser usados fora da classe.

'''

import os

print('\n------------------------------\n')

class Caneta:
    
    def __init__(self, cor):
        
        self._cor = cor
        
    @property
    def cor(self):
        
        print('PROPERTY')
        return self._cor
    
caneta = Caneta('Azul')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')