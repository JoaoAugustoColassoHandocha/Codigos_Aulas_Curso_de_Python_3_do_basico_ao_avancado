'''
EXERCíCIO

Sistema de perguntas e respostas

'''

import os

os.system('color 1f')

# Declaração da função do menu do sistema
def main(opcao_menu):

    # Apresentação das opções do menu
    print('\n' + '-' * 20)
    print('[C] - Começar o Jogo')
    print('[S] - Sair')
    print('-' * 20 + '\n')
    
    # Solicitação de escolha de uma das opções solicitadas anteriormente
    opcao_menu = input('Escolha sua opção: ')
    
    os.system('cls')
    
    # Caso seja repassado uma opção vazia, solicita que seja inserido a opção desejada, retornando novamente ao menu inicial
    if opcao_menu == '' or opcao_menu == ' ':
        
        print('\nFavor inserir a opção desejada!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu)
    
    # Caso a opção "C" seja escolhida, é executado o jogo
    elif opcao_menu.upper() == 'C':
        
        jogo_perguntas(perguntas = '')

    # Caso a opção "S" seja escolhida, é encerrado o programa
    elif opcao_menu.upper() == 'S':
        
        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')
        os.system('exit')
    
    # Caso seja repassado outra opção que não seja "C" ou "S", é solicitado digitar a opção correta, sendo retornado ao menu    
    elif opcao_menu.upper() != 'C' or opcao_menu.upper() != 'S':
        
        print('\nFavor digitar uma das opções repassadas!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu)
    
    # Caso apresente qualquer informação incorreta, repassa mensagem de erro e retorna ao menu    
    else:
        
        print('\nErro no processamento da aplicação!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu)

# Declaração da função do jogo
def jogo_perguntas(perguntas):

    # Lista dos dicionários das perguntas do jogo
    perguntas = [
        
        {
            
            'pergunta': 'Quanto é 2 + 2?',
            'opcoes': ['1', '2', '3', '4'],
            'resposta': '4',
            
        },
        
        {
            
            'pergunta': 'Quanto é 5 X 5?',
            'opcoes': ['25', '55', '10', '51'],
            'resposta': '25',
            
        },
        
        {
            
            'pergunta': 'Quanto é 10 / 2?',
            'opcoes': ['4', '5', '2', '1'],
            'resposta':'5',
            
        },
        
    ]
    
    # Número de acertos e erros
    acertos = 0
    erros = 0
    
    # Pergunta 1
    print(f'\n[1] - {perguntas[0]['pergunta']}\n')
    
    alternativas = 1
    
    for opcao in perguntas[0]['opcoes']:
        
        print(f'{alternativas}) {opcao}')
        
        alternativas += 1
        
    resposta_1 = int(input('\nQual é a resposta: '))
    
    os.system('cls')
    
    if resposta_1 == 4:
        
        print(f'\nParabéns!!! Resposta certa é {perguntas[0]['resposta']}\n')
        acertos += 1
        os.system('pause')
        os.system('cls')
    
    elif resposta_1 != 4:
        
        print(f'\nErrou!!! Que pena! Resposta certa é {perguntas[0]['resposta']}\n')
        erros += 1
        os.system('pause')
        os.system('cls')
        
    else: 
        
        print('\nErro no processamento da aplicação!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu = '')
        
    # Pergunta 2
    print(f'\n[2] - {perguntas[1]['pergunta']}\n')
    
    alternativas = 1
    
    for opcao in perguntas[1]['opcoes']:
        
        print(f'{alternativas}) {opcao}')
        
        alternativas += 1
        
    resposta_2 = int(input('\nQual é a resposta: '))
    
    os.system('cls')
    
    if resposta_2 == 1:
        
        print(f'\nParabéns!!! Resposta certa é {perguntas[1]['resposta']}\n')
        acertos += 1
        os.system('pause')
        os.system('cls')
    
    elif resposta_2 != 1:
        
        print(f'\nErrou!!! Que pena! Resposta certa é {perguntas[1]['resposta']}\n')
        erros += 1
        os.system('pause')
        os.system('cls')
        
    else: 
        
        print('\nErro no processamento da aplicação!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu = '')
        
    # Pergunta 3
    print(f'\n[3] - {perguntas[2]['pergunta']}\n')
    
    alternativas = 1
    
    for opcao in perguntas[2]['opcoes']:
        
        print(f'{alternativas}) {opcao}')
        
        alternativas += 1
        
    resposta_3 = int(input('\nQual é a resposta: '))
    
    os.system('cls')
    
    if resposta_3 == 2:
        
        print(f'\nParabéns!!! Resposta certa é {perguntas[2]['resposta']}\n')
        acertos += 1
        os.system('pause')
        os.system('cls')
    
    elif resposta_3 != 2:
        
        print(f'\nErrou!!! Que pena! Resposta certa é {perguntas[2]['resposta']}\n')
        erros += 1
        os.system('pause')
        os.system('cls')
        
    else: 
        
        print('\nErro no processamento da aplicação!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu = '')
        
    # Resultado
    

# Mensagem de boas vindas
print('\n' + '=' * 31 + '\nBem vindo ao jogo de perguntas!\n' + '=' * 31 + '\n')
os.system('pause')
os.system('cls')

main(opcao_menu = '')