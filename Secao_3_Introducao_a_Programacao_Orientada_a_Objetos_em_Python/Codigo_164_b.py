'''


'''

import os, json
from Codigo_164_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

print('\n------------------------------\n')

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    
    pessoas = json.load(arquivo)
    
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')