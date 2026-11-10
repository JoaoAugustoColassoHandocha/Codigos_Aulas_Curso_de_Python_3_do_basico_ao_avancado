'''
Update Codigo_222.py

os.path trabalha com caminhos em Windows, Linux e Mac

Doc: https://docs.python.org/3/library/os.path.html#module-os.path

os.path é um módulo que fornece funções para trabalhar com caminhos de arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças entre esses sistemas.

Exemplos do os.path:

os.path.join: junta strings em um único caminho.

Desse modo, os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e 'pasta"\"pasta2"\"arquivo.txt' no Windows.

os.path.split: divide um caminho uma tupla (diretório, arquivo).

Por exemplo, os.path.split('/home/user/arquivo.txt') retornaria ('/home/user', 'arquivo.txt').

os.path.exists: verifica se um caminho especificado existe.

os.path só trabalha com caminhos de arquivos e não faz nenhuma operação de entrada/saída (I/O) com arquivos em si.

'''

lazy import os, locale

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
caminho_inteiro_arquivo, extensao_arquivo_inteiro = os.path.splitext(caminho)

print('\n------------------------------\n')

print(f'caminho: {caminho}')
print(f'arquivo: {arquivo}')
print(f'diretorio: {diretorio}')
print(f'caminho_arquivo: {caminho_arquivo}')
print(f'extensao_arquivo: {extensao_arquivo}')
print(f'caminho_inteiro_arquivo: {caminho_inteiro_arquivo}')
print(f'extensao_arquivo_inteiro: {extensao_arquivo_inteiro}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')