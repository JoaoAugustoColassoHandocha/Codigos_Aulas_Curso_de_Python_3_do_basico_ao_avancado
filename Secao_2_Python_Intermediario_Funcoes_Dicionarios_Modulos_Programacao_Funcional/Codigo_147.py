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

with open('Codigo_147_1.json', 'w+', encoding = 'utf-8') as arquivo_w:
    
    json.dump(pessoa, arquivo_w, ensure_ascii = False, indent= 2)
    
    print(json.dumps(pessoa, indent = 2))
    
print('\n******************************\n')
    
with open('Codigo_147_1.json', 'r+', encoding = 'utf-8') as arquivo_r:
    
    pessoa_2 = json.load(arquivo_r)
    
    print(pessoa_2)

print('\n******************************\n')

os.system('pause')
os.system('cls')