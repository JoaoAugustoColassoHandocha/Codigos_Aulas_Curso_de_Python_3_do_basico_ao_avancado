'''
* Iterável -> str, range, entre outros
* Iterador -> Quem sabe entregar um valor por vez
* next -> Me entregue o próximo valor
* iter -> Me entregue seu iterador

'''

import os

os.system('color 1f')

numeros = range(0, 101, 8)

print('\n')

for numero in numeros:
    
    print(numero)
    
print('\n')

os.system('pause')
os.system('cls')