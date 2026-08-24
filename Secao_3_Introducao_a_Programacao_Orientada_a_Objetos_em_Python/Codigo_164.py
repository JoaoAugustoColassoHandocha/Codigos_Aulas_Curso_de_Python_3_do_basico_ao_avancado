'''
Exercício:

Salve os dados da sua classe em JSON, e depois crie novamente as instâncias da classe com os dados salvos.

Faça em arquivos separados.

'''

import os, json

print('\n------------------------------\n')

CAMINHO_ARQUIVO = 'Codigo_164.json'

class Pessoa:
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('João', 33)
p1 = Pessoa('Helena', 21)
p1 = Pessoa('Joana', 11)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')