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
NOVA_PASTA = os.path.join(DOCUMENTOS, 'NOVA_PASTA')

os.makedirs(NOVA_PASTA, exist_ok = True)

print('\n------------------------------\n')

print(HOME)
print(DOCUMENTOS)
print(PASTA_ORIGINAL)
print(NOVA_PASTA)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    
    for file in files:

        # shutil.copy()
        
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = 

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')