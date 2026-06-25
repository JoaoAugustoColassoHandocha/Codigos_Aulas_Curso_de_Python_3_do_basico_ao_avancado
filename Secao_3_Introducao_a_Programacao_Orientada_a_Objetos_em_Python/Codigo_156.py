'''


'''

import os

print('\n------------------------------\n')

class Pessoa:
    
    def __init__(self, nome, sobrenome):
        
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('João', 'Augusto')
p2 = Pessoa('Maria', 'Joana')

print(f'{p1.nome} {p1.sobrenome}\n')
print(f'{p2.nome} {p2.sobrenome}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')