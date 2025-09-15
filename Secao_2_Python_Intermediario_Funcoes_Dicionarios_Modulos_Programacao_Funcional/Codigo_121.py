'''
variáveis Livres + nonlocal

'''

import os

os.system('color 1f')

print('\n******************************\n')

def fora(x):
    
    a = x # Váriavel livre - Ela não está definida dentro da função "dentro".
    
    def dentro():
        
        return a
    
    return dentro

print(fora(10))
print(fora(20))

print('\n******************************\n')

os.system('pause')
os.system('cls')