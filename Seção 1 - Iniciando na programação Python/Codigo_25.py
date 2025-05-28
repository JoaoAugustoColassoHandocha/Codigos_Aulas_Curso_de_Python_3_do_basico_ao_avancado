'''
Exercício

* Peça ao usuário para digitar seu nome e idade.
* Se nome e idade forem digitados:
    
    Exiba:
    
        Seu nome é <nome>
        Seu nome invertido é <nome invertido>
        Seu nome contém (ou não) espaços
        Seu nome tem <n> letras
        A primeira letra do seu nome é <letra>
        A última letra do seu nome é <letra>

    Se nada for digitado, exiba:
    
        'Desculpe, você deixou os campos vazios.'
            
'''

import os

os.system('color 1f')

def menu():
    
    print('\n' + '=' * 10 + '\n')
    print('EXERCÍCIO')
    print('\n' + '=' * 10 + '\n')
    print('Bem-vindo ao programa de análise de nome!\n')
    print('[E] - Entrar')
    print('[S] - Sair')
    print('\n' + '=' * 10 + '\n')
    
    opcao = input('Escolha uma opção: ')
    
    os.system('cls')
    
    if opcao == 'E' or opcao == 'e':
        
        info()
        
    elif opcao == 'S' or opcao == 's':
        
        print(' \nSaindo do programa...\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        print('\nOpção inválida. Tente novamente.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
def info():
    
    print('\n' + '=' * 10 + '\n')
    print('[I] - Informar dados')
    print('[R] - Retornar ao menu')
    print('\n' + '=' * 10 + '\n')
    
    op = input('Escolha uma opção: ')
    
    os.system('cls')
    
    if op == 'I' or op == 'i':
        
        nome = input('\nDigite seu nome: ')
        idade = input('\nDigite sua idade: ')
        
        os.system('cls')
        
        if bool(nome) and bool(idade) == True:
            
            print('\n' + '=' * 10 + '\n')
            print(f'Seu nome é {nome} e tem {idade} anos!\n')
            print(f'Seu nome invertido é {nome[::-1]}!\n')
            
            if ' ' in nome:
                
                print(f'Seu nome contém espaços!\n')
                
            elif ' ' not in nome:
                
                print(f'Seu nome não contém espaços!\n')
                
            else:
                
                print(f'Erro ao identificar se seu nome contém espaços ou não!\n')
                
            print(f'Seu nome tem {len(nome)} letras!\n')
            print(f'A primeira letra do seu nome é {nome[0]}!\n')
            print(f'A última letra do seu nome é {nome[-1]}!')
            print('\n' + '=' * 10 + '\n')
            os.system('pause')
            os.system('cls')
            info()
            
        elif nome == '' or idade == '':
            
            print('\nDesculpe, você deixou algum dos campos vazio.')
            print('\nFavor preencher os campos corretamente!\n')
            os.system('pause')
            os.system('cls')
            info()
        
        else:
            
            print('\nErro ao identificar os campos!\n')
            os.system('pause')
            os.system('cls')
            info()
            
    elif op == 'R' or op == 'r':
        
        print('\nRetornando ao menu...\n')
        os.system('pause')
        os.system('cls')
        menu()
    
    else:
        
        print('\nOpção inválida. Tente novamente.\n')
        os.system('pause')
        os.system('cls')
        info()
    
menu()