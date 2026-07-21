'''
Métodos em instâncias de classes Python.

Hard Coded - É algo que foi escrito diretamente no código.

'''

import os

print('\n------------------------------\n')

class Carro:
    
    def __init__(self, nome):
        
        self.nome = nome
        
    def acelerar(self):
        
          print(f'{self.nome} está acelerando...')  
        
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')