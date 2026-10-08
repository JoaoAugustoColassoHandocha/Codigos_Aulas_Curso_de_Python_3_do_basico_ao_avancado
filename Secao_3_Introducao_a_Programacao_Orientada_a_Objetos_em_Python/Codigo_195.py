'''
Update Codigo_195.py

Funções decoradoras e decoradores com classes

'''

import os

class Time:
    
    def __init__(self, nome):
        
        self.nome = nome
        
class Planeta:
    
    def __init__(self, nome):
        
        self.nome = nome

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print('\n------------------------------\n')

print(f'{}\n')
print(f'{}\n')
print(f'{}\n')
print(f'{}\n')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')