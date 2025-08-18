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
    
except ZeroDivisionError  as error:
    
    print(f'{error.__class__.__name__}: {error}')
    
except NameError  as error:
    
    print(f'{error.__class__.__name__}: {error}')

except (TypeError, IndexError) as error:
    
    print('TypeError + IndexError')
    print(f'{error.__class__.__name__}: {error}')
    
except Exception  as error:
    
    print('ERRO DESCONHECIDO.')
    print(f'{error.__class__.__name__}: {error}')

print('\n##############################\n')

os.system('pause')
os.system('cls')