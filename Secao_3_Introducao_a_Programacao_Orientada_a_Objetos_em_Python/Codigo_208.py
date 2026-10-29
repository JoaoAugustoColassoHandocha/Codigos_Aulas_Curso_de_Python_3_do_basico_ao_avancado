'''
Update Codigo_208.py

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

@dataclass(repr = True)
class Pessoa:
    
    nome: str
    sobrenome: str

print('\n------------------------------\n')

if __name__ == '__main__':
    
    lista = [Pessoa('A', 'B'), Pessoa('C', 'D'), Pessoa('E', 'F')]
    
    # Funciona somente com order = True
    # ordenadas = sorted(lista)
    # print(ordenadas)
    
    ordenadas = sorted(lista, key = lambda p : p.nome)
    print(ordenadas)
    
    print()
    
    ordenadas_reverso = sorted(lista, reverse = True, key = lambda p : p.nome)
    print(ordenadas_reverso)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')