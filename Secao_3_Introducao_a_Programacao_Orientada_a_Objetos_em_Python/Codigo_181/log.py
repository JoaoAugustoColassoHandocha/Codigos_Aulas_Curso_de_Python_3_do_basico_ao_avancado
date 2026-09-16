'''
Update Codigo_181.py

Abstração

Herança - é um

'''

import os

class Log:
    
    def log(self, msg):
        
        raise NotImplementedError('Implemente o método log')
    
class LogFileMixin(Log):
    
    def log(self, msg):
        
        print(msg)
        
class LogPrintMixin(Log):
    
    def log(self, msg):
        
        print(msg)

print('\n------------------------------\n')

if __name__ == '__main__':

    l = LogFileMixin()
    l.log('Qualquer coisa')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')