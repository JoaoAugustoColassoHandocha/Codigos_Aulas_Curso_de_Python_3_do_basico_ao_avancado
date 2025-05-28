"""
Atividade:

Apresentar o valor maior.

"""

import os

os.system('color 1f')

def menu(valor1, valor2):
    
    print('\n============')
    print('VALOR MAIOR')
    print('============\n')

    valor1 = input('Digite o primeiro valor: ')
    valor2 = input('Digite o segundo valor: ')

    os.system('cls')
    
    valores(valor1, valor2)

def valores(valor1, valor2):

    if valor1 > valor2:
        
        print(f'\nO primeiro valor ({valor1}) é maior que o segundo valor ({valor2}).\n')
        os.system('pause')
        os.system('cls')
        menu(valor1 = 0, valor2 = 0)
        
    elif valor1 < valor2:
        
        print(f'\nO segundo valor ({valor2}) é maior que o primeiro valor ({valor1}).\n')
        os.system('pause')
        os.system('cls')
        menu(valor1 = 0, valor2 = 0)
        
    elif valor1 == valor2:
        
        print(f'\nOs valores 1 ({valor1}) e 2 ({valor2}) são iguais.\n')
        os.system('pause')
        os.system('cls')
        menu(valor1 = 0, valor2 = 0)
        
    else:
            
        print('\nValores inválidos.\n')
        os.system('pause')
        os.system('cls')
        menu(valor1 = 0, valor2 = 0)
        
menu(valor1 = 0, valor2 = 0)