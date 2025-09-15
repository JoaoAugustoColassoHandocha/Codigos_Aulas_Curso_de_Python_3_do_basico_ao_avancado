'''
variáveis Livres + nonlocal (locals e globals)

locals - Me fala quais funções são locais.

globals - 

'''

import os

os.system('color 1f')

print('\n******************************\n')

def fora(x):
    
    a = x # Váriavel livre - Ela não está definida dentro da função "dentro".
    
    def dentro():
        
        return a
    
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

print('\n******************************\n')

os.system('pause')
os.system('cls')