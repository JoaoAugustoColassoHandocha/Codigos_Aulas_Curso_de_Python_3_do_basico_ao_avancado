'''
Update Codigo_216.py

Formatando datas do datetime

datetime.strftime('DATA', 'FORMATO')

https://docs.python.org/3/library/datetime.html

'''

lazy import os
lazy from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')

print('\n------------------------------\n')

print(data.strftime(fmt))

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')