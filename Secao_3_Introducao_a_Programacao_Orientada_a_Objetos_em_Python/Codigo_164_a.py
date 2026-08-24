'''
Exercício:

Salve os dados da sua classe em JSON, e depois crie novamente as instâncias da classe com os dados salvos.

Faça em arquivos separados.

'''

import os, json

print('\n------------------------------\n')

CAMINHO_ARQUIVO = '/workspaces/Codigos_Aulas_Curso_de_Python_3_do_basico_ao_avancado/Secao_3_Introducao_a_Programacao_Orientada_a_Objetos_em_Python/Codigo_164.json'

class Pessoa:
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

bd = [p1.__dict__, p2.__dict__, p3.__dict__]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    
    json.dump(bd, arquivo, ensure_ascii = False, indent = 2)
    
print('Dados salvos!')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')