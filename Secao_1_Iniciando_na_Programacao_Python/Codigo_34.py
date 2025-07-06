'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

'''
import os

os.system('color 1f')

contador = 0

while True:
    
    contador += 1
    
    if contador % 2 != 0:
        
        continue
    
    print(f'\n{contador}')
    
    if contador >= 10:
        
        break
    
print('\nAcabou\n')

os.system('pause')
os.system('cls')