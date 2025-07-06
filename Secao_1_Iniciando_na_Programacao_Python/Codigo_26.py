'''
Introdução ao try/except

* try - tentar executar o código
* except - se ocorrer um erro, execute o código dentro do except

'''

import os

os.system('color 1f')

def sol_num():
    
    print('\n'+ '=' * 10)
    print('[I] - IF/ELSE')
    print('[T] - TRY/EXCEPT')
    print('[S] - SAIR')
    print('=' * 10 + '\n')
    op = input('\nEscolha uma opção: ')
    os.system('cls')
    
    if op == 'I' or op == 'i':
        
        numero = input('\nDigite um número: ')
        os.system('cls')
        if_num(numero)
        
    elif op == 'T' or op == 't':
        
        numero = input('\nDigite um número: ')
        os.system('cls')
        try_except(numero)
        
    elif op == 'S' or op == 's':

        print('\nSaindo do sistema...\n')
        os.system('pause')
        os.system('cls')
    
    else:
        
        print('\nOpção inválida\n')
        os.system('pause')
        os.system('cls')
        sol_num()

# Exemplo de execução do sistema sem utilizar o try/except, onde ao inserir um número futuante, apresenta que não é dígito.
def if_num(numero):

    if numero.isdigit():
        
        print(f'\nO dobro de {numero} é {int(numero) * 2}\n')
        os.system('pause')
        os.system('cls')
        sol_num()

    elif numero != numero.isdigit():
        
        print(f'\nO número {numero} não é dígito\n')
        os.system('pause')
        os.system('cls')
        sol_num()
        
    else:
        
        print('\nFalha na execução do programa')
        print('\nVerifique se o número digitado\n')
        os.system('pause')
        os.system('cls')
        sol_num()

# Exemplo try/except

def try_except(numero):
    
    try:
        
        try:
            
            print(f'\nO dobro de {numero} é {int(numero) * 2}\n')
            os.system('pause')
            os.system('cls')
            sol_num()
        
        except ValueError:
            
            print(f'\nO dobro de {float(numero):.2f} é {float(numero) * 2:.2f}\n')
            os.system('pause')
            os.system('cls')
            sol_num()
        
    except ValueError:
        
        print('\nFalha na execução do programa')
        print('\nVerifique se o número digitado\n')
        os.system('pause')
        os.system('cls')
        sol_num()
        
sol_num()