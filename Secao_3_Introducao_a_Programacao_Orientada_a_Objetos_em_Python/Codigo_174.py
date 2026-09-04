'''
Exercício com classe:

1 - Crie uma classe Carro (Nome)

2 - Crie uma classe Motor (Nome)

3 - Crie uma classe Fabricante (Nome)

4 - Faça a ligação entre Carro tem um Motor
Obs.: Um motor pode ser de vários carros

5 - Faça a ligação entre Carro e um Fabricante
Obs.: Um fabricante pode fabricar vários carros

Exiba o nome do carro, motor e fabricante na tela

'''

import os

class Carro:
    
    def __init__(self, nome_carro):
        
        self._nome_carro = nome_carro
        
    def listar_carro(self):
        
        for carro in self._nome_carro:
        
            print(f'{carro}')
                
class Motor:
    
    def __init__(self):
        
        self._nome_motor = []
    
    def inserir_motor(self, *motores):
        
        self._nome_motor.extend(motores)
        
    def listar_motor(self):
        
        for motor in self._nome_motor:
            
            print(f'{motor}')
    
class Fabricante:
    
    def __init__(self, nome_fabricante, nome_motor, nome_carro):
        
        self._nome_fabricante = nome_fabricante
        self.motor = nome_motor
        self.carro = nome_carro        
        
    def inserir_fabricante(self, *fabricantes):
        
        self._nome_fabricante.extend(fabricantes)
        
    def listar_fabricante(self):
        
        for fabricante in self._nome_fabricante:
        
            print(f'{fabricante}')
            
fab = input('\nFabricante: ')
mot = input('\nMotor: ')
car = input('\nCarro: ')


    
print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')