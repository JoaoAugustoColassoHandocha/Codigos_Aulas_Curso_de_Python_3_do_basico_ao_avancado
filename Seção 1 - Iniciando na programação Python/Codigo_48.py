'''
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis:

    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas

CRUD:

Create | Read | Update  | Delete
Criar  | Ler  | Alterar | Apagar

lista[i] (CRUD)

lista.insert(índice, item)

'''

import os

os.system('color 1f')

# Repassando as listas A e B, concatenando em uma lista C.
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print('\n' + '=' * 30 + '\n')
print(f'{lista_c}\n')
print('=' * 30 + '\n')

# Concatenando as listas A e B na própria lista A.
lista_a.extend(lista_b)
print(f'{lista_a}\n')
print('=' * 30 + '\n')

os.system('pause')
os.system('cls')