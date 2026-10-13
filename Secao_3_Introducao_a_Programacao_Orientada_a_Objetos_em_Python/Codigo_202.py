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

import os

def mover(direcao):
    
    print(f'Movendo para {direcao}')

print('\n------------------------------\n')

mover('esquerda')
mover('direita')
mover('acima')
mover('abaixo')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')