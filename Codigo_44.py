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
        
    if op == '' or op == ' ':
        
        print('\nFavor repassar a opção desejada!!!\n')
        os.system('pause')
        os.system('cls')
        main(op)
        
    elif op.upper() == 'C':
             
        jogo()
        
    elif op.upper() == 'S':
        
        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')
        
    elif op.upper() != 'C' or op.upper() != 'S':
        
        print('\nFavor digitar uma das opções repassadas!!!\n')
        os.system('pause')
        os.system('cls')
        main(op = '')
        
    else:
        
        print('\nErro no processamento dos dados!!!\n')
        os.system('pause')
        os.system('cls')
        main(op = '')
        
    
def jogo():
    
    palavras_secretas = ['teste', 'banana', 'dia', 'noite', 'tarde', 'sol', 'lua', 'cafe', 'amor', 'pao', 'pai', 'mae', 'filho', 'filha', 'neto', 'neta', 'avo', 'tio', 'tia']
    
    palavra_secreta_sorteada = random.choice(palavras_secretas)
    
    esconde_palavra_secreta = ''
    
    letras_acertadas = ''
    
    i = 0
    
    for letra in palavra_secreta_sorteada:
       
        esconde_palavra_secreta += '*'
        
        i += 1
        
    print(f'\nA palavra sortiada é: {esconde_palavra_secreta}\n')
      
    while True:
        
        letra_secreta = input('Digite a letra que faz parte da palavra secreta (Para retornar, escreva "menu"): ')
        
        os.system('cls')
        
        if letra_secreta.upper() == 'MENU':
            
            main(op = '')
            
        elif len(letra_secreta) > 1:
            
            print('\nFavor repassar somente uma letra!!!\n')
            os.system('pause')
            os.system('cls')
            jogo()
        
        elif letra_secreta in palavra_secreta_sorteada:
            
            letras_acertadas += letra_secreta
            
        for letra_secreta in palavra_secreta_sorteada:
            
            if letra_secreta in letras_acertadas:
                
                print(letra_secreta)
                
            else:
                
                print('*')
        
        print('\n')


main(op = '')