'''
Conversão de funções para lambda

'''

import os

os.system('color 1f')

def executa(funcao, *args):
    
    return funcao(*args)


def cria_multiplicador(multiplicador):
    
    def multiplica(numero):
        
        return numero * multiplicador
    
    return multiplica

def soma(x, y):
    
    return x + y

#########################################

# Função def soma convertida para lambda

# Lambda seria a mesma coisa que def

print(executa(lambda x, y: x + y, 2, 3))

os.system('pause')
os.system('cls')