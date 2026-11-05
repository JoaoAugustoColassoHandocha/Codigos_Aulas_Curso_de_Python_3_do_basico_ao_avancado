'''
Update Codigo_215.py

datetime.timedelta e dateutil.relativetimedelta (calculando datas)

Docs:

https://dateutil.readthedocs.io/en/stable/relativedelta.html
https://docs.python.org/3/library/datetime.html#timedelta-objects

'''

lazy import os
lazy from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta = data_fim - data_inicio

print('\n------------------------------\n')

print(data_inicio)
print(data_fim)
print(data_fim > data_inicio)
print(data_fim == data_inicio)
print(data_fim < data_inicio)
print(delta)
print(delta.days, delta.seconds, delta.microseconds)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')