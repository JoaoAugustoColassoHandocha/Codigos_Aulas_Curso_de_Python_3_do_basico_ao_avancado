'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.

'''

import os

os.system('color 1f')

cond = True

while cond:
    
    name = input('\nQual o seu nome: ')
    
    os.system('cls')
    
    if name == 'Joao':
             
        cond = False
        
    else:
        
        print(f'\nSeu nome é {name} e está errado\n')
        os.system('pause')
        os.system('cls')
        
print(f'\nSeu nome é {name} e está certo\n')

os.system('pause')
os.system('cls')