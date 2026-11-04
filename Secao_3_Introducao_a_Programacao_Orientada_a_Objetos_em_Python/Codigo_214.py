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
lazy from pytz import timezone

print('\n------------------------------\n')

data = datetime(2026, 11, 4, 7, 49, 23)
print(data)

print('\n------------------------------\n')

data_str_data = '2026/11/04 07:49:23'
data_str_fmt = '%Y/%m/%d %H:%M:%S'
data_str = datetime.strptime(data_str_data, data_str_fmt)
print(data_str)

print('\n------------------------------\n')

data_str_data = '04/11/2026 07:49:23'
data_str_fmt = '%d/%m/%Y %H:%M:%S'
data_str = datetime.strptime(data_str_data, data_str_fmt)
print(data_str)

print('\n------------------------------\n')

data_now = datetime.now()
print(data_now)

print('\n------------------------------\n')

data_timezone = datetime.now(timezone('Asia/Tokyo'))
print(data_timezone)

print('\n------------------------------\n')

data_timezone_pre_def = datetime(2026, 11, 4, 7, 49, 23, tzinfo = timezone('Asia/Tokyo'))
print(data_timezone_pre_def)

print('\n------------------------------\n')

data_stamp = datetime.now()
print(data_stamp.timestamp())
print(datetime.fromtimestamp(1670849077.739638))

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')