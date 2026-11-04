'''
Update Codigo_212.py

Implementando o protocolo do Iterator em Python

Essa é apenas uma aula para introduzir os protocolos de collections.abc no
Python.

Qualquer outro protocolo poderá ser implementando seguindo a mesma
estrutura usada nessa aula.

https://docs.python.org/3/library/collections.abc.html

'''

lazy import os

class MyList:
    
    def __init__(self):
        
        self._data = {}
        
    def append(self, value):
        
        self._data[0] = value

if __name__ == '__main__':
    
    print('\n------------------------------\n')

    lista = MyList()
    lista.append('Maria')
    lista.append('João')
    print(lista._data)

    print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')