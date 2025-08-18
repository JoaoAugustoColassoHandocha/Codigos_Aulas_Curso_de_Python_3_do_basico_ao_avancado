'''
Try, except, else e finally

'''

import os

os.system('color 1f')

print('\n##############################\n')

try:
    
    a = 18
    b = 0
    print(b[0])
    print('Linha 1')
    c = a / b
    print('Linha 2')
    
except ZeroDivisionError:
    
    print('Dividiu por zero')
    
except NameError:
    
    print('Nome nãodefinido')

except (TypeError, IndexError):
    
    print('TypeError')
    
except Exception:
    
    print('ERRO DESCONHECIDO.')

print('\n##############################\n')

os.system('pause')
os.system('cls')