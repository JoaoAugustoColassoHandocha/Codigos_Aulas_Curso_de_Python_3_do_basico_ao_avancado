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

        cpf_soma = cpf_num[0] + cpf_num[1] + cpf_num[2] + cpf_num[3] + cpf_num[4] + cpf_num[5] + cpf_num[6] + cpf_num[7] + cpf_num[8]
        
        print(cpf_soma)
        print('\n')
        break

    elif cpf == '' or cpf == ' ' or len(cpf) >= 12 or len(cpf) < 11:
        
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