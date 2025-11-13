'''
JSON

'''

import os, json

os.system('color 1f')

pessoa = {
    
    'nome': 'João',
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

print('\n******************************\n')

with open('Codigo_147.json', 'w+', encoding = 'utf-8') as arquivo:
    
    json.dump(pessoa, arquivo, ensure_ascii = False, indent= 2)

print('\n******************************\n')

os.system('pause')
os.system('cls')