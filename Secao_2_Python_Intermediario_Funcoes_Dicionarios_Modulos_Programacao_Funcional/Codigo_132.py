'''
Groupby - agrupando valores (itertools)

'''

import os
from itertools import groupby

os.system('color 1f')

alunos = [
    
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    
]

def print_iter(iterator):
    
    for chave, grupo in iterator:
          
        print(f'| {chave} |')
        
        for aluno in grupo: 
            
            print(f'| {aluno} |')
            print('\n')
        
alunos_agrupados = sorted(alunos, key = lambda a: a['nota'])
grupos = groupby(alunos_agrupados, key = lambda a: a['nota'])

print('\n******************************\n')

print_iter(grupos)

print('\n******************************\n')

os.system('pause')
os.system('cls')