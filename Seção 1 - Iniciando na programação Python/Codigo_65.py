'''
Possíveis problemas e soluções para o código de algoritmo do CPF.

.replace('o que quer substituir', 'para qual caracter quer substituir') - pode ser feito de forma encadeada.

[import re] - re.sub(r'o que quer substituir', 'para qual caracter quer substituir', 'dado repassado')

'''

import os, re

os.system('color 1f')

while True:
    
    cpf_1 = input('\nDigite o CPF: ')
    
    os.system('cls')
    
    corrigir_cpf = cpf_1.replace('.', '').replace('-', '').replace(' ', '')
    
    if len(corrigir_cpf) == 11:
        
        try:
            
            nove_digitos = corrigir_cpf[:9]
            contador_regressivo_1 = 10
            resultado_1 = 0
            
            for digito in nove_digitos:
                
                resultado_1 += int(digito) * contador_regressivo_1
                contador_regressivo_1 -= 1
            
            digito_1 = (resultado_1 * 10) % 11
            
            digito_1 = digito_1 if digito_1 <= 9 else 0
            
            dez_digitos = corrigir_cpf[:10]
            contador_regressivo_2 = 11
            resultado_2 = 0
            
            for digito in dez_digitos:
                
                resultado_2 += int(digito) * contador_regressivo_2
                contador_regressivo_2 -= 1
                
            digito_2 = (resultado_2 * 10) % 11
            
            digito_2 = digito_2 if digito_2 <= 9 else 0
            
            
            if str(digito_1) == corrigir_cpf[9] and str(digito_2) == corrigir_cpf[10]:
                
                print('\nO CPF é verdadeiro!\n')
                os.system('pause')
                os.system('cls')
                break
            
            elif str(digito_1) != corrigir_cpf[9] or str(digito_2) != corrigir_cpf[10]:
                
                print('\nO CPF é falso!\n')
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
        
    elif cpf_1 == '' or cpf_1 == ' ' or len(cpf_1) >= 12 or len(cpf_1) < 11:
        
        print('\nCPF inválido!\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        os.system('pause')
        os.system('cls')
        break
    
os.system('pause')
os.system('cls')

####################################################

while True:
    
    cpf_2 = input('\nDigite o CPF: ')
    
    os.system('cls')
    
    corrigir_cpf = re.sub(r'[^0-9]', '', cpf_2)
    
    if len(corrigir_cpf) == 11:
        
        try:
            
            nove_digitos = corrigir_cpf[:9]
            contador_regressivo_1 = 10
            resultado_1 = 0
            
            for digito in nove_digitos:
                
                resultado_1 += int(digito) * contador_regressivo_1
                contador_regressivo_1 -= 1
            
            digito_1 = (resultado_1 * 10) % 11
            
            digito_1 = digito_1 if digito_1 <= 9 else 0
            
            dez_digitos = corrigir_cpf[:10]
            contador_regressivo_2 = 11
            resultado_2 = 0
            
            for digito in dez_digitos:
                
                resultado_2 += int(digito) * contador_regressivo_2
                contador_regressivo_2 -= 1
                
            digito_2 = (resultado_2 * 10) % 11
            
            digito_2 = digito_2 if digito_2 <= 9 else 0
            
            
            if str(digito_1) == corrigir_cpf[9] and str(digito_2) == corrigir_cpf[10]:
                
                print('\nO CPF é verdadeiro!\n')
                os.system('pause')
                os.system('cls')
                break
            
            elif str(digito_1) != corrigir_cpf[9] or str(digito_2) != corrigir_cpf[10]:
                
                print('\nO CPF é falso!\n')
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
        
    elif cpf_2 == '' or cpf_2 == ' ' or len(cpf_2) >= 12 or len(cpf_2) < 11:
        
        print('\nCPF inválido!\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        os.system('pause')
        os.system('cls')
        break
    
os.system('pause')
os.system('cls')

####################################################

while True:
    
    cpf_3 = input('\nDigite o CPF: ')
    
    os.system('cls')
    
    corrigir_cpf = re.sub(r'[^0-9]', '', cpf_3)
    
    prim_char_ent_cpf_rep = corrigir_cpf == corrigir_cpf[0] * len(corrigir_cpf)
    
    if len(corrigir_cpf) == 11 and not prim_char_ent_cpf_rep:
        
        try:
            
            nove_digitos = corrigir_cpf[:9]
            contador_regressivo_1 = 10
            resultado_1 = 0
            
            for digito in nove_digitos:
                
                resultado_1 += int(digito) * contador_regressivo_1
                contador_regressivo_1 -= 1
            
            digito_1 = (resultado_1 * 10) % 11
            
            digito_1 = digito_1 if digito_1 <= 9 else 0
            
            dez_digitos = corrigir_cpf[:10]
            contador_regressivo_2 = 11
            resultado_2 = 0
            
            for digito in dez_digitos:
                
                resultado_2 += int(digito) * contador_regressivo_2
                contador_regressivo_2 -= 1
                
            digito_2 = (resultado_2 * 10) % 11
            
            digito_2 = digito_2 if digito_2 <= 9 else 0
            
            
            if str(digito_1) == corrigir_cpf[9] and str(digito_2) == corrigir_cpf[10]:
                
                print('\nO CPF é verdadeiro!\n')
                os.system('pause')
                os.system('cls')
                break
            
            elif str(digito_1) != corrigir_cpf[9] or str(digito_2) != corrigir_cpf[10]:
                
                print('\nO CPF é falso!\n')
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
        
    elif cpf_3 == '' or cpf_3 == ' ' or len(cpf_3) >= 12 or len(cpf_3) < 11 or prim_char_ent_cpf_rep:
        
        print('\nCPF inválido!\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        os.system('pause')
        os.system('cls')
        break
    
os.system('pause')
os.system('cls')