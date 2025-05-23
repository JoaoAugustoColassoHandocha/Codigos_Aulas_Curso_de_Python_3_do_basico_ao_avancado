'''
RESOLUÇÃO DO EXERCÍCIO DE OUTRA FORMA

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0

________________________

Outra forma para verificar se o CPF é válido:

cpf = 74682489070

cpf_gerado_calculo = {nove_digitos}{digito_1}{digito_2}

if cpf == cpf_gerado_calculo:

    print(f'{cpf} válido')
    
elif cpf != cpf_gerado_calculo:

    print(f'{cpf} inválido')
    
else:

    print('CPF inválido')

'''

import os

os.system('color 1f')

while True:
    
    cpf = input('\nDigite o CPF (somente números): ')
    
    os.system('cls')
    
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