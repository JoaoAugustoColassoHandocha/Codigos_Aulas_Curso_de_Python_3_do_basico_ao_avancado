'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é onde todo o código é alcançavel.
O escopo local é onde apenas nomes do mesmo local podem ser alcançados.

'''

import os

os.system('color 1f')

def escopo():
    
    x = 1
    
    print(x)

escopo()

os.system('pause')
os.system('cls')