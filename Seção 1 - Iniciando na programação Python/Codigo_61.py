'''
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

'''

import os

os.system('color 1f')

while True:

    cpf = input('\nDigite o CPF (somente números): ')

    os.system('cls')
    
    if len(cpf) == 11:
        
        try:
        
            cpf_list = list(cpf)
            
            cpf_list_num = list(cpf_list)
            
            cpf_int = [int(i) for i in cpf_list_num]

            cpf_soma = (cpf_int[0] * 10) + (cpf_int[1] * 9) + (cpf_int[2] * 8) + (cpf_int[3] * 7) + (cpf_int[4] * 6) + (cpf_int[5] * 5) + (cpf_int[6] * 4) + (cpf_int[7] * 3) + (cpf_int[8] * 2)
            
            cpf_mult = cpf_soma * 10
            
            cpf_rest = cpf_mult % 11
            
            if cpf_rest > 9:
                
                calc_primeiro_dig = 0
                
            elif cpf_rest <= 9 or cpf_rest >= 0:
                
                calc_primeiro_dig = cpf_rest
                
            else:
                
                print('\nErro!!! Favor entrar em contato com o suporte!\n')
                os.system('pause')
                os.system('cls')
                break
                
            if calc_primeiro_dig == cpf_int[9]:
                
                print('\nO primeiro dígito do CPF é verdadeiro!\n')
                os.system('pause')
                os.system('cls')
                break
            
            elif calc_primeiro_dig != cpf_int[9]:
                
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