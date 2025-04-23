'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.

'''

import os

os.system('color 1f')

cond = True

while cond:
    
    name = input('\nQual o seu nome: ')
    
    os.system('cls')
    
    if name == 'Joao':
        
        print(f'\nSeu nome é {name} e está certo\n')
        os.system('pause')
        os.system('cls')
        
        break
        
    elif name != 'Joao':
        
        if name == 'exit' or 'sair':
            
            print('\nSaindo...\n')
            os.system('pause')
            os.system('cls')
            
            break
        
        else:
                    
            print(f'\nSeu nome é {name} e está errado\n')
            os.system('pause')
            os.system('cls')
                    
    else:
        
        print('\nErro no processamento do dado repassado\n')
        os.system('pause')
        os.system('cls')