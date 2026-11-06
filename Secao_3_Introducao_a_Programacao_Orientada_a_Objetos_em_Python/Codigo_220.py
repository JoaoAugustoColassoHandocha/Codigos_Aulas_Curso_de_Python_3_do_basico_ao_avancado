'''
Update Codigo_220.py

locale para internacionalização (tradução)

https://docs.python.org/3/library/locale.html
https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

'''

lazy import os, calendar, locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

print('\n------------------------------\n')

print(calendar.calendar(2026))
print()
print(locale.getlocale())

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')