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
        
    print(json.dumps(pessoas))
    
    print('\n')
    
    json_string = '[{"nome": "Joao", "sobrenome": "Augusto", "enderecos": [{"rua": "R1", "numero": 32}, {"rua": "R2", "numero": 55}], "altura": 1.8, "numeros_preferidos": [2, 4, 6, 8, 10], "dev": true, "nada": null}]'
    
    dados = json.loads(json_string)
    
    for dado in dados:
        
        print(f'Nome: {dado['nome']}')
        print(f'Sobrenome: {dado['sobrenome']}')
        
        x = 1
        
        for end in dado['enderecos']:
            
            print(f'Endereço {i}: {end}')
            
            x += 1
        
        print(f'Altura: {dado['altura']}')
        print(f'Números Preferidos: {dado['numeros_preferidos']}')
        print(f'DEV: {dado['dev']}')

print('\n')

os.system('pause')
os.system('cls')