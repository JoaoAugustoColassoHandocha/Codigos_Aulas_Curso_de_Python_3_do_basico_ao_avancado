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
        self.carro = []
        self.motor = []
        
    def inserir_carro(self, nome_carro):
            
        self.carro.append(Carro(nome_carro))
        
    def inserir_motor(self, nome_motor):
        
        self.motor.append(Motor(nome_motor))
        
    def listar_fabricante(self):
        
        print(f'{self.nome_fabricante}')
        
class Motor:
    
    def __init__(self, nome_motor):
        
        self.nome_motor = nome_motor
        
class Carro:
    
    def __init__(self, nome_carro):
        
        self.nome_carro = nome_carro
            
fab = input('\nFabricante: ')
mot = input('\nMotor: ')
car = input('\nCarro: ')


    
print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')