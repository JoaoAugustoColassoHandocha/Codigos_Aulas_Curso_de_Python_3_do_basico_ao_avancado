'''
Criando Exceptions em Python Orientado a Objetos

Para criar uma Exception em Python, você só precisa herdar de alguma exceção da linguagem.

A recomendação da doc é herdar de Exception.

https://docs.python.org/3/library/exceptions.html

Criando exceções (comum colocar Error ao final)

Levantando (raise) / Lançando (throw) exceções

Relançando exceções

Adicionando notas em exceções (3.11.0)

'''

import os

class MyError(Exception):
    
    ...

print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')