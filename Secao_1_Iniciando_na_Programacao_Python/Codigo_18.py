"""  
Operadores de comparação (relacionais):

OP      Significado     Exemplo (True)
>       Maior           2 > 1
>=      Maior ou igual  2 >= 2
<       Menor           1 < 2
<=      Menor ou igual  2 <= 2
==      Igual           'a' == 'a'
!=     Diferente       'a' != 'b'   
    
"""

import os

os.system('color 1f')

maior = 2 > 1
maior_igual = 2 >= 2
menor = 1 < 2
menor_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

print(f'\nmaior: {maior}')
print(f'\nmaior_igual: {maior_igual}')
print(f'\nmenor: {menor}')
print(f'\nmenor_igual: {menor_igual}')
print(f'\nigual: {igual}')
print(f'\ndiferente: {diferente}\n')

os.system('pause')
os.system('cls')