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
    
        print(item, isinstance(item, set)) # {0, 1} True
    
print('\n##############################\n')

for item in lista:
    
    if isinstance(item, set):
        
        item.add(5)    
        print(item, isinstance(item, set)) # {0, 1, 5} True
    
print('\n##############################\n')

for item in lista:
    
    if isinstance(item, str):
          
        print(item.upper(), isinstance(item, str)) # A True
    
print('\n##############################\n')

for item in lista:
    
    if isinstance(item, (int, float)): # Quando passa dentro da tupla mais de um tipo, vai significar ou int ou float, como no exemplo
          
        print(item, item * 2, isinstance(item, (int, float)))
        
'''
1 2 True
1.1 2.2 True
True 2 True    
    
'''
    
print('\n##############################\n')

os.system('pause')
os.system('cls')