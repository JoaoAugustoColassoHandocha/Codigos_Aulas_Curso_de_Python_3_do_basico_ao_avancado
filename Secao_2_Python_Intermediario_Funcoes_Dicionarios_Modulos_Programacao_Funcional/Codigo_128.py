'''
EXERCICIO

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

print('\n******************************\n')

def func_soma(lista1, lista2):
    
    intervalo_maximo = min(len(lista1),len(lista2))
    return [(lista1[i] + lista2[i]) for i in range(intervalo_maximo)]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

for lista_soma in func_soma(lista_a, lista_b):
    
    print(f'{lista_soma}')

print('\n******************************\n')

soma_das_listas = [a + b for a, b in zip(lista_a, lista_b)]

for res_soma_das_listas in soma_das_listas:
    
    print(soma_das_listas)

print('\n******************************\n')

os.system('pause')
os.system('cls')