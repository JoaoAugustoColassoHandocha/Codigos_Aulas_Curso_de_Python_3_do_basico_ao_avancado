'''
Exercícios

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
    
    novos_produtos = copy.deepcopy([{**produto, 'preco': produto['preco'] * 1.10} for produto in produtos])
    
    for item_novos_produtos in novos_produtos:
    
        print(f'Produto: {item_novos_produtos['nome']} | Preço: R${item_novos_produtos['preco']:.2f}')
        
    print('\n******************************\n')
    
    def ordena_nome_descrescente(item_nome):
    
        return item_nome['nome']

    produtos_ordenados_por_nome = novos_produtos
    
    produtos_ordenados_por_nome.sort(key = ordena_nome_descrescente, reverse = True)
    
    for item_produtos_ordenados_por_nome in copy.deepcopy(produtos_ordenados_por_nome):
        
        print(f'Produto: {item_produtos_ordenados_por_nome['nome']} | Preço: R${item_produtos_ordenados_por_nome['preco']:.2f}')
    
    print('\n******************************\n')
    
    def ordena_preco_crescente(item_preco):
        
        return item_preco['preco']

    produtos_ordenados_por_preco = novos_produtos
    
    produtos_ordenados_por_preco.sort(key = ordena_preco_crescente)
    
    for item_produtos_ordenados_por_preco in copy.deepcopy(produtos_ordenados_por_preco):
    
        print(f'Produto: {item_produtos_ordenados_por_preco['nome']} | Preço: R${item_produtos_ordenados_por_preco['preco']:.2f}')
    
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