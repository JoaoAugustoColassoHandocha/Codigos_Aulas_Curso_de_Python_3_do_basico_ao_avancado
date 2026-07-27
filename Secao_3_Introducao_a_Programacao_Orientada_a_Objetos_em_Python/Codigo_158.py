'''



'''

import os

print('\n------------------------------\n')

class Carro:
    
    def __init__(self, nome):
        
        self.nome = nome
        
    def acelerar(self):
        
          print(f'{self.nome} está acelerando...') 

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')