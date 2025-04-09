'''
Operadores lógicos

* and(e) / or(ou) / not(não)
* and - Todas as condições precisam ser verdadeiras - Se qualquer valor for considerado falso, a expressão inteira será avalisada naquele valor.
* or - Qualquer condição verdadeira avalia toda a expressão como verdadeira - Se qualquer valor for considerado verdadeiro, a expressão inteira será avalisada naquele valor.
* São considerados falsy: 0, 0.0. '', False
* Também existe o tipo None que é usado para representar um não valor.
* not - Inverte o valor lógico da expressão - Se a expressão for verdadeira, o not a tornará falsa e vice-versa. - not False = True | not True = False

'''

# Exemplo

import os, getpass

# Mudança de cor do terminal.
os.system('color 1f')

# Menu do app.
def menu():
    
    print('\n==========================')
    print('EXEMPLO DE ACESSO A SISTEMA')
    print('==========================\n')

    print('[E] - Entrar\n')
    print('[S] - Sair\n')

    # Opção de escolha para entrar no sistema ou sair.
    op = input('Escolha uma opção: ')

    os.system('cls')
    
    # Caso o usuário escolha entrar no sistema, chama a função acesso().
    if op == 'E' or op == 'e':
        
        acesso()

    # Caso o usuário queira sair do sistema, o programa é encerrado.
    elif op == 'S' or op == 's':
        
        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')
    
    # Caso o usuário não digite nada, o mesmo será notificado pelo sistema e o menu é chamado novamente.    
    elif not op:
    
        print('\nOpção não digitada!\n')
        print('Favor preencher campo solicitado!\n')        
        os.system('pause')
        os.system('cls')
        menu()
        
    # Caso o usuário digite uma opção inválida, o mesmo será notificado pelo sistema e o menu é chamado novamente.
    else:
        
        print('\nOpção inválida!\n')
        print('Favor verificar dados repassados!\n')
        os.system('pause')
        os.system('cls')
        menu()

# Função de acesso ao sistema.
def acesso():
    
    print('\n======')
    print('ACESSO')
    print('======\n')
    
    print('[A] - Acessar o sistema\n')
    print('[R] - Retornar ao Menu\n')
    
    # Opção de escolha para acesso no sistema ou retornar ao menu.
    opcao = input('Escolha uma opção: ')
    
    os.system('cls')
    
    # Caso o usuario escolha acessar o sistema, solicita usuário e senha.
    if opcao == 'A' or opcao == 'a':
                  
        # Aplicativo solicita usuário e senha para acesso.
        usuario = input('Usuário: ')
        senha = getpass.getpass('Senha: ')
        
        val_acesso =  usuario == 'Admin' and senha == 'Admin@123'
        
        os.system('cls')
        
        # Caso o usuário e senha estejam corretos, o acesso é permitido.
        if val_acesso == True:
            
            print('\nAcesso Permitido!\n')
            os.system('pause')
            os.system('cls')
            acesso()
            
        # Caso o usuário e senha estejam incorretos ou não digitados, o acesso é negado.
        elif val_acesso != True:
            
            print('\nAcesso Negado!\n')
            print('Usuário ou Senha incorreto ou não digitado!\n')
            os.system('pause')
            os.system('cls')
            acesso()
        
        # Caso o usuário digite uma opção inválida, o mesmo será notificado pelo sistema.
        else:
                
            print('\nAcesso Negado!\n')
            print('Favor verificar dados repassados!\n')
            os.system('pause')
            os.system('cls')
            acesso()
    
    # Caso o usuário escolha retornar ao menu, o mesmo é chamado novamente.
    elif opcao == 'R' or opcao == 'r':
        
        menu()
        
    # Caso o usuário não digite nada, o mesmo será notificado pelo sistema.   
    elif not opcao:
    
        print('\nOpção não digitada!\n')
        print('Favor preencher campo solicitado!\n')        
        os.system('pause')
        os.system('cls')
        acesso()
    
    # Caso o usuário digite uma opção inválida, o mesmo será notificado pelo sistema.
    else:
        
        print('\nOpção inválida!\n')
        os.system('pause')
        os.system('cls')
        acesso()

# Chamada da função menu() para iniciar o sistema.       
menu()