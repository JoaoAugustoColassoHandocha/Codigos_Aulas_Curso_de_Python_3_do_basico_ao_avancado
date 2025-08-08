'''
DIR, HASATTR, e GETATTR em Pyhton

* dir: É usada para listar os atributos (como métodos, variáveis, etc.) de um objeto (Por exemplo, dentro da string).
* hasattr: É usada para verificar se um objeto possui um determinado atributo.
* getattr:

'''

import os

os.system('color 1f')

string = 'João'

print('\n##############################\n')

print(string) # João

print('\n##############################\n')

# dir

print(dir(string)) # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print('\n##############################\n')

# hasattr

if hasattr(string, 'upper'):
    
    print(f'Existe upper: {string.upper()}') # Existe upper: JOÃO

print('\n##############################\n')

os.system('pause')
os.system('cls')