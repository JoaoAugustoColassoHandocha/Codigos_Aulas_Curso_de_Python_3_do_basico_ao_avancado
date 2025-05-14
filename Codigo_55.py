'''
Faça uma lista de compras com listas

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista

Não permita que o programa quebre com erros de índices inexistentes na lista.

'''

import os, getpass

os.system('color 1f')

lista = []

def main():

    print('\n' + '-' * 5 + 'LISTA DE COMPRA' + '-' * 5 + '\n')
    print('[1] - Acessar o sistema')
    print('[4] - Sair')
    print('\n' + '-' * 25 + '\n')
        
    op = input('Escolha uma opção: ')
        
    os.system('cls')
    
    if op == 1:
        
        senha = getpass.getpass('Favor repassar a senha de acesso: ')
        
        os.system('cls')
        
        while True:
        
            if senha == 'AcessoLista':
                
                lista_compra()
                break
                
            elif senha != 'AcessoLista':
                
                print('\nSENHA ERRADA!!!')
                print('\nFavor inserir senha correta!')
                        
    elif op == 2:
        
        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')
        os.system('exit')
        
    else:
        
        print('\nERRO!!!')
        print('\nFavor entrar em contato com o suporte do sistema.')
        os.system('pause')
        os.system('cls')
        os.system('exit')
        
def lista_compra():
    
    print('\nteste\n')
    os.system('pause')
    os.system('cls')
    
main()

os.system('pause')
os.system('cls')