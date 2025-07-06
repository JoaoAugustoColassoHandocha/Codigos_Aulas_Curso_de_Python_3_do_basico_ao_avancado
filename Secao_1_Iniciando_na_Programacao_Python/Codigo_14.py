import os

os.system('color 1f')

a = 'A'
b = 'B'
c = 1.1
string_1 = '| a = {} | b = {} | c = {:.2f} |'
string_2 = '| a = {2:.2f} | b = {0} | c = {1} |' # Índices
string_3 = '| a = {nome1} | b = {nome2} | c = {nome3:.2f} |'
formato_1 = string_1.format(a, b, c)
formato_2 = string_2.format(a, b, c)
formato_3 = string_3.format(nome1 = a, nome2 = b, nome3 = c) # Parametro nomeado


print(f'\n{formato_1}')
print(f'{formato_2}')
print(f'{formato_3}\n')

os.system('pause')
os.system('cls')