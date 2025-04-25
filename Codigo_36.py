'''
Iterando strings com while

'''

import os

os.system('color 1f')

nome = input('Nome: ')
tamanho_nome = len(nome)
x = 0
nome_atualizado = ''

while x < tamanho_nome:
    
    letra = nome[x]
    nome_atualizado += f'*{letra}'
    
    x += 1

nome_atualizado += '*'

print(nome_atualizado)
os.system('pause')
os.system('cls')