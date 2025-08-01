'''
Mapeamento de dados em list comprehension

'''

import os

os.system('color 1f')

produtos = [
    
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
    
]

print('\n##############################\n')

novos_produtos = [produto for produto in produtos]
print(novos_produtos) # [{'nome': 'p1', 'preco': 20}, {'nome': 'p2', 'preco': 10}, {'nome': 'p3', 'preco': 30}]

print('\n##############################\n')

print(*novos_produtos, sep = ' | ') # {'nome': 'p1', 'preco': 20} | {'nome': 'p2', 'preco': 10} | {'nome': 'p3', 'preco': 30}

print('\n##############################\n')

os.system('pause')
os.system('cls')