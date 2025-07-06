# EXERCÍCIOS

import os

os.system('color 1f')

'''
* Faça um programa que peça ao usuário para digitar um número inteiro;
* Informe se este número é par ou Ímpar;
* Caso o usuário não digite um número inteiro, informe que não é um número inteiro;

'''

num_inteiro = input('\nDigite um número inteiro: ')

os.system('cls')

if num_inteiro.isdigit() == True:
    
    if int(num_inteiro) % 2 == 0:
        
        print(f'\nO número {num_inteiro} é par.\n')
        
    elif int(num_inteiro) % 2 == 1:
        
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

hrs = input('\nHora: ')
min = input('\nMinuto: ')

os.system('cls')

if hrs.isdigit() and min.isdigit() == True:

    if int(hrs) >= 0 and int(hrs) <= 11:
        
        if int(min) >= 0 and int(min) <= 59:
        
            print(f'\nBom dia, são {hrs}:{min}\n')
            
        elif int(min) < 0 or int(min) > 59:
            
            print('\nFavor inserir os minutos entre 0 a 59!\n')
            
        else:
        
            print('\nErro de processamento dos dados repassados\n')
        
    elif int(hrs) >= 12 and int(hrs) <= 17:
        
        if int(min) >= 0 and int(min) <= 59:
        
            print(f'\nBoa tarde, são {hrs}:{min}\n')
            
        elif int(min) < 0 or int(min) > 59:
            
            print('\nFavor inserir os minutos entre 0 a 59!\n')
            
        else:
        
            print('\nErro de processamento dos dados repassados\n')
        
    elif int(hrs) >= 18 and int(hrs) <= 23:
        
        if int(min) >= 0 and int(min) <= 59:
        
            print(f'\nBoa noite, são {hrs}:{min}\n')
            
        elif int(min) < 0 or int(min) > 59:
            
            print('\nFavor inserir os minutos entre 0 a 59!\n')
            
        else:
        
            print('\nErro de processamento dos dados repassados\n')
            
    elif int(hrs) < 0 or int(hrs) > 23:
        
        print('\nFavor inserir as horas entre 0 a 23!\n')

    else:
        
        print('\nErro de processamento dos dados repassados\n')

elif hrs.isdigit() == False or min.isdigit() == False:
    
    print('\nFavor inserir números inteiros!\n')
    
else:
    
    print('\nErro de processamento dos dados repassados\n')
    
os.system('pause')
os.system('cls')

'''
* Faça um programa que peça o primeiro nome do usuário;
* Se o nome tiver 4 letras ou menos, escreva 'Seu nome é curto';
* Se tiver entre 5 e 6 letras, escreva 'Seu nome 'normal';
* Maior que 6 letras escreva 'Seu nome é muito grande'.

'''

nome = input('\nQual o seu primeiro nome: ')

os.system('cls')

if bool(nome) == True:
    
    if len(nome) <= 1:
        
        print('\nFavor inserir seu nome correto!\n')
    
    elif len(nome) <= 4:
        
        print('\nSeu nome é curto!\n')
        
    elif len(nome) >= 5 and len(nome) <= 6:
        
        print('\nSeu nome é normal!\n')
        
    elif len(nome) > 6:
        
        print('\nSeu nome é muito grande!\n')
    
elif nome == '':
    
    print('\nDesculpe, você deixou algum dos campos vazio.')
    print('\nFavor preencher os campos corretamente!\n')
    
else:
    
    print('\nErro ao identificar os campos!\n')
    
os.system('pause')
os.system('cls')