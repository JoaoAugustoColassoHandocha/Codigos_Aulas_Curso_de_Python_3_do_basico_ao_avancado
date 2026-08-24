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
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

bd = [p1, p2, p3]

with open(CAMINHO_ARQUIVO, 'W') as arquivo:
    
    json.dump(bd, arquivo, ensure_ascii = False, indent = 2)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')