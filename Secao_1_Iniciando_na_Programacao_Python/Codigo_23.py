'''
Formatação básica de strings

* s - string
* d - int
* f - float
* .<número de dígitos>f - float com n dígitos após a vírgula
* x ou X - hexadecimal
* (Caractere)(><^)(quantidade)
* > - Esquerda
* < - Direita
* ^ - Centro
* Sinal: - ou +
* Ex: 0 >- 100,.1f
* Conversion flags: !r, !s, !a

'''

import os

os.system('color 1f')

variavel = 'Python'

print('\n' + 10 * '=')
print(f'\n{variavel}.\n')
print(10 * '=')
print(f'\n{variavel: >10}.\n')
print(10 * '=')
print(f'\n{variavel: <10}.\n')
print(10 * '=')
print(f'\n{variavel: ^10}.\n')
print(10 * '=')
print(f'\nR${1000.4873648: .2f}\n')
print(10 * '=' + '\n')
print(f'O hexadecimal de 255 é {255:06X}')
print(10 * '=' + '\n')

os.system('pause')
os.system('cls')