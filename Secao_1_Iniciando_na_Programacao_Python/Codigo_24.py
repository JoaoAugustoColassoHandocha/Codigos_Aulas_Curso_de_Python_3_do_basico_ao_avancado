'''
Fatiamento de strings

* Olá Mundo
* 012345678
*-987654321
* Fatiamento [i:f:p] [::] - i: indice inicial, f: indice final, p: passo
* No final do fatiamento, sempre indicar um número de indice a mais.
* Obs: a função len() retorna a quantidade de caracteres da string.

'''

# Exemplo de iteráveis

import os

os.system('color 1f')

variavel = 'Olá Mundo'

print('\n' + '=' * 10 + '\n')

print(variavel[0])
print(variavel[1])
print(variavel[2])
print(variavel[3])
print(variavel[4])
print(variavel[5])
print(variavel[6])
print(variavel[7])
print(variavel[8])

print('\n' + '=' * 10 + '\n')

print(variavel[-9])
print(variavel[-8])
print(variavel[-7])
print(variavel[-6])
print(variavel[-5])
print(variavel[-4])
print(variavel[-3])
print(variavel[-2])
print(variavel[-1])

print('\n' + '=' * 10 + '\n')

os.system('pause')
os.system('cls')

# Exemplo de fatiamento de strings

print('\n' + '=' * 10 + '\n')

print(variavel[0:3] + '\n')  # Olá
print(variavel[4:9] + '\n')  # Mundo
print(variavel[0:len(variavel):2] + '\n') # Ol Mnd
print(variavel[::-1] + '\n') # odnuM alO
print(variavel[-1:-10:-1]) # odnuM alO

print('\n' + '=' * 10 + '\n')

os.system('pause')
os.system('cls')

# Exemplo len()

print('\n' + '=' * 10 + '\n')

print(len(variavel))  # 9
print(f'\nO tamanho da string "{variavel}" é: {len(variavel)}')

print('\n' + '=' * 10 + '\n')

os.system('pause')
os.system('cls')