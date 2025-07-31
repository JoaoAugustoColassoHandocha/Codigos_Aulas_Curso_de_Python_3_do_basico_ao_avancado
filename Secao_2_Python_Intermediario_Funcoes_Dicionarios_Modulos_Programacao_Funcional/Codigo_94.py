'''
Empacotamento e desempacotamento de dicionários

'''

import os

os.system('color 1f')

a, b = 1, 2
a, b = b, a

print(f'\n{a, b}\n')

################################

pessoa = {
    
    'nome': 'Aline',
    'sobrenome': 'Souza',
    
}

# Retorna o nome das chaves (nome sobrenome)
a, b = pessoa
print(f'{a, b}\n')

# Retorna os valores das chaves (Aline Souza)
a, b = pessoa.values()
print(f'{a, b}\n')

# Retorna as chaves e valores em tupla (('nome', 'Aline') ('sobrenome', 'Souza'))
a, b = pessoa.items()
print(f'{a, b}\n')

# Retorna desempacotado a chave e o valor (nome Aline)(sobrenome Souza)
(a1, a2), (b1, b2) = pessoa.items()
print(f'{a1, a2}')
print(f'{b1, b2}\n')

dados_pessoa = {
    
    'idade': 16,
    'altura': 1.75,
    
}

os.system('pause')
os.system('exit')