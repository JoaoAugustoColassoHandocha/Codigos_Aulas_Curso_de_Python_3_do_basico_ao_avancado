'''
Argumentos nomeados e não nomeados em funções Pyhton
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

Parâmetro - É a váriavel do código, que armazena as informações repassadas.

Argumento - É a informação repassada para a váriavel.

Argumentos nomeados recebem o nome do parâmetro antes do valor, argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem.

Obs: Não se pode enviar argumentos posicionais após argumentos nomeados.

'''

###############################

import os, gc

os.system('color 1f')

def soma(x, y):
    
    print(f'{x = } e {y = } | x + y = ', x + y)
    
print('\n')
soma(1, 2)
soma(y = 2, x = 1)
print('\n')

os.system('pause')
os.system('cls')
gc.collect()

###############################

def subtracao(x, y, z):
    
    print(f'{x = }, {y = } e {z = } | x - y - z = ', x - y - z)
    
print('\n')
subtracao(1, 2 , 3)
subtracao(y = 2, z = 3, x = 1)
print('\n')

os.system('pause')
os.system('cls')
gc.collect()

###############################