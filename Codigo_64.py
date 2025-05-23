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

'''

import os

os.system('color 1f')

while True:
    
    cpf = input('\nDigite o CPF (somente números): ')
    
    os.system('cls')
    
    if len(cpf) == 11:
        
        try:
            
            nove_digitos = cpf[:9]
            contador_regressivo = 10
            resultado = 0
            
            for digito in nove_digitos:
                
                resultado += int(digito) * contador_regressivo
                contador_regressivo -= 1
            
            digito = (resultado * 10) % 11
            
            digito = digito if digito <= 9 else 0
            
            if str(digito) == cpf[9]:
                
                print('\nO primeiro dígito do CPF é verdadeiro!\n')
                os.system('pause')
                os.system('cls')
                break
            
            elif str(digito) != cpf[9]:
                
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