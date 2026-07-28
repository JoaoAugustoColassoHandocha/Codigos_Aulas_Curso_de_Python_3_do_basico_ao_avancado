'''
atributos de classe

'''

import os, time
from datetime import datetime

print('\n------------------------------\n')

class Pessoa:
    
    atributo = 'valor'
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        
        return datetime.now() - self.idade
        

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')