'''
Higher Order Functions
Funções de primeira classe

'''

import os

os.system('color 1f')

def saudacao(msg, nome):
    
    return f'{msg}, {nome}!'

# O *args está recebendo o restante dos dados e compactando
def executa(funcao, *args):
    
    # Aqui o *args está descompactando os dados resebidos
    return funcao(*args)

print(f'\n{executa(saudacao, 'Bom dia', 'João')}\n')

os.system('pause')
os.system('cls')