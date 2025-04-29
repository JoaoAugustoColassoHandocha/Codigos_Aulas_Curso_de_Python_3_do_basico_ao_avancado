'''
* \ - quebra a linha.

* .count(palavra) -  Método para buscar quantas vezes a palavra ou letra foi repassada na frase ou texto.

* .upper() - Insere o texto ou palavra todo MAIÚSCULO.

* .lower() - Insere o texto ou palavra todo minúsculo.

'''

import os

os.system('color 1f')

frase = 'O python é uma linguagem de programação'\
        'multiparadigma. '\
        'Pyhton foi criado por Guido Van Rossum.'
        
print(f'\n{frase.count('python')}\n')

os.system('pause')
os.system('cls')