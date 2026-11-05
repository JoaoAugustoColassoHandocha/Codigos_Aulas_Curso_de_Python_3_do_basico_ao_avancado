'''
Update Codigo_216.py

Formatando datas do datetime

datetime.strftime('DATA', 'FORMATO')

https://docs.python.org/3/library/datetime.html

'''

lazy import os
lazy from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')

print('\n------------------------------\n')

print(data)
print(data.strftime(fmt))
print('\nstr | int')
print(f'{data.strftime('%Y')} | {data.year}')
print(f'{data.strftime('%m')} | {data.month}')
print(f'{data.strftime('%d')} | {data.day}')
print(f'{data.strftime('%H')} | {data.hour}')
print(f'{data.strftime('%M')} | {data.minute}')
print(f'{data.strftime('%S')} | {data.second}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')

fmt_now = '%d/%m/%Y %H:%M:%S'
data_now = datetime.now()

while True:
    
    print(data_now)