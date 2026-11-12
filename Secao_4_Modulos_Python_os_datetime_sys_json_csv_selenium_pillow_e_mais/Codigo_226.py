'''
Update Codigo_226.py

os + shutil - Mover, copiar e apagar arquivos

Vamos copiar arquivos de uma pasta para outra.

Copiar -> shutil.copy
Mover/Renomear -> shutil.move
Mover/Renomear -> os.rename
Apagar -> os.unlink
Apagar diretório recursivamente -> shutil.rmtree

'''

lazy import os, locale, shutil

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

HOME = os.path.expanduser('~')
DOCUMENTOS = os.path.join(HOME, 'Documentos')
PASTA_ORIGINAL = os.path.join(DOCUMENTOS, 'Desktop')

print('\n------------------------------\n')

print(HOME)
print(DOCUMENTOS)
print(PASTA_ORIGINAL)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')