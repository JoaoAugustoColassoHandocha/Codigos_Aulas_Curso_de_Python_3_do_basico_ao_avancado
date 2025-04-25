'''
Operadores de atribuição
= += -= *= /= //= **= %=

'''

import os

os.system('color 1f')

contador = 0

while contador < 10:
    
    contador += 1 # Atribuindo o operador +=
    
    print(f'\n{contador}')
    
print('\nAcabou\n')

# Exemplo de concatenação com operador de atribuição +=

cont = 'a'

print(f'{cont}\n')

cont += 'bc'

print(f'{cont}\n')

# Exemplo de multiplicar str com operador de atribuição *=

mult = '='

mult *= 30

print(f'{mult}\n')

os.system('pause')
os.system('cls')