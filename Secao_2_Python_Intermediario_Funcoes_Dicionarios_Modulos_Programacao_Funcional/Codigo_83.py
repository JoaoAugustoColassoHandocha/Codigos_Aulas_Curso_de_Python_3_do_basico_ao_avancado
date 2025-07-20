'''
EXERCíCIO

Sistema de perguntas e respostas

'''

import os

os.system('color 1f')

def menu():
    
    print('\nBem vindo ao jogo de perguntas!\n')
    
    os.system('pause')
    os.system('cls')
    
    print('\n' + '-' * 20)
    print('[C] - Começar o Jogo')
    print('[S] - Sair')
    print('-' * 20 + '\n')
    
    opcao_menu = input('Escolha sua opção: ')

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

os.system('pause')
os.system('cls')