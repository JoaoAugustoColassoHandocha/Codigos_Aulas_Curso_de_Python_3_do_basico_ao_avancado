'''
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

            cpf_soma_1 = (cpf_int[0] * 10) + (cpf_int[1] * 9) + (cpf_int[2] * 8) + (cpf_int[3] * 7) + (cpf_int[4] * 6) + (cpf_int[5] * 5) + (cpf_int[6] * 4) + (cpf_int[7] * 3) + (cpf_int[8] * 2)
            
            cpf_rest_1 = (cpf_soma_1 * 10) % 11
            
            if cpf_rest_1 > 9:
                
                calc_primeiro_dig = 0
                
            elif cpf_rest_1 <= 9 or cpf_rest_1 >= 0:
                
                calc_primeiro_dig = cpf_rest_1
                
            else:
                
                print('\nErro!!! Favor entrar em contato com o suporte!\n')
                os.system('pause')
                os.system('cls')
                break
            
            cpf_soma_2 = (cpf_int[0] * 11) + (cpf_int[1] * 10) + (cpf_int[2] * 9) + (cpf_int[3] * 8) + (cpf_int[4] * 7) + (cpf_int[5] * 6) + (cpf_int[6] * 5) + (cpf_int[7] * 4) + (cpf_int[8] * 3) + (cpf_int[9] * 2)
            
            cpf_rest_2 = (cpf_soma_2 * 10) % 11
            
            if cpf_rest_2 > 9:
                
                calc_segundo_dig = 0
                
            elif cpf_rest_2 <= 9 or cpf_rest_2 >= 0:
                
                calc_segundo_dig = cpf_rest_2
                
            else:
                
                print('\nErro!!! Favor entrar em contato com o suporte!\n')
                os.system('pause')
                os.system('cls')
                break
            
            if calc_primeiro_dig == cpf_int[9] and calc_segundo_dig == cpf_int[10]:
                
                print('\nO CPF é verdadeiro!\n')
                os.system('pause')
                os.system('cls')
                break
            
            elif calc_primeiro_dig != cpf_int[9] or calc_segundo_dig != cpf_int[10]:
                
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

    elif cpf == '' or cpf == ' ' or len(cpf) >= 12 or len(cpf) < 11:
        
        print('\nCPF inválido!\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        os.system('pause')
        os.system('cls')
        break