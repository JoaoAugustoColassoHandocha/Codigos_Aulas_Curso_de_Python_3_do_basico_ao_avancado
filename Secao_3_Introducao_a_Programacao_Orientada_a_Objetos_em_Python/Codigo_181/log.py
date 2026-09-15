'''
Update Codigo_181.py

Abstração

'''

import os

class Log:
    
    def log(self, msg):
        
        raise NotImplementedError('Implemente o método log')
    
class LogFileMixin(Log):

print('\n------------------------------\n')

if __name__ == '__main__':

    l = Log()
    l.log('Qualquer coisa')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')