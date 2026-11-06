'''
Update Codigo_219.py

Usando calendar para calendários e datas

https://docs.python.org/3/library/calendar.html

calendar é usado para coisas genéricas de calendários e datas.

Com calendar, você pode saber coisas como:

- Qual o último dia do mês (ex.: monthrange)
- Qual o nome e número do dia de determinada data (ex.: weekday)
- Criar um calendário em si (ex.: monthcalendar)
- Trabalhar com coisas específicas de calendários (ex.: calendar, month)

Por padrão dia da semana começa em 0 até 6

0 = segunda-feira | 6 = domingo

'''

lazy import os, calendar

print('\n------------------------------\n')

print(calendar.calendar(2026)) # Calendário ano

print('\n------------------------------\n')

print(calendar.month(2026, 11)) # Calendário mês

print('\n------------------------------\n')

print(calendar.monthrange(2026, 11)) # Último dia do mês

print('\n------------------------------\n')

print(list(enumerate(calendar.day_name)))

print('\n------------------------------\n')

numero_primeiro_dia, ultimo_dia = calendar.monthrange(2026, 11)

print(calendar.day_name[numero_primeiro_dia])

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')