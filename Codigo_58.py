'''
Lista de listas e seus índices

'''

import os

os.system('color 1f')

salas = [
    #   0        1
    ['Maria', 'Helena', ], # 0
    
    #   0
    ['Elaine', ], # 1
    
    #  0       1         2                3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # 2
    
]

print(f'\n{salas}\n')

print(f'{salas[2][1]}\n')

print(f'{salas[2][3][3]}\n')

os.system('pause')
os.system('cls')