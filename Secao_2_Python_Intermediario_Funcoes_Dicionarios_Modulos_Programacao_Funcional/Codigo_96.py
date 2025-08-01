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

novos_produtos_2 = [produto['nome'] for produto in produtos]
print(novos_produtos_2) # ['p1', 'p2', 'p3']

print('\n##############################\n')

novos_produtos_3 = [{**produto, 'preco': produto['preco'] * 1.05} for produto in produtos]
print(novos_produtos_3) # [{'nome': 'p1', 'preco': 21.0}, {'nome': 'p2', 'preco': 10.5}, {'nome': 'p3', 'preco': 31.5}]

print('\n##############################\n')

novos_produtos_3 = [

    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos

]

print(novos_produtos_3) # 

print('\n##############################\n')

os.system('pause')
os.system('cls')