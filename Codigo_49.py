'''

Cuidados com dados mutáveis

= - Copiado o valor (imutáveis)
= - Aponta para o mesmo valor na memória (mutável)

lista.copy() - Copia a lista para outra lista

'''
import os

os.system('color 1f')

lista_a = ['Joao', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Maria'

print(f'\n{lista_a}')
print(f'\n{lista_b}\n')

os.system('pause')
os.system('cls')