'''
* Iterável -> str, range, entre outros (__iter__)
* Iterador -> Quem sabe entregar um valor por vez
* next -> Me entregue o próximo valor
* iter -> Me entregue seu iterador

'''

import os

os.system('color 1f')

numeros = range(0, 101, 8)
tst = iter('Joao')
texto_espaco = ' ' + 'Joao'
texto = iter(texto_espaco)
txt = next(texto)

print('\n')

for numero in numeros:
    
    print(numero)

print('\n')

os.system('pause')
os.system('cls')

# iter - Indica o endereço onde o objeto do interador está na memória.   
print(f'\n{texto}\n')

os.system('pause')
os.system('cls')

print('\n')

# Quando finaliza as informações repassadas, mas o next continua buscando, apresenta erro de 'StopIteration', realizando o cancelamento da próxima busca.
for txt in texto:

    print(txt)
    
print('\n')

os.system('pause')
os.system('cls')

print('\n')

while True:
    
    try:
        
        txt_rep = next(tst)
        
        print(txt_rep)
        
    except StopIteration:
        
        print('\nErro StopIteration tratado!')
        
        break
    
print('\n')

os.system('pause')
os.system('cls')