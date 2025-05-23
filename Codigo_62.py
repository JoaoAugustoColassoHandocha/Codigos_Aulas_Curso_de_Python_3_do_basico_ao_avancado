'''
RESOLUÇÃO DO EXERCÍCIO DE OUTRA FORMA

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