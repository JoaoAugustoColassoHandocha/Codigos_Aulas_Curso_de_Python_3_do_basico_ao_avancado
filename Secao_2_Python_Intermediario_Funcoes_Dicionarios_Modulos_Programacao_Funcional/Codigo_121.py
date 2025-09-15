'''
variáveis Livres + nonlocal

'''

import os

os.system('color 1f')

print('\n******************************\n')

def fora():
    
    a = 1 # Váriavel livre - Ela não está definida dentro da função "dentro".
    
    def dentro():
        
        return a
    
    return dentro

print('\n******************************\n')



print('\n******************************\n')

os.system('pause')
os.system('cls')