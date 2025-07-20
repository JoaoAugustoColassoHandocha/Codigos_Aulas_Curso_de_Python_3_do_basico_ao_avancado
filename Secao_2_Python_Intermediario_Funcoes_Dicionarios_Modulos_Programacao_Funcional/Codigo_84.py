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

qtd_acertos = 0

for pergunta in perguntas:
    
    print('Pergunta:', pergunta['pergunta'])
    
    print('\n')

    opcoes = pergunta['opcoes']
    
    for i, opcao in enumerate(opcoes):
        
        print(f'{i})', opcao)
    
    print('\n')

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        
        escolha_int = int(escolha)

    if escolha_int is not None:
        
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
        
            if opcoes[escolha_int] == pergunta['resposta']:
        
                acertou = True

    print('\n')
    
    if acertou:
        
        qtd_acertos += 1
        
        print('Acertou 👍')
    
    else:
    
        print('Errou ❌')

    print('\n')


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

os.system('pause')
os.system('cls')