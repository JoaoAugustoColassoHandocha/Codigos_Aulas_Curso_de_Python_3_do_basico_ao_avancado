'''
Exemplo JSON - Carregando o JSON

'''

import os, json

os.system('color 1f')

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'aquivo_JSON.json')

with open(JSON_FILE, 'r+') as file:
    
    pessoas = json.load(file)
    
    for pessoa in pessoas:
        
        print(f'Nome: {pessoa['nome']}')
        print(f'Sobrenome: {pessoa['sobrenone']}')
        print(f'Endereços: {pessoa['enderecos']}')

os.system('pause')
os.system('cls')