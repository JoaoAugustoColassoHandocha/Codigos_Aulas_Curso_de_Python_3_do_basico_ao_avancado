'''
__dict__ e vars para atributos de instância

del p1.nome - exclui a chave

'''

import os
from datetime import date

print('\n------------------------------\n')

class Pessoa:
    
    ano_atual = date.today().year 
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
               
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(f'Ano Atual: {Pessoa.ano_atual}')
print(f'Ano de nascimento p1: {p1.get_ano_nascimento()}')
print(f'Ano de nascimento p2: {p2.get_ano_nascimento()}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')