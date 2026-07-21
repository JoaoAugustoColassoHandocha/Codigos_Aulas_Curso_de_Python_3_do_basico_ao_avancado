'''
Métodos em instâncias de classes Python.

Hard Coded - É algo que foi escrito diretamente no código.

'''

import os

print('\n------------------------------\n')

class Carro:
    def __init__(self, alguma_coisa = 'Sei lá'):
        self.nome = alguma_coisa
        
    

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')