'''
while / else

* Quando o laço while é executado completamente, o else é executado.

* Quando é executado um break no while, não será executado o else também.

'''
import os

os.system('color 1f')

valor1 = 'Repassando um valor'
x = 0
y = 0

print('\n')

while x < len(valor1):
    
    letra = valor1[x]
    
    if letra == ' ':
        
        print('\nEncontrei um espaço vazio!\n')
        break
    
    print(letra)
    
    x += 1
    
else:
    
    print('\nNão encontrei espaço vazio!\n')
    
os.system('pause')
os.system('cls')

####################################

valor2 = 'Repassandoumvalor'

print('\n')

while y < len(valor2):
    
    letra = valor2[y]
    
    if letra == ' ':
        
        print('\nEncontrei um espaço vazio!\n')        
        break
    
    print(letra)
    
    y += 1
    
else:
    
    print('\nNão encontrei espaço vazio!\n')
    
os.system('pause')
os.system('cls')