'''
Desempacotamento em chamadas de métodos e funções

O parâmetro "end" do Python é usado para adicionar qualquer string ao final da saída de print().

Por outro lado, para separar a saída por caractere ou string no lugar do valor de espaço padrão, usamos o parâmetro "sep" do Python.

'''

import os

os.system('color 1f')

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, c = lista

print(f'\n{a, c}\n')

#########################

for nome in lista:
    
    print(nome, end = ' ')

print('\n')

#########################

print(*lista + '\n')

#########################

print(*string + '\n')

#########################

print(*tupla + '\n')

os.system('pause')
os.system('cls')