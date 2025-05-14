'''
Faça uma lista de compras com listas

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista

Não permita que o programa quebre com erros de índices inexistentes na lista.

'''

import os

os.system('color 1f')

def main():

    print('\n' + '-' * 5 + 'LISTA DE COMPRA' + '-' * 5 + '\n')
    print('[1] - Cadastrar produto')
    print('[2] - Mostrar lista')
    print('[3] - Apagar produto')
    print('[4] - Sair')
    print('\n' + '-' * 25 + '\n')
        
    op = input('Escolha uma opção: ')
        
    os.system('cls')
    
    if op == 1:
        
        cadastrar()
        
    elif op == 2:
        
        mostrar()
        
    elif op == 3:
        
        apagar()
        
    elif op == 4:
        
        print('Saindo...')
        os.system('pause')
        os.system('cls')
        os.system('exit')

os.system('pause')
os.system('cls')