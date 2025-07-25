'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é onde todo o código é alcançavel.
O escopo local é onde apenas nomes do mesmo local podem ser alcançados.

Não temos acesso a nomes de escopos internos nos escopos externos.

A palavra global faz uma váriavel do escopo externo ser a mesma no escopo interno.

'''

import os

os.system('color 1f')

def escopo():
    
    x = 1
    
    print(x)

print('\n')
escopo()
print('\n')

os.system('pause')
os.system('cls')

##################

x = 1

def escopo_2():
    
    x = 10
    
    def outra_funcao():
        
        x = 11
        y = 2
        
        print(x, y)
        
    outra_funcao()
    
    print(x)

print('\n')    
print(x)
escopo_2()
print(x)
print('\n')

os.system('pause')
os.system('cls')