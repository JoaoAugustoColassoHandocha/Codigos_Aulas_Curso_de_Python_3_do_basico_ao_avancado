'''
Introdução ao desempacotamento + tuples (tuplas)

( _ ) - É uma variável que não será utilizada

'''

import os

os.system('color 1f')

nomes = ['Maria', 'Helena', 'Joao']

nome1, nome2, nome3 = nomes

print('\n' + '*' * 30)
print(f'\n{nome1} - {nome2} - {nome3}')

nome1, *resto = nomes

print('\n' + '*' * 30)
print(f'\n{nome1} - {resto}')

nome1, *_ = nomes

print('\n' + '*' * 30)
print(f'\n{nome1} - {_}')

_, nome2, *_ = nomes

print('\n' + '*' * 30)
print(f'\n{_} - {nome2} - {_}')

_, _, nome3, *_ = nomes

print('\n' + '*' * 30)
print(f'\n{_} - {_} - {nome3}')

print('\n' + '*' * 30 + '\n')

os.system('pause')
os.system('cls')