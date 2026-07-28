'''
atributos de classe

'''

import os

print('\n------------------------------\n')

class Pessoa:
    
    atributo = 'valor'
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade
        

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')