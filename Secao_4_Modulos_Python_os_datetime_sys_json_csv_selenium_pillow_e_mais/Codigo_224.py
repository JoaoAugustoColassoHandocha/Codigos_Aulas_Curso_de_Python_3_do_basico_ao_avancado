'''
Update Codigo_224.py

os.walk para navegar de caminhos de forma recursiva

os.walk é uma função que permite percorrer uma estrutura de diretórios de maneira recursiva.

Ela gera uma sequência de tuplas, onde cada tupla possui três elementos: o diretório atual (root), uma lista de subdiretórios (dirs) e uma lista dos arquivos do diretório atual (files).

'''

lazy import os, locale
lazy from itertools import count

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

caminho = os.path.join('C:\\Temp', 'Desktop')
counter = count()

print('\n------------------------------')

for root, dirs, files in os.walk(caminho):
    
    the_counter = next(counter)
    
    print()
    print(the_counter, 'Pasta atual:', root)
    
    for dir_ in dirs:
        
        print('     |_____', the_counter, 'Diretório:', dir_)
        
    for file_ in files:
        
        caminho_completo_arquivo = os.path.join(root, file_)
        print('     |_____', the_counter, 'Arquivo:', caminho_completo_arquivo)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')