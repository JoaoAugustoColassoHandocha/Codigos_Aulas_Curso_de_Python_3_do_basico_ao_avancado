'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)

'''

import os

os.system('color 1f')

nome = 'João'
preco = 1000.95897643
variavel = '%s, o preço é R$ %.2f' % (nome, preco)

print('\n' + variavel + '\n')
print(10 * '=' + '\n')
print('O hexadecimal de %d é %06X' % (255, 255) + '\n')

os.system('pause')
os.system('cls')
