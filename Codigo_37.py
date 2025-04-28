'''

Calculadora com while

.lower() - Converti maiusculo para minusculo.
.startwith - Começa com...
.endswith - Termina com...

'''

import os

os.system('color 1f')

cls = os.system('cls')
pause = os.system('pause')

try:

    while True:
        
        print('\n' + '=' * 10 + 'Calculadora' + '=' * 10)
        print('\n[S] - Sair')
        print('\n' + '=' * 31)
        
        op = input('Escoha uma opção: ')
        
        try:
        
            if op.lower():
                
                
            
            elif op.lower() == s:
                
                print('\nSaindo...\n')
                pause
                cls
                break
            
            else:
                
                print('\nErro na opção repassada!!!\n')
                print('Favor verificar solicitação ou entrar em contato com o suporte técnico!\n')
                pause
                cls
        
        except:
            
            print('\nErro no processamento do dado repassado!!!\n')
            print('Favor verificar solicitação ou entrar em contato com o suporte técnico!\n')
            pause
            cls

except:
    
    print('\nErro na execução do programa!!!\n')
    print('Favor entrar em contato com o suporte técnico!\n')
    pause
    cls