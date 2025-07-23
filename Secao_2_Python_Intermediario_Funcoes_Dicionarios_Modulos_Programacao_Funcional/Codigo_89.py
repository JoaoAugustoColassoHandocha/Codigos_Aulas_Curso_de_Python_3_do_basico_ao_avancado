'''
Exemplo de uso dos sets

'''

import os

os.system('color 1f')

letras = set()

while True:
    
    letra = input('Digite: ')
    letras.add(letra.lower())
    print(f'\n{letras}\n')
    
    if 'l' in letras:
        
        print('Parabéns!\n')
        
        break

os.system('pause')
os.system('cls')