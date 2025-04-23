'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

'''

import os

os.system('color 1f')

cont = 0

while cont < 10:
    
    cont = cont + 1

    print(f'\n_{cont}_')
    
    
print('\nAcabou\n')
os.system('pause')
os.system('cls')