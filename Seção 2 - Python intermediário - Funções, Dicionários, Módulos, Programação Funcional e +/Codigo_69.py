'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

Refatorar - Editar o seu código.

'''

import os

os.system('color 1f')

def soma(x, y):
    
    print(x + y)
    
soma(1, 2)
soma(3, 5)
soma(100, 200)

os.system('pause')
os.system('cls')