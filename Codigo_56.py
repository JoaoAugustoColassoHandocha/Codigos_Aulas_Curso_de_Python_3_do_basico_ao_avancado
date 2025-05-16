'''
Imprecisão de ponto flutuante

Double-precision floating-point format IEEE 754

'''

import os, decimal

os.system('color 1f')

numero_1 = 0.1
numero_2 = 0.7

numero_3 = numero_1 + numero_2

# Apresenta o problema de imprecisão, imprimindo o valor 0.7999999999...
print('\n' + '+' * 10 + '\n')
print(numero_3)
print('\n' + '+' * 10 + '\n')

# Primeira forma de contornar, imprimindo 0.80
print(f'{numero_3:.2f}')
print('\n' + '+' * 10 + '\n')

# Segunda forma de contornar, imprimindo 0.8
print(round(numero_3, 1))
print('\n' + '+' * 10 + '\n')

# Terceira forma de contornar, imprimindo

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')

numero_3 = numero_1 + numero_2

print(numero_3)
print('\n' + '+' * 10 + '\n')

os.system('pause')
os.system('cls')