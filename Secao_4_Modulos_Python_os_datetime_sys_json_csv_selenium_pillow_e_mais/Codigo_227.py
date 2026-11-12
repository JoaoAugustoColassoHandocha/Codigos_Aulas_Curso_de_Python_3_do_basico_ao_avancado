'''
Update Codigo_227.py

os + shutil - Apagando, copiando, movendo e renomeando pastas com Python

Vamos copiar arquivos de uma pasta para outra.

Copiar -> shutil.copy

Copiar Árvore recursivamente -> shutil.copytree

Apagar Árvore recursivamente -> shutil.rmtree

Apagar arquivos -> os.unlink

Renomear/Mover -> shutil.move ou os.rename

'''

lazy import os, locale, shutil

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

HOME = os.path.expanduser('~')
DOCUMENTOS = os.path.join(HOME, 'Documentos')
PASTA_ORIGINAL = os.path.join(DOCUMENTOS, 'Desktop')
NOVA_PASTA = os.path.join(DOCUMENTOS, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA)

input('...')

shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')