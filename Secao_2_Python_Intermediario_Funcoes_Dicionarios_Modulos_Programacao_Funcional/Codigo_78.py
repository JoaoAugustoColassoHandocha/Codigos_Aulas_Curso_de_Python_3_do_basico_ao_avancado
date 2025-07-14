'''
EXERCÍCIOS

Crie funções que duplicam, triplicam e quadrupicam o número recebido como parâmetro.

'''

import os

os.system('color 1f')

def multiplica_numero(multiplicador):
    
    def numero_repassado(numero):
        
        return multiplicador * numero
    
    return numero_repassado

numero = int(input('\nNúmero: '))

os.system('cls')

duplicar = multiplica_numero(2)
triplicar = multiplica_numero(3)
quadruplicar = multiplica_numero(4)

print(f'\nO dobro de {numero} é {duplicar(numero)}')
print(f'O triplo de {numero} é {triplicar(numero)}')
print(f'O quadruplo de {numero} é {quadruplicar(numero)}\n')

os.system('pause')
os.system('cls')