'''
EXERCÍCIOS

Crie funções que duplicam, triplicam e quadrupicam o número recebido como parâmetro.

'''

import os

os.system('color 1f')

def duplicar(numero):
    
    return numero * 2

def triplicar(numero):
    
    return numero * 3

def quadruplicar(numero):
    
    return numero * 4

print('\n')
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
print('\n')

os.system('pause')
os.system('cls')

############################

def criar_multiplicador(multiplicador):
    
    def multiplicar(numero):
        
        return numero * multiplicador
    
    return multiplicar

duplicar_2 = criar_multiplicador(2)
triplicar_3 = criar_multiplicador(3)
quadruplicar_4 = criar_multiplicador(4)

print('\n')
print(duplicar_2(2))
print(triplicar_3(2))
print(quadruplicar_4(2))
print('\n')