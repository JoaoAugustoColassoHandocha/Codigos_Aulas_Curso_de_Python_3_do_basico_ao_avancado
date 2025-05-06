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
    
    esconde_palavra_secreta = ''
    
    i = 0
    
    for letra in palavra_secreta_sorteada:
       
        esconde_palavra_secreta += '*'
        
        i += 1
        
    print(f'\n{esconde_palavra_secreta}\n')
      
    while True:
        
        letra_secreta = input('Digite a letra que faz parte da palavra secreta (Para retornar, escreva "menu"): ')
        
        if letra_secreta.upper() == 'MENU':
            
            os.system('cls')
            main(op = '')
        
        elif letra_secreta == palavra_secreta_sorteada[i]:
            
            print(f'\nParabéns! Acertou a Letra: {esconde_palavra_secreta[i]}')
        
        os.system('cls')
        
        break
        

main(op = '')