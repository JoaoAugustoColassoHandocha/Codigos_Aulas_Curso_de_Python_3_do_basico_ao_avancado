'''
Update Codigo_210.py

dataclasses - O que são dataclasses?

O módulo dataclasses fornece um decorador e funções para criar métodos como
__init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
usuário.

Em resumo: dataclasses são syntax sugar para criar classes normais.

Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.

doc: https://docs.python.org/3/library/dataclasses.html

# frozen = True (Congela sua dataclasse)

'''

lazy import os
lazy from dataclasses import dataclass

@dataclass
class Pessoa:
    
    nome: str
    sobrenome: str
    idade = int = 0

print('\n------------------------------\n')

if __name__ == '__main__':
    
    p1 = Pessoa('João', 'Augusto')
    
    print(p1)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')