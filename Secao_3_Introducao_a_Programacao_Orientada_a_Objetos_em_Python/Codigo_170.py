'''
Encapsulamento (modificadores de acesso: public, protected, private)

Python NÃO TEM modificadores de acesso, mas podemos seguir as seguintes convenções:

(sem underline) = public - pode ser usado em qualquer lugar

_ (um underline) = protected - não DEVE ser usado fora da classe ou suas subclasses.

__ (dois underlines) = private - "name mangling" (desfiguração de nomes) em Python

_NomeClasse__nome_attr_ou_method - só DEVE ser usado na classe em que foi declarado.

'''

import os

print('\n------------------------------\n')

class Foo:
    
    def __init__(self):
        
        ...

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')