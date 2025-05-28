'''
Enumerate - Enumera iteráveis (índices)

enumerate()

\t - TAB

'''

import os

os.system('color 1f')

lista = ['Maria', 'Helena', 'Luiz']

lista.append('João')

print('\n')

for indice, nome in enumerate(lista):

    print(indice, nome)
    
print('\n')
    
# Outra forma de fazer

lista_enumerada = list(enumerate(lista))

print(f'{lista_enumerada}\n')

os.system('pause')
os.system('cls')