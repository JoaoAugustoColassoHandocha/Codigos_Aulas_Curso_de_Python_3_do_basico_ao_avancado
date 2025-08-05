'''
List comprehension com mais de um for

* O lado esquerdo do for é utilizado para o mapeamento

'''

import os

os.system('color 1f')

print('\n##############################\n')

# FOR sem o list comprehension

lista = []

for x in range(3):
    
    for y in range(3):
        
        lista.append((x, y))
        
print(lista) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


print('\n##############################\n')

# FOR com list comprehension

lista = [(x, y) for x in range(3) for y in range(3)]

print(lista) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

print('\n##############################\n')

os.system('pause')
os.system('cls')