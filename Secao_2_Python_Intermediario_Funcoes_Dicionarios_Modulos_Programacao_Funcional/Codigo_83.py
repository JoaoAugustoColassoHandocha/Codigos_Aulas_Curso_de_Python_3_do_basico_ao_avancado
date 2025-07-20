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

main(opcao_menu = '')

os.system('pause')
os.system('cls')