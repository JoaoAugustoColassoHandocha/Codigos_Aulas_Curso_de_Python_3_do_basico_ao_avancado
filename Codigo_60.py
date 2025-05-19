'''
Operação ternária (condicional de uma linha)

<valor> if <condição> else <outro valor>

'''

import os

os.system('color 1f')

##########################

print('\nValor\n' if True else '\nOutro valor\n')

##########################

condicao = 10 == 10
variavel = 'Igual a 10' if condicao else 'Não é igual a 10'

print(f'{variavel}\n')

##########################

digito_1 = 5
digito_2 = 12

novo_digito_1 = digito_1 if digito_1 <= 9 else 0
print(f'{novo_digito_1}\n')

novo_digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'{novo_digito_2}\n')

os.system('pause')
os.system('cls')