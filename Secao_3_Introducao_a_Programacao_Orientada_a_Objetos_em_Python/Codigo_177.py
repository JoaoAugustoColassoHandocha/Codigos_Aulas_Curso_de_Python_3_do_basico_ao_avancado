'''
Herança simples - Relações entre classes

Associação - usa

Agregação - tem

Composição - É dono de

Herança - É um

Herança vs Composição

Classe principal (Pessoa) -> super class, base class, parent class

Classes filhas (Cliente) -> sub class, child class, derived class

help(NomeDaClasse) - Verifica sua classe
 
'''

import os

class Pessoa:
    
    def __init__(self, nome, sobrenome):
        
        self.nome = nome
        self.sobrenome = sobrenome
    
print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')