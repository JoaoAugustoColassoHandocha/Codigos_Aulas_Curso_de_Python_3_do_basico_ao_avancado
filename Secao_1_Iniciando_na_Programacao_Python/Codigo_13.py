import os

os.system('color 1f')

nome = 'João Augusto'
altura = 1.80
peso = 97.478
imc = ... # Ellipsis - placeholder para adicionar posteriormente o código.

imc = peso / (altura * altura)

print(f'\n{nome}, tem {altura:.2f} de altura, pesa {peso:.2f}kg e seu IMC é {imc:.2f}\n')

os.system('pause')
os.system('cls')