'''
Filtro de dados em list comprehension

Filtro serve caso não queria incluir determinada questão na lista, se a condição que foi passada for True

'''

import os

os.system('color 1f')

print('\n##############################\n')

lista = [numeros for numeros in range(10)] # Sem o filtro ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(lista)

print('\n##############################\n')

lista = [numeros for numeros in range(10) if numeros < 5] # Com o filtro ([0, 1, 2, 3, 4])
print(lista)

print('\n##############################\n')

# Exemplo com filtro

produtos = [
    
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
    
]

novos_produtos_4 = [

    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10

]

print(novos_produtos_4) # [{'nome': 'p1', 'preco': 20}, {'nome': 'p3', 'preco': 31.5}]

print('\n##############################\n')

os.system('pause')
os.system('cls')