'''
Update Codigo_181.py

'''

from log import LogPrintMixin, LogFileMixin

lf = LogFileMixin()
lp = LogPrintMixin()
    
lf._log('Qualquer coisa')
lp._log('Qualquer coisa')
lf.log_error('Qualquer coisa')
lp.log_error('Qualquer coisa')
lf.log_success('Qualquer coisa')
lp.log_success('Qualquer coisa')