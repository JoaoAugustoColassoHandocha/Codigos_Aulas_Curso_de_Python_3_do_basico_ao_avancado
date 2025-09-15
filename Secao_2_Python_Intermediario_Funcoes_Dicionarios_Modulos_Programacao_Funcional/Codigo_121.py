'''
variáveis Livres + nonlocal (locals e globals)

locals: Me fala quais funções são locais.

globals: Todas as variáveis globais que estão definidas.

"nomedafuncao".__code__.co_freevars: Acesso as variáveis livres dentro da função.

'''

import os

os.system('color 1f')

print('\n******************************\n')

def fora(x):
    
    a = x # Váriavel livre - Ela não está definida dentro da função "dentro".
    
    def dentro():
        
        print(f'{locals()} || {dentro.__code__.co_freevars}')
        
        return a
    
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

print('\n******************************\n')

print(globals())

print('\n******************************\n')



print('\n******************************\n')

os.system('pause')
os.system('cls')