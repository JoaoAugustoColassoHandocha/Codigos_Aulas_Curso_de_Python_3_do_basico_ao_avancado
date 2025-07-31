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
    
    
* Utilizar o lambda para funções menos complexas.

* Caso a lambda comece a ficar muito complexa, melhor criar um def, visando que outros devs possam entender.

'''

import os

os.system('color 1f')

def executa(funcao, *args):
    
    return funcao(*args)

# Função def soma convertida para lambda

# Lambda seria a mesma coisa que def

print('\n#########################################\n')

print(executa(lambda x, y: x + y, 2, 3)) # executa seria o nome da função (como se fosse a criação de uma def)

print('\n#########################################\n')

print(executa(lambda multiplicador: lambda numero: numero * multiplicador, 2))

print('\n#########################################\n')

print(executa(lambda *args: sum(args), 1, 2, 3))

print('\n#########################################\n')

os.system('pause')
os.system('cls')