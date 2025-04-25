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

while line  <= qtd_lines:
    
    print(f'\n{line}')
    
    line += 1
    
print('\nAcabou\n')

os.system('pause')
os.system('cls')