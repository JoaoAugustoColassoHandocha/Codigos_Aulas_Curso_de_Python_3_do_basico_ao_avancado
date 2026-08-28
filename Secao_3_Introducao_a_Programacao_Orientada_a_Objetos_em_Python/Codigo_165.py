'''
Métodos de classe + factories (fábricas)

São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, recebemosa própria classe.

@classmethod - Em vez de receber o argumento self (que aponta para um objeto criado), ele recebe o argumento cls (que aponta para a própria classe).

'''

import os

print('\n------------------------------\n')

class Pessoa:
    
    ano = 2023 # Atributo de classe
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade

    @classmethod        
    def metodo_de_classe(cls):
        
        print('\nHey')
        
    @classmethod
    def criar_com_50_anos(cls, nome):
        
        return cls(nome, 50)
        
p1 = Pessoa('João', 34)
print(Pessoa.ano)
Pessoa.metodo_de_classe()

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')