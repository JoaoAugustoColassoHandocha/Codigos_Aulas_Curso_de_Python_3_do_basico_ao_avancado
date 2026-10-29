'''
Update Codigo_206.py

dataclasses - O que são dataclasses?

O módulo dataclasses fornece um decorador e funções para criar métodos como
__init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
usuário.

Em resumo: dataclasses são syntax sugar para criar classes normais.

Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.

doc: https://docs.python.org/3/library/dataclasses.html

'''

lazy import os
lazy from dataclasses import dataclass

@dataclass
class Pessoa:
    
    nome: str
    idade: int

print('\n------------------------------\n')

if __name__ == '__main__':
    
    p1 = Pessoa('João', 28)
    p2 = Pessoa('João', 28)
    p3 = Pessoa('Maria', 24)
    
    print(p1)
    print(p2)
    print(p3)
    
    print()
    
    print(f'P1 == P2: {p1 == p2}')
    print(f'P1 == P3: {p1 == p3}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')