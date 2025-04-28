'''

Calculadora com while

.lower() - Converti maiusculo para minusculo.
.startwith - Começa com...
.endswith - Termina com...

except Exception as error  - apresenta o erro ocorrido. Ex:

try:

    ...
    
except Exception as error:

    print(error)

'''

import os

os.system('color 1f')

try:

    while True:
        
        print('\n' + '=' * 10 + 'Calculadora' + '=' * 10)
        print('\n[A] - Acessar')
        print('\n[S] - Sair')
        print('\n' + '=' * 31)
        
        op = input('\nEscolha uma opção: ').lower()
        
        os.system('cls')
        
        try:
        
            if op == 'a':
                
                print('\n' + '=' * 10 + 'Operadores' + '=' * 10)
                print('\n[1] - Soma')
                print('\n[2] - Subtração')
                print('\n[3] - Multiplicação')
                print('\n[4] - Divisão')
                print('\n' + '=' * 30)
                
                oper = int(input('\nEcolha um operador: '))
                
                os.system('cls')
                
                if oper == 1 or oper == 2 or oper == 3 or oper == 4:
                                       
                    n1 = float(input('\nDigite o primeiro número: '))
                    n2 = float(input('\nDigite o segundo número:'))
                
                    os.system('cls')
                            
                    if oper == 1:
                        
                        res = n1 + n2
                                    
                        print(f'\nO resultado de {n1:.2f} + {n2:.2f} = {res:.2f}\n')
                        os.system('pause')
                        os.system('cls')
                                    
                    elif oper == 2:
                        
                        res = n1 - n2
                                
                        print(f'\nO resultado de {n1:.2f} - {n2:.2f} = {res:.2f}\n')
                        os.system('pause')
                        os.system('cls')
                                
                    elif oper == 3:
                        
                        res = n1 * n2        
                                
                        print(f'\nO resultado de {n1:.2f} X {n2:.2f} = {res:.2f}\n')
                        os.system('pause')
                        os.system('cls')
                                
                    elif oper == 4:
                        
                        res = n1 / n2
                                
                        print(f'\nO resultado de {n1:.2f} / {n2:.2f} = {res:.2f}\n')
                        os.system('pause')
                        os.system('cls')
                                
                    else:
                        
                        os.system('cls')
                        print('\nErro na opção repassada!!!\n')
                        print('Favor verificar solicitação ou entrar em contato com o suporte técnico!\n')
                        os.system('pause')
                        os.system('cls')
                
                else:
                    
                    os.system('cls')
                    print('\nErro na opção repassada!!!\n')
                    print('Favor verificar solicitação ou entrar em contato com o suporte técnico!\n')
                    os.system('pause')
                    os.system('cls')
                
                    
            elif op == 's':
                
                print('\nSaindo...\n')
                
                os.system('pause')
                os.system('cls')
                break
            
            else:
                
                os.system('cls')
                print('\nErro na opção repassada!!!\n')
                print('Favor verificar solicitação ou entrar em contato com o suporte técnico!\n')
                os.system('pause')
                os.system('cls')
        
        except Exception as error:
            
            os.system('cls')
            print(f'\nErro: {error}\n')
            print('Favor verificar solicitação ou entrar em contato com o suporte técnico!\n')
            os.system('pause')
            os.system('cls')

except Exception as error:
    
    os.system('cls')
    print(f'\nErro: {error}\n')
    print('Favor entrar em contato com o suporte técnico!\n')
    os.system('pause')
    os.system('cls')