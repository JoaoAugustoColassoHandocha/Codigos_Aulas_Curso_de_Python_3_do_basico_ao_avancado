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

class Fabricante:
    
    def __init__(self, nome_fabricante):
        
        self.nome_fabricante = nome_fabricante
        self.carro = None
        self.motor = None
        
    def inserir_carro(self, nome_carro):
            
        self.carro.append(Carro(nome_carro))
        
    def inserir_motor(self, nome_motor):
        
        self.motor.append(Motor(nome_motor))
        
    def inserir_fabricante(self, nome_fabricante):
        
        self.nome_fabricante.append(nome_fabricante)
        
    def listar(self):
        
        print(f'Carro: {self.inserir_carro}\nFabricante: {self.inserir_fabricante}\nMotor: {self.inserir_motor}')
        
class Motor:
    
    def __init__(self, nome_motor):
        
        self.nome_motor = nome_motor
        
class Carro:
    
    def __init__(self, nome_carro):
        
        self.nome_carro = nome_carro

info_car = Fabricante('')            
info_car.inserir_carro = input('\nCarro: ')
info_car.inserir_motor = input('\nMotor: ')
info_car.inserir_fabricante = input('\nFabricante: ')
    
print('\n------------------------------\n')

info_car.listar()

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')