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

with open('Codigo_147.json', 'w+', encoding = 'utf-8') as arquivo_w:
    
    json.dump(pessoa, arquivo_w, ensure_ascii = False, indent= 2)
    
    print(json.dumps(pessoa, indent = 2, ensure_ascii = False))
    
print('\n******************************\n')
    
with open('Codigo_147.json', 'r+', encoding = 'utf-8') as arquivo_r:
    
    pessoa_2 = json.load(arquivo_r)
    
    print(pessoa_2)
    
    print(f'\nNome: {pessoa_2['nome']}\n')
    print(f'Sobrenome: {pessoa_2['sobrenome']}\n')
    print('Endereços:\n')
    for ends in pessoa_2['enderecos']:
            
        print(f'Rua: {ends['rua']}')
        print(f'Número: {ends['numero']}\n')
            
    print(f'Altura: {pessoa_2['altura']}\n')
    print('Números Preferidos:\n')
    for num in pessoa_2['numeros_preferidos']:
        
        print(num)
        
    print('\n')        
    print(f'DEV: {pessoa_2['dev']}\n')
    print(f'Nada: {pessoa_2['nada']}')

print('\n******************************\n')

os.system('pause')
os.system('cls')