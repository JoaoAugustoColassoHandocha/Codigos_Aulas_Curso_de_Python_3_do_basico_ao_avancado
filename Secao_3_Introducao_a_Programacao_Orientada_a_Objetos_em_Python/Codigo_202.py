'''
Update Codigo_202.py

Enum -> Enumerações

Enumerações na programação, são usadas em ocasiões onde temos um determinado número de coisas para escolher.

Enums têm membros e seus valores são constantes.

Enums em python:

    - são um conjunto de nomes simbólicos (membros) ligados a valores únicos

    - podem ser iterados para retornar seus membros canônicos na ordem de definição

enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada diretamente (mesmo assim, Enums não são classes normais em Python).

Você poderá usar seu Enum com type annotations, com isinstance e outras coisas relacionadas com tipo.

Para obter os dados:

membro = Classe(valor), Classe['chave']
chave = Classe.chave.name
valor = Classe.chave.value

'''

lazy import os, enum

class Direcoes(enum.Enum):
    
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

direcoes = enum.Enum('direcoes', ['ESQUERDA', 'DIREITA', 'ACIMA', 'ABAIXO'])

print(f'\n{direcoes(1), direcoes['ESQUERDA'], direcoes.ESQUERDA}')
print(f'\n{direcoes.ESQUERDA.name, direcoes.ESQUERDA.value}')

def mover(direcao: Direcoes):
    
    if not isinstance(direcao, direcoes):
        
        raise ValueError('Direção não encontrada!')
    
    print(f'Movendo para {direcao.name} ({direcao.value})')

print('\n------------------------------\n')

mover(direcoes.ESQUERDA)
mover(direcoes.DIREITA)
mover(direcoes.ACIMA)
mover(direcoes.ABAIXO)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')