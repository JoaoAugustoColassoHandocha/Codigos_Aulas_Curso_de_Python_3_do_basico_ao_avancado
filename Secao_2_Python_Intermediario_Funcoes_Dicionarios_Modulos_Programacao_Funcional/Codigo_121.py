'''
variáveis Livres + nonlocal

'''

import os

os.system('color 1f')

print('\n******************************\n')

def fora():
    
    a = 1
    
    def dentro():
        
        return a
    
    return dentro

print('\n******************************\n')



print('\n******************************\n')

os.system('pause')
os.system('cls')