'''
Introdução ás funções (def) em Python

Funções são trechos de código usados para replicar determinada ação ao longo do seu código.

Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.

Por padrão, funções Python retornam None (nada).

'''

import os, gc

os.system('color 1f')

def imprimir (a, b, c):
    
    print(a, b, c)

print('\n')    
imprimir(1, 2, 3)
imprimir(4, 5, 6)
print('\n')
os.system('pause')
os.system('cls')
gc.collect()

def saudacao(nome = 'Sem nome'):
    
    print(f'Olá, {nome}')
    
print('\n')
saudacao('João Augusto')
saudacao()
print('\n')
os.system('pause')
os.system('cls')
gc.collect()