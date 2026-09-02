'''
Relações entre classes: associação, agregação e composição

Composição é uma especialização da agregação.

Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.

'''

import os

class Cliente:
    
    def __init__(self, nome):
        
        self.nome = nome
        self.enderecos = []
        
    def inserir_endereco(self, rua, numero):
        
        self.enderecos.append()

print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')