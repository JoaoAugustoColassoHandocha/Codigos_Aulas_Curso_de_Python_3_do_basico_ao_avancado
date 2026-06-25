'''
class - Classes são moldes para criar novos objetos

As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.

Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

Por convenção, usamos PascalCase (Ex: CriarBaseDeDados) para nomes de classes.

'''

import os

string = 'João' # Classe str

print('\n------------------------------\n')

print(string.upper())
print('\n')
print(isinstance(string, str))

print('\n------------------------------\n')

class Pessoa:
    
    ...

p1 = Pessoa()

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')