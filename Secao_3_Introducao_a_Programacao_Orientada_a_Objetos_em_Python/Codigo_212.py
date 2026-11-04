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
lazy from collections.abc import Iterable, Iterator, Sequence

class MyList(Sequence):
    
    def __init__(self):
        
        self._data = {}
        self._index = 0
        self._next_index = 0
        
    def append(self, value):
        
        self._data[self._index] = value
        self._index += 1
    
    # Método Iterable e Iterator
    # def __iter__(self): ...
    
    # Método Iterator
    # def __next__(self): ...
    
    # Método Sequence
    def __getitem__(self, index):
        
        print(f'getitem: {index}')
        
        return self._data[index]
    
    # Método Sequence
    def __len__(self) -> int:
        
        return self._index
    
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        return

if __name__ == '__main__':
    
    print('\n------------------------------\n')

    lista = MyList()
    lista.append('Maria')
    lista.append('João')
    print(lista._data)
    print(lista[0])
    print(len(lista))

    print('\n------------------------------\n')
    
    for item in lista:
        
        print(item)
    
    print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')