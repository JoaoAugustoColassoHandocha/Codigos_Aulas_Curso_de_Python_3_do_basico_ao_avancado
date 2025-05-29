'''
Argumentos nomeados e não nomeados em funções Pyhton
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

'''

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