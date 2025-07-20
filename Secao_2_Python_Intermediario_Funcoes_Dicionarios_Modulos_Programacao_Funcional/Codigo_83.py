'''
EXERCíCIO

Sistema de perguntas e respostas

'''

import os

os.system('color 1f')

def main(opcao_menu):
    
    print('\nBem vindo ao jogo de perguntas!\n')
    
    os.system('pause')
    os.system('cls')
    
    print('\n' + '-' * 20)
    print('[C] - Começar o Jogo')
    print('[S] - Sair')
    print('-' * 20 + '\n')
    
    opcao_menu = input('Escolha sua opção: ')
    
    os.system('cls')
    
    if opcao_menu == '' or opcao_menu == ' ':
        
        print('\nFavor inserir a opção desejada!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu)
        
    elif opcao_menu.upper() == 'C':
        
        jogo_perguntas(perguntas = '')
        
    elif opcao_menu.upper() == 'S':
        
        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')
        os.system('exit')
        
    elif opcao_menu.upper() != 'C' or opcao_menu.upper() != 'S':
        
        print('\nFavor digitar uma das opções repassadas!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu)
        
    else:
        
        print('\nErro no processamento da aplicação!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu)
        
def jogo_perguntas(perguntas):

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
    
    acertos = 0
    erros = 0
    alternativas = 1
    
    print(f'\n[1] - {perguntas['pergunta'[0]]}\n')
    
    for opcao in perguntas['opcoes'[0]]:
        
        print(f'{alternativas}) {opcao}')
        
        alternativas += 1
        
    resposta_1 = int(input('\nQual é a resposta: '))
    
    if resposta_1 == 4:
        
        print(f'Parabéns!!! Resposta certa é {perguntas['resposta'[0]]}')
        acertos += 1
        os.system('pause')
        os.system('cls')
    
    elif resposta_1 != 4:
        
        print(f'Errou!!! Que pena! Resposta certa é {perguntas['resposta'[0]]}')
        erros += 1
        os.system('pause')
        os.system('cls')
        
    else: 
        
        print('\nErro no processamento da aplicação!!!\n')
        os.system('pause')
        os.system('cls')
        main(opcao_menu = '')
        
main(opcao_menu = '')