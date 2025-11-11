'''
Exemplo JSON

'''

import os, json

os.system('color 1f')

pessoas = [
    
    {
        
        'nome': 'Joao',
    'sobrenome': 'Augusto',
    'enderecos': [
        
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
        
    ],
    'altura': 1.80,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
        
    }
    
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'aquivo_JSON.json')

with open(SAVE_TO, 'w+', encoding = 'utf-8') as file:
    
    json.dump(pessoas, file, indent = 2)

print(json.dumps(pessoas, indent = 2))

print('\nCriado JSON\n')

os.system('pause')
os.system('cls')