'''
Exemplo JSON - Carregando o JSON

'''

import os, json

os.system('color 1f')

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'aquivo_JSON.json')

print('\n')

with open(JSON_FILE, 'r+') as file:
    
    pessoas = json.load(file)
    
    for pessoa in pessoas:
        
        print(f'Nome: {pessoa['nome']}')
        print(f'Sobrenome: {pessoa['sobrenome']}')
        
        i = 1
        
        for endereco in pessoa['enderecos']:
            
            print(f'Endereço {i}: {endereco}')
            
            i += 1
        
        print(f'Altura: {pessoa['altura']}')
        print(f'Números Preferidos: {pessoa['numeros_preferidos']}')
        print(f'DEV: {pessoa['dev']}')

print('\n')

os.system('pause')
os.system('cls')