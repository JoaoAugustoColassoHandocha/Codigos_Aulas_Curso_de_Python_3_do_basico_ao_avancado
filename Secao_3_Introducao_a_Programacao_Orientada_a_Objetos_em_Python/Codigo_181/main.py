'''
Update Codigo_181.py

'''

import os
from log import LogPrintMixin, LogFileMixin

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

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')