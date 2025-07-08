'''


'''

import os

os.system('color 1f')

def soma(*args):
    
    total = 0
    
    for numero in args:
        
        total += numero
        
    return total

print('\n')
soma(1, 2, 3, 4, 5)
print('\n')

os.system('pause')
os.system('cls')