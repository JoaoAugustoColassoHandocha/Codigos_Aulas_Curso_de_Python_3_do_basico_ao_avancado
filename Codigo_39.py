'''
.count(palavra) -  Método para buscar quantas vezes a palavra ou letra foi repassada na frase ou texto.

.upper() - Insere o texto ou palavra todo MAIÚSCULO.

.lower() - Insere o texto ou palavra todo minúsculo.

'''

import os

os.system('color 1f')

# \ - quebra de linha no código
frase = 'O python é uma linguagem de programação'\
        'multiparadigma. '\
        'Python foi criado por Guido Van Rossum.'.upper()
        
print(f'\nQuantas vezes apareceu a palavra "Python": {frase.count('PYTHON')}')
print(f'\nQuantas vezes apareceu a letra "A": {frase.count('A')}\n')

os.system('pause')
os.system('cls')

i = 0

qtd_mais_vzs_letra = 0
mais_vzs_letra = ''

while i < len(frase):
    
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        
        i += 1
        
        continue
    
    n_vez_letra = frase.count(letra_atual)
    
    if qtd_mais_vzs_letra < n_vez_letra:
        
        qtd_mais_vzs_letra = n_vez_letra
        
        mais_vzs_letra = letra_atual
    
    i += 1
    
print(f'\nA letra que mais apareceu foi "{mais_vzs_letra}", sendo {qtd_mais_vzs_letra} vezes.\n')

os.system('pause')
os.system('cls')