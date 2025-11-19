'''
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

'''

import os

os.system('color 1f')

lista_tarefas_adicionadas = []
lista_tarefas_refazer = []

def menu(op = 0): 

    print('\n' + '*' * 10 + 'Menu' + '*' * 10 + '\n')
    print('1 - Incluir Tarefa')
    print('2 - Listar Tarefa')
    print('3 - Desfazer Tarefa')
    print('4 - Refazer Tarefa')
    print('5 - Sair')
    print('\n' + '*' * 24 + '\n')
    
    op = input('Digite o número da opção desejada: ')
    
menu(op = 0)

os.system('pause')
os.system('cls')