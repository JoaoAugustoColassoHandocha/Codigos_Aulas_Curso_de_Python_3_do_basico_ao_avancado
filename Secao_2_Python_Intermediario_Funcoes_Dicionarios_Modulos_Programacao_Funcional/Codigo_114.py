'''


'''

import os, sys

import Codigo_114_Package.Codigo_114_Modulo

from Codigo_114_Package.Codigo_114_Modulo import soma

os.system('color 1f')

print('\n******************************\n')

print(__name__)

print('\n******************************\n')

print(*sys.path, sep = '\n')

print('\n******************************\n')

print(f'O resultado de 1 + 2 é {Codigo_114_Package.Codigo_114_Modulo.soma(1, 2)}')

print('\n******************************\n')

print(f'O resultado de 1 + 2 é {soma(1, 2)}')

print('\n******************************\n')

os.system('pause')
os.system('cls')