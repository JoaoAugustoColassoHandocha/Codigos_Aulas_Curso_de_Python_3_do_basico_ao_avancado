import os

color = os.system('color 1f')

def menu():
    
    color
    print('\n=======================')
    print('Solicitação Informações')
    print('=======================\n')
    
    os.system('pause')
    os.system('cls')
    
    nome = input('\nDigite o nome: ')
    sobrenome = input('\nDigite o sobrenome: ') 
    idade = int(input('\nDigite a idade: '))
    dia_nasc = int(input('\nDigite o dia de nascimento: '))
    mes_nasc = int(input('\nDigite o mês de nascimento: '))
    ano_nasc = int(input('\nDigite o ano de nascimento: '))
    altura = float(input('\nDigite a altura: '))
    
    os.system('cls')
    
    resultado(nome, sobrenome, idade, dia_nasc, mes_nasc, ano_nasc, altura)

def resultado(nome, sobrenome, idade, dia_nasc, mes_nasc, ano_nasc, altura):

    print(f'\nNome: {nome}')
    print(f'\nSobrenome: {sobrenome}')
    print(f'\nIdade: ', idade)
    print(f'\nDia de Nascimento: {dia_nasc}')
    print(f'\nMês de Nascimento: {mes_nasc}')
    print(f'\nAno de Nascimento: {ano_nasc}')
    print(f'\nAltura: {altura:.2f}')

    if idade >= 18:
        
        print(f'\n{nome} {sobrenome}, nasceu em {dia_nasc}/{mes_nasc}/{ano_nasc}, tendo {idade} anos, com {altura:.2f}m de altura, sendo maior de idade!\n')
        os.system('pause')
        os.system('cls')

    elif idade < 18:
        
        print(f'\n{nome} {sobrenome}, nasceu em {dia_nasc}/{mes_nasc}/{ano_nasc}, tendo {idade} anos, com {altura:.2f}m de altura, sendo menor de idade!\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        print('\nErro!')
        print('\nVerifique os dados inseridos!\n')
        os.system('pause')
        os.system('cls')
        menu()
        
menu()