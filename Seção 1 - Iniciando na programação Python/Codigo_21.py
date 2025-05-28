'''
Operadores in e not in

* Strings são iteráveis (Pode navegar em cada item. Ex: letra por letra)
* 0 1 2 3 4 5
* P y t h o n
* -6-5-4-3-2-1

'''

# Exemplo de iteráveis

import os

os.system('color 1f')

nome = 'Python'

print('\n')

print(nome[0]) # P
print(nome[1]) # y
print(nome[2]) # t
print(nome[3]) # h
print(nome[4]) # o
print(nome[5]) # n

print('\n')

print(nome[-6]) # P
print(nome[-5]) # y
print(nome[-4]) # t
print(nome[-3]) # h
print(nome[-2]) # o
print(nome[-1]) # n

print('\n')

os.system('pause')
os.system('cls')

# Exemplo de in e not in

palavra = input('Digite a palavra que formou: ')

os.system('cls')

if palavra in nome:
    
    print(f'\n"{palavra}" é a palavra formada\n')
    os.system('pause')
    os.system('cls')
    
elif palavra not in nome:
    
    print(f'\n"{palavra}" não é a palavra formada\n')
    os.system('pause')
    os.system('cls')
    
else:
    
    print('\nInformação inválida!\n')
    os.system('pause')
    os.system('cls')