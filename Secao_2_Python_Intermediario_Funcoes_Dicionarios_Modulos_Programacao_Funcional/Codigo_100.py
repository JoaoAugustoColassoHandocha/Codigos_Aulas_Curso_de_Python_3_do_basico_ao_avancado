'''
Isinstance - Para saber se objeto é de determinado tipo

'''

import os

os.system('color 1f')

lista = [
    
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'João'}
    
]

print('\n##############################\n')

for item in lista:
    
    if isinstance(item, set):
    
        print(item, isinstance(item, set)) # 
    
print('\n##############################\n')

os.system('pause')
os.system('cls')