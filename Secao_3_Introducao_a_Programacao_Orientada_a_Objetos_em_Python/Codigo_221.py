'''
Update Codigo_221.py

O módulo os para interação com o sistema

Doc: https://docs.python.org/3/library/os.html

O módulo `os` fornece funções para interagir com o sistema operacional.

Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de arquivos e a função os.listdir() pode ser usada para listar os arquivos em um diretório.

O método os.system() permite executar comandos do sistema operacional a partir do seu código Python.

Windows 11 (PowerShell), Linux, Mac = clear
Windows (antigo, cmd) = cls

'''

lazy import os, locale

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

os.system('cls' if os.name == 'nt' else 'clear')

print('\n------------------------------\n')

os.system('echo Hello world' if os.name == 'nt' else 'echo "Hello world"')
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')