'''
Conversão de funções para lambda

def executa(funcao, *args):
    
    return funcao(*args)


def cria_multiplicador(multiplicador):
    
    def multiplica(numero):
        
        return numero * multiplicador
    
    return multiplica

def soma(x, y):
    
    return x + y

'''

import os

os.system('color 1f')

# Função def soma convertida para lambda

# Lambda seria a mesma coisa que def

print('\n#########################################\n')
print(executa(lambda x, y: x + y, 2, 3)) # executa seria o nome da função (como se fosse a criação de uma def)
print('\n#########################################\n')



os.system('pause')
os.system('cls')