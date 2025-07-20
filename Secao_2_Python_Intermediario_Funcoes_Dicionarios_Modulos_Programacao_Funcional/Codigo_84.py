'''
EXERCíCIO

Sistema de perguntas e respostas

'''

import os

os.system('color 1f')

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

for pergunta in perguntas:
    
    print(f'Pergunta: {pergunta['pergunta']}')
    print('\n')
    
    for i, opcao in enumerate(pergunta['opcoes']):
        print(f'{i}) {opcao}')
        
    print('\n')
    
    escolha = input('Escolha uma opção: ')
    
    print('\n')