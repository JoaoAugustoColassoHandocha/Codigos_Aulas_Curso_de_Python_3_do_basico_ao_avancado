'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

'''

import os

os.system('color 1f')

qtd_lines = 5
qtd_coluns = 5

line = 1

while line <= qtd_lines:
    
    colun = 1
    
    while colun <= qtd_coluns:
        
        print(f'{line} - {colun}')
        
        colun += 1
    
    print('\n')
    
    line += 1
    
print('Acabou\n')

os.system('pause')
os.system('cls')