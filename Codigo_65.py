'''
Possíveis problemas e soluções para o código de algoritmo do CPF.

.replace('o que quer substituir', 'para qual caracter quer substituir') - pode ser feito de forma encadeada.

'''

import os

os.system('color 1f')

while True:
    
    cpf = input('\nDigite o CPF (somente números): ')
    
    os.system('cls')
    
    corrigir_cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    
    if len(cpf) == 11:
        
        try:
            
            nove_digitos = cpf[:9]
            contador_regressivo_1 = 10
            resultado_1 = 0
            
            for digito in nove_digitos:
                
                resultado_1 += int(digito) * contador_regressivo_1
                contador_regressivo_1 -= 1
            
            digito_1 = (resultado_1 * 10) % 11
            
            digito_1 = digito_1 if digito_1 <= 9 else 0
            
            dez_digitos = cpf[:10]
            contador_regressivo_2 = 11
            resultado_2 = 0
            
            for digito in dez_digitos:
                
                resultado_2 += int(digito) * contador_regressivo_2
                contador_regressivo_2 -= 1
                
            digito_2 = (resultado_2 * 10) % 11
            
            digito_2 = digito_2 if digito_2 <= 9 else 0
            
            
            if str(digito_1) == cpf[9] and str(digito_2) == cpf[10]:
                
                print('\nO primeiro dígito do CPF é verdadeiro!\n')
                os.system('pause')
                os.system('cls')
                break
            
            elif str(digito_1) != cpf[9] or str(digito_2) != cpf[10]:
                
                print('\nO primeiro dígito do CPF é falso!\n')
                os.system('pause')
                os.system('cls')
            
            else:
                
                print('\nErro!!! Favor entrar em contato com o suporte!\n')
                os.system('pause')
                os.system('cls')
                break
            
        except ValueError:
            
            print('\nCPF inválido!\n')
            os.system('pause')
            os.system('cls')
        
    elif cpf == '' or cpf == ' ' or len(cpf) >= 12 or len(cpf) < 11:
        
        print('\nCPF inválido!\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        os.system('pause')
        os.system('cls')
        break