'''
Funções decoradoras e decoradores

Decorar = Adicionar / Remover / Restringir / Alterar

Funções decoradoras são funções que decoram outras funções

Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.

'''

import os

os.system('color 1f')

print('\n******************************\n')

def inverte_string(string):
    
    return string[::-1]

invertida = inverte_string('Joao')

print(invertida)

print('\n******************************\n')



print('\n******************************\n')

os.system('pause')
os.system('cls')