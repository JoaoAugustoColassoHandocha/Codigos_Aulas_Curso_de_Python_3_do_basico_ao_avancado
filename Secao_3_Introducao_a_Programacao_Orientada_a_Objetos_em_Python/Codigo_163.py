'''
Exercício:

Salve os dados da sua classe em JSON, e depois crie novamente as instâncias da classe com os dados salvos.

Faça em arquivos separados.

'''

import os, json, sys

ASE_DIR = os.path.dirname(__file__)
JSON_ADD_TAREFAS = os.path.join(BASE_DIR, 'Codigo_152_lista_tarefas.json')
JSON_FILE_TASK = os.path.join(BASE_DIR, 'Codigo_152_lista_tarefas.json')
JSON_FILE_LIXEIRA = os.path.join(BASE_DIR, 'Codigo_152_lixeira_tarefas.json')


print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')