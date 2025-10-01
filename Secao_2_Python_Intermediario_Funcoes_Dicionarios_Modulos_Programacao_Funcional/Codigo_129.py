'''
RESOLUÇÃO

Considerando duas listas de inteiros ou floats (lista A e lista B), some os valores nas listas, retornando uma nova lista com os valores somados.

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

Resultado:

lista_soma = [2, 4, 6, 8]

'''

import os

os.system('color 1f')

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print('\n******************************\n')

lista_soma = []

for i in range(len(lista_b)):
    
    lista_soma.append(lista_a[i] + lista_b[i])

print('\n******************************\n')

os.system('pause')
os.system('cls')