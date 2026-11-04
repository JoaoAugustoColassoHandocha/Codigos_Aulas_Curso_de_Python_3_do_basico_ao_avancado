'''
Update Codigo_214.py

Criando datas com módulo datetime

datetime(ano, mês, dia)

datetime(ano, mês, dia, horas, minutos, segundos)

datetime.strptime('DATA', 'FORMATO')

datetime.now()

https://pt.wikipedia.org/wiki/Era_Unix

datetime.fromtimestamp(Unix Timestamp)

https://docs.python.org/3/library/datetime.html

Para timezones

https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

Instalando o pytz

pip install pytz types-pytz

'''

lazy import os
lazy from datetime import datetime

print('\n------------------------------\n')

data = datetime(2026, 11, 4, 7, 49, 23)
print(data)

print('\n------------------------------\n')

data_str_data = '2026-11-04 07:49:23'
data_str_fmt = '%Y-%m'
data = datetime.strptime(data_str_data, data_str_fmt)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')