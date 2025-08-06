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
    
    print(item, isinstance(item, set))
    
'''
a False
1 False
1.1 False
True False
[0, 1, 2] False
(1, 2) False
{0, 1} True
{'nome': 'João'} False 

'''
    
print('\n##############################\n')

os.system('pause')
os.system('cls')