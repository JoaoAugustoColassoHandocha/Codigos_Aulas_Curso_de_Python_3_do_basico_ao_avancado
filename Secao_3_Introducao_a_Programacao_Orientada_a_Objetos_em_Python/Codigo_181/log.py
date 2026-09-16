'''
Update Codigo_181.py

Abstração

Herança - é um

'''

import os
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    
    def _log(self, msg):
        
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
            
            return self._log(f'Success: {msg}')
class LogFileMixin(Log):
    
    def _log(self, msg):
        
        print(f'{msg} - {self.__class__.__name__}')
        
class LogPrintMixin(Log):
    
    def _log(self, msg):
        
        print(f'{msg} - {self.__class__.__name__}')

print('\n------------------------------\n')

if __name__ == '__main__':

    lf = LogFileMixin()
    lp = LogPrintMixin()
    
    lf._log('Qualquer coisa')
    lp._log('Qualquer coisa')
    lf.log_error('Qualquer coisa')
    lp.log_error('Qualquer coisa')
    lf.log_success('Qualquer coisa')
    lp.log_success('Qualquer coisa')
    print(LOG_FILE)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')