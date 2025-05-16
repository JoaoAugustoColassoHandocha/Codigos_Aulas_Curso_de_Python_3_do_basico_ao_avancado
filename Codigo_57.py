'''
split e join com list e str

split - divide uma string

join - une uma string

strip() - Corta os espaços do início e final da informação imprimida

'''

import os

os.system('color 1f')

frase = 'Olha só que, coisa interessante'

#######################

lista_palavras_1 = frase.split()

print(f'\n{lista_palavras_1}\n')

#######################

lista_palavras_2 = frase.split(',')

print(f'{lista_palavras_2}\n')

#######################

lista_palavras_3 = frase.split(', ')

for i, frase in enumerate(lista_palavras_3):
    
    print(lista_palavras_3[i])
    
print('\n')

#######################
    
os.system('pause')
os.system('cls')