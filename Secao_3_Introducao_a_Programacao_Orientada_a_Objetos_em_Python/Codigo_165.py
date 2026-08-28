'''
Métodos de classe

São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, recebemosa própria classe.

'''

import os

print('\n------------------------------\n')

class Pessoa:
    
    ano = 2023 
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')