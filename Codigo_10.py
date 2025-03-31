import os

os.system('color 1f')

# Exemplo de uso de operadores lógicos

# Menu

def menu():
    
    print('\n====================================')
    print('Exemplo de uso de operadores lógicos')
    print('====================================\n')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Divisão Inteira')
    print('6 - Exponenciação')
    print('7 - Módulo (Resto da Divisão)')
    print('8 - Sair')
    print('\n====================================\n')
    
    op = int(input('Escolha uma opção: '))
    
    os.system('cls')
    
    if op == 1:
        
        adicao()
        
    elif op == 2:
        
        subtracao()
        
    elif op == 3:
        
        multiplicacao()
        
    elif op == 4:
        
        divisao()
    
    elif op == 5:
        
        divisao_inteira()
        
    elif op == 6:
        
        exponenciacao()
        
    elif op == 7:
        
        modulo()
        
    elif op == 8:
        
        print('\nFinalizando sistema...\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        print('\nErro!!!')
        print('\nFavor verificar os número da opção digitada.\n')
        os.system('pause')
        os.system('cls')
        menu()

# Adição

def adicao():
    
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    os.system('cls')

    soma  = a + b

    if soma > 10:
    
        print(f'\nA soma de {a} + {b} = {soma} é maior que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
    
    elif soma < 10:
        
        print(f'\nA soma de {a} + {b} = {soma} é menor que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif soma == 10:
        
        print(f'\nA soma de {a} + {b} = {soma} é igual a 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    else:
        
        print('\nErro no processamento da soma!!!')
        print('\nFavor verificar os números digitados.\n')
        os.system('pause')
        os.system('cls')
        menu()
    
# Subtração

def subtracao():

    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    os.system('cls')

    sub = a - b

    if sub > 10:
            
        print(f'\nA subtração de {a} - {b} = {sub} é maior que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif sub < 10:
        
        print(f'\nA subtração de {a} - {b} = {sub} é menor que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif sub == 10:
            
        print(f'\nA subtração de {a} - {b} = {sub} é igual a 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    else:
        
        print('\nErro no processamento da subtração!!!')
        print('\nFavor verificar os números digitados.\n')
        os.system('pause')
        os.system('cls')
        menu()
    
# Multiplicação

def multiplicacao():
    
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    os.system('cls')
    
    mult = a * b

    if mult > 10:
            
        print(f'\nA multiplicação de {a} * {b} = {mult} é maior que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif mult < 10:
        
        print(f'\nA multiplicação de {a} * {b} = {mult} é menor que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif mult == 10:
            
        print(f'\nA multiplicação de {a} * {b} = {mult} é igual a 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    else:
        
        print('\nErro no processamento da multiplicação!!!')
        print('\nFavor verificar os números digitados.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
# Divisão

def divisao():
    
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    os.system('cls')
    
    div = a / b

    if div > 10:
            
        print(f'\nA divisão de {a} / {b} = {div:.2f} é maior que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif div < 10:
        
        print(f'\nA divisão de {a} / {b} = {div:.2f} é menor que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif div == 10:
            
        print(f'\nA divisão de {a} / {b} = {div:.2f} é igual a 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    else:
        
        print('\nErro no processamento da divisão!!!')
        print('\nFavor verificar os números digitados.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
# Divisão Inteira

def divisao_inteira():
    
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    os.system('cls')
    
    div_int = a // b

    if div_int > 10:
            
        print(f'\nA divisão inteira de {a} // {b} = {div_int:.2f} é maior que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif div_int < 10:
        
        print(f'\nA divisão inteira de {a} // {b} = {div_int:.2f} é menor que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif div_int == 10:
            
        print(f'\nA divisão inteira de {a} // {b} = {div_int:.2f} é igual a 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    else:
        
        print('\nErro no processamento da divisão inteira!!!')
        print('\nFavor verificar os números digitados.\n')
        os.system('pause')
        os.system('cls')
        menu()

# Exponenciação

def exponenciacao():
    
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    os.system('cls')
    
    exp = a ** b

    if exp > 10:
            
        print(f'\nA exponenciação de {a} ** {b} = {exp} é maior que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif exp < 10:
        
        print(f'\nA exponenciação de {a} ** {b} = {exp} é menor que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif exp == 10:
            
        print(f'\nA exponenciação de {a} ** {b} = {exp} é igual a 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    else:
        
        print('\nErro no processamento da exponenciação!!!')
        print('\nFavor verificar os números digitados.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
# Módulo (Resto da Divisão)

def modulo():
    
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    os.system('cls')
    
    mod = a % b

    if mod > 10:
            
        print(f'\nO restro da divisão (Módulo) de {a} % {b} = {mod} é maior que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif mod < 10:
        
        print(f'\nO restro da divisão (Módulo) de {a} % {b} = {mod} é menor que 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    elif mod == 10:
            
        print(f'\nO restro da divisão (Módulo) {a} % {b} = {mod} é igual a 10.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
    else:
        
        print('\nErro no processamento do restro da divisão (Módulo)!!!')
        print('\nFavor verificar os números digitados.\n')
        os.system('pause')
        os.system('cls')
        menu()
        
print('\n+++++++++')
print('Exemplos:')
print('+++++++++\n')

ad = 10 + 10
print(f'Adição de 10 + 10: {ad}\n')

subt = 10 - 5
print(f'Subtração de 10 - 5: {subt}\n')

multi = 10 * 10
print(f'Multiplicação de 10 * 10: {multi}\n')

divi = 10 / 2.2 # Float - Sempre imprimi com ponto flutuante
print(f'Divisão de 10 / 2.2: {divi:.2f}\n')

divi_inteira = 10 // 2.2 # Todo número que vem depois do ponto, não virá
print(f'Divisão inteira de 10 // 2.2: {divi_inteira:.2f}\n')

expo = 2 ** 10
print(f'Exponenciação de 2 ** 10: {expo}\n')

modu = 55 % 5 # Resto da divisão
print(f'Módulo de 55 % 5: {modu}\n')

os.system('pause')
os.system('cls')

menu()