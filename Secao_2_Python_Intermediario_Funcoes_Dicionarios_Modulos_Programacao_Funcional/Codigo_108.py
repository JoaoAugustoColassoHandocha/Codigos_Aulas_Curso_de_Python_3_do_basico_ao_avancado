'''
Try, except, else e finally

* finally sempre será executado, mesmo que ocorra um erro.

'''

import os

os.system('color 1f')

print('\n##############################\n')

try:
    
    print('Abrir arquivo')
    8/0
    
except ZeroDivisionError  as error:
    
    print(f'{error.__class__.__name__}: {error}')
    
except NameError  as error:
    
    print(f'{error.__class__.__name__}: {error}')

except (TypeError, IndexError) as error:
    
    print(f'{error.__class__.__name__}: {error}')
    
except Exception  as error:
    
    print(f'{error.__class__.__name__}: {error}')
    
finally:
    
    print('Fechar arquivo')

print('\n##############################\n')

os.system('pause')
os.system('cls')