'''
Valores Truthy e Falsy

Tipos mutáveis e imutáveis:

* Mutáveis = [] {} set()
* Imutáveis = () '' 0 0.0 None False range(0, 10)

'''

import os

os.system('color 1f')

# Falso
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    
    return 'falsy' if not valor else 'truthy'

print('\n##############################\n')
print(f'TESTE - {falsy('TESTE')}')
print('\n##############################\n')
print(f'{lista = } - {falsy(lista)}')
print('\n##############################\n')
print(f'{dicionario = } - {falsy(dicionario)}')
print('\n##############################\n')
print(f'{conjunto = } - {falsy(conjunto)}')
print('\n##############################\n')
print(f'{tupla = } - {falsy(tupla)}')
print('\n##############################\n')
print(f'{string = } - {falsy(string)}')
print('\n##############################\n')
print(f'{inteito = } - {falsy(inteito)}')
print('\n##############################\n')
print(f'{flutuante = } - {falsy(flutuante)}')
print('\n##############################\n')
print(f'{nada = } - {falsy(nada)}')
print('\n##############################\n')
print(f'{falso = } - {falsy(falso)}')
print('\n##############################\n')
print(f'{intervalo = } - {falsy(intervalo)}')
print('\n##############################\n')

os.system('pause')
os.system('cls')