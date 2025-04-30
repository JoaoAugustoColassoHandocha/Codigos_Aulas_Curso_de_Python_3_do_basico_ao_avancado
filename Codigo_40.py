'''
Laço de repetição FOR/IN

* Utilizar o while quando não saber quantas repetições serão necessárias

'''

import os

os.system('color 1f')

texto = 'Python'
i = 0
texto_modificado = ''

print('\n')

for letra in texto:
    
    i += 1
    
    texto_modificado += f'*{letra}'
    
    print(f'{letra} - {i}')
    
print(f'\n{texto_modificado}*\n')

os.system('pause')
os.system('cls')