'''
Faça um jogo para o usuário adivinhar qual a palavra secreta.

* Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.

* Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

* Se a letra digitada estiver na palavra secreta, exiba a letra

* Se a letra digitada não estar na palavra secreta, exiba "*"

Faça a contagem de tentativas do seu usuário.

'''

import os
import random

os.system('Color 1f')

def main(op):
    
    print('\n' + '=' * 10 + 'PALAVRA SECRETA' + '=' * 10 + '\n')
    print('[C] - Começar o Jogo')
    print('[S] - Sair')
    print('\n' + '=' * 35 + '\n')
    
    op = input('Opção: ')
    
    os.system('cls')
        
    
    if op.upper() == 'C':
             
        jogo()
        
    elif op.upper() == 'S':
        
        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')
        
    
def jogo():
    
    palavras_secretas = ['teste', 'banana', 'dia', 'noite', 'tarde', 'sol', 'lua', 'cafe', 'amor', 'pao', 'pai', 'mae', 'filho', 'filha', 'neto', 'neta', 'avo', 'tio', 'tia']
    
    palavra_secreta_sorteada = random.choice(palavras_secretas)
    
    tamanho_palavra = len(palavra_secreta_sorteada)
    
    esconde_palavra_secreta = ''
    
    i = 0
        
    for i in tamanho_palavra:
            
        esconde_palavra_secreta += '*'
    
    while True:
        
        print(f'\n{esconde_palavra_secreta}')
        
        letra_secreta = input('\nDigite a letra que faz parte da palavra secreta: ')
        
        os.system('cls')
        
        break
        

main(op = '')