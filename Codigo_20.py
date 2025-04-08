'''
Operadores lógicos

* and(e) / or(ou) / not(não)
* and - Todas as condições precisam ser verdadeiras.
* Se qualquer valor for considerado falso, a expressão inteira será avalisada naquele valor.
* São considerados falsy: 0, 0.0. '', False
* Também existe o tipo None que é usado para representar um não valor.

'''

# Exmplo and

import os, getpass

os.system('color 1f')

def menu():
    
    print('\n===========')
    print('EXEMPLO AND')
    print('===========\n')

    print('[E] - Entrar\n')
    print('[S] - Sair\n')

    op = input('Escolha uma opção: ')

    os.system('cls')
    
    if op == 'E' or op == 'e':
        
        acesso()
        
    elif op == 'S' or op == 's':
        
        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')
    
    else:
        
        print('Opção inválida!')
        os.system('pause')
        os.system('cls')
        menu()
    
def acesso():
    
    print('\n======')
    print('ACESSO')
    print('======\n')
    
    usuario = input('Usuário: ')
    senha = getpass.getpass('Senha: ')
    
    os.system('cls')
    
    if usuario == 'Admin' and senha == 'Admin@123':
        
        print('\nAcesso Permitido!\n')
        os.system('pause')
        os.system('cls')
        menu()
    
    elif usuario or senha == False:
        
        print('\nAcesso Negado!\n')
        print('Usuário ou Senha incorreto!\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    else:
            
        print('\nAcesso Negado!\n')
        print('Favor verificar dados repassados!\n')
        os.system('pause')
        os.system('cls')
        menu()
        
menu()