'''
Exercícios

* Aula 92, 82, 80, 93, 96

* Aumente os preços dos produtos a seguir em 10%.
* Gere novos_produtos por deep copy (cópia profunda).

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

* Ordene os produtos por nome decrescente (do maior para menor).
* Gere produtos_ordenados_por_nome por deep copy (cópia profunda).

* Ordene os produtos por preco crescente (do menor para maior).
* Gere produtos_ordenados_por_preco por deep copy (cópia profunda).

'''

import os, copy

os.system('color 1f')

produtos = [
    
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
    
]

print('\n******************************\n')

try:
    
    novos_produtos = copy.deepcopy([{**produto, 'preco': produto['preco%.2f'] * 1.10} for produto in produtos])
    
    for item_novos_produtos in novos_produtos:
    
        print(f'{item_novos_produtos}\n')
        
    print('\n******************************\n')

    produtos_ordenados_por_nome = copy.deepcopy(novos_produtos.sort(key = lambda item: item['nome'], reverse = True))
    
    print(f'{produtos_ordenados_por_nome}\n')
    
    print('\n******************************\n')

    produtos_ordenados_por_preco = copy.deepcopy(novos_produtos.sort(key = lambda custo: custo['preco']))
    
    print(f'{produtos_ordenados_por_preco}\n')
    
except ZeroDivisionError  as error:
    
    print(f'{error.__class__.__name__}: {error}')
    
except NameError  as error:
    
    print(f'{error.__class__.__name__}: {error}')

except (TypeError, IndexError) as error:
    
    print(f'{error.__class__.__name__}: {error}')
    
except Exception  as error:
    
    print(f'{error.__class__.__name__}: {error}')

print('\n******************************\n')

os.system('pause')
os.system('cls')