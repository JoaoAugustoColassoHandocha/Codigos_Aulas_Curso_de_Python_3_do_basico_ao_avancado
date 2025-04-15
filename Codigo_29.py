# EXERCÍCIOS

import os

os.system('color 1f')

'''
* Faça um programa que peça ao usuário para digitar um número inteiro;
* Informe se este número é par ou Ímpar;
* Caso o usuário não digite um número inteiro, informe que não é um número inteiro;

'''

num_inteiro = int(input('Digite um número inteiro: '))

if num_inteiro.isdigit() == True:
    
    if num_inteiro % 2 == 0:
        
        print(f'\nO número {num_inteiro} é par.\n')
        
    elif num_inteiro % 2 != 0:
        
        print(f'\nO número {num_inteiro} é ímpar.\n')
        
    else:
        
        print(f'\nErro no processamento do dado repassado!\n')
        
elif num_inteiro.isdigit() == False:
    
    print(f'\nO número {num_inteiro} não é um número inteiro!\n')

else:
    
    print(f'\nErro no processamento do dado repassado!\n')
    
os.system('pause')
os.system('cls')

'''
* Faça um programa que pergunte a hora ao usuário;
* Baseando-se no horário informado, exiba a saudação apropriada;
* Ex: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.

'''



'''
* Faça um programa que peça o primeiro nome do usuário;
* Se o nome tiver 4 letras ou menos, escreva 'Seu nome é curto';
* Se tiver entre 5 e 6 letras, escreva 'Seu nome 'normal';
* Maior que 6 letras escreva 'Seu nome é muito grande'.

'''