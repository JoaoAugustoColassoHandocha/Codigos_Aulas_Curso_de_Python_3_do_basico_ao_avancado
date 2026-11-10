'''
Update Codigo_224.py

os.walk para navegar de caminhos de forma recursiva

os.walk é uma função que permite percorrer uma estrutura de diretórios de maneira recursiva.

Ela gera uma sequência de tuplas, onde cada tupla possui três elementos: o diretório atual (root), uma lista de subdiretórios (dirs) e uma lista dos arquivos do diretório atual (files).

'''

lazy import os, locale

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

caminho = os.path.join('C:\\Temp', 'Desktop')

print('\n------------------------------\n')

for root, dirs, files in os.

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')