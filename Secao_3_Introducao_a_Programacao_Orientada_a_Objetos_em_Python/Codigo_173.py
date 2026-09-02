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
        
        self.enderecos.append(Endereco(rua, numero))
        
    def listar_enderecos(self):
        
        for endereco in self.enderecos:
            
            print(f'{endereco.rua} - {endereco.numero}')
            
    def __del__(self):
        
        print(f'[AVISO] Apagando {self.nome}!')
        
class Endereco:
    
    def __init__(self, rua, numero):
        
        self.rua = rua
        self.numero = numero
        
    def __del__(self):
        
        print(f'[AVISO] Apagando {self.rua} - {self.numero}!')           
        
cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av. Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)

print('\n------------------------------\n')

cliente1.listar_enderecos()

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')