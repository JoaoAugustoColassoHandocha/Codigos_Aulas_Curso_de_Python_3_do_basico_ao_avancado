'''
https://docs.python.org/pt-br/3/libary/stdtypes.html

Imutáveis que vimos: str, int, float, bool

'''

import os

os.system('color 1f')

string = 'joão augusto'

string_2 = string

string_3 = f'{string[:3]}0{string[4:]}'

print(f'\n{string}')

print(f'\n{string_2}')

print(f'\n{string_3}\n')

os.system('pause')
os.system('cls')

print(f'\n{string.capitalize()}\n')

os.system('pause')
os.system('cls')