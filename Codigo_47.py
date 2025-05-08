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

'''

import os

os.system('color 1f')

lista = [10, 20, 30, 40] # Lista
print('=' * 30 + '\n')

# Adicionando um item na lista, onde esse adicionamento é posicionado no final da mesma, e imprimindo a lista modificada na tela.
print(f'{lista.append(50)}\n')
print('=' * 30 + '\n')

# Removendo o último item da lista e imprimindo na tela a lista modificada.
print(f'{lista.pop()}\n')
print('=' * 30 + '\n')

# Adicionando novamente um item na lista, removendo esse item de uma forma diferente, e imprimindo a lista modificada na tela.
print(f'{lista.append(50)}\n')
print('=' * 30 + '\n')
del lista[-1]
print(f'{lista}\n')
print('=' * 30 + '\n')

# Limpando a lista completa e exibindo a mesma vazia
print(f'{lista.clear()}\n')
print('=' * 30 + '\n')

os.system('pause')
os.system('cls')