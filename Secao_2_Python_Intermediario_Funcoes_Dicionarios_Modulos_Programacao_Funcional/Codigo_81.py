'''
Manipulando chaves e valores em dicionários.

'''

import os

os.system('color 1f')

pessoa = {
    
    'nome': 'João Augusto',
    'sobrenome': 'Colasso Handocha',
    'idade': 27,
    'altura': 1.80,
    'endereços': [
        
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 345},
        
    ],
        
}

print(f'\nNome e Sobrenome: {pessoa['nome']} {pessoa['sobrenome']}')
print(f'Idade: {pessoa['idade']}')
print(f'Altura: {pessoa['altura']}')
print(f'Endereços: {pessoa['endereços']}\n')

os.system('pause')
os.system('cls')

##############################

dados_pessoa = {}

dados_pessoa['nome'] = input('\nQual seu nome: ')
os.system('cls')
dados_pessoa['idade'] = int(input('\nQuantos anos você tem (Insira somente números): '))
os.system('cls')
dados_pessoa['altura'] = float(input('\nQual sua altura: '))
os.system('cls')
dados_pessoa['peso'] = float(input('\nQual seu peso: '))
os.system('cls')

print(f'\nInformações salvas no banco de dados: {dados_pessoa}\n')

os.system('pause')
os.system('cls')

print(f"\n{dados_pessoa['nome']}, tem {dados_pessoa['idade']} anos, {dados_pessoa['altura']:.2f} metros de altura, pesando {dados_pessoa['peso']:.3f}Kg.\n")

os.system('pause')
os.system('cls')

##############################

dados = {}

dados['nome'] = 'João'
dados['sobrenome'] = 'Augusto'

print(f'\n{dados}\n')

del dados['sobrenome']

print(f'{dados}\n')

if dados.get('sobrenome') is None:
    
    print('Não existe\n')
    
else:
    
    print(f'{dados['sobrenome']}\n')

os.system('pause')
os.system('cls')