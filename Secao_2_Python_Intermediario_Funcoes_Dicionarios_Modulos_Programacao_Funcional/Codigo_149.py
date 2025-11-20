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
    
    id_redo = 1
    id_list = 1

    print('\n' + '*' * 10 + 'Menu' + '*' * 10 + '\n')
    print('1 - Incluir Tarefa')
    print('2 - Lista de Tarefas')
    print('3 - Lixeira')
    print('4 - Desfazer Tarefa')
    print('5 - Refazer Tarefa')
    print('6 - Sair')
    print('\n' + '*' * 24 + '\n')

    op = input('Digite o número da opção desejada: ')
    
    os.system('cls')

    if op == '1':

        task = input('\nDigite a tarefa a ser adicionada: ')
        lista_tarefas_adicionadas.append(task)
        os.system('cls')
        menu(op = 0)

    elif op == '2':

        print('\nSua lista de tarefas: ')

        print('\n' + '*' * 25 + '\n')

        for item_list_print in lista_tarefas_adicionadas:

            print(f'{id_list} - {item_list_print}')
            id_list += 1

        print('\n' + '*' * 25 + '\n')
        
        os.system('pause')
        os.system('cls')
        menu(op = 0)
        

    elif op == '3':

        print('\nSua lista de tarefas excluídas: ')

        print('\n' + '*' * 25 + '\n')

        for item_list_redo_ex in lista_tarefas_refazer:

            print(f'{id_redo} - {item_list_redo_ex}')
            id_redo += 1
    
        print('\n' + '*' * 25 + '\n')

        os.system('pause')
        os.system('cls')
        menu(op = 0)
        
    elif op == '4':
        
        print('\nSua lista de tarefas: ')

        print('\n' + '*' * 25 + '\n')

        for item_list_delete in lista_tarefas_adicionadas:

            print(f'{id_list} - {item_list_delete}')
            id_list += 1

        print('\n' + '*' * 25 + '\n')

        task_to_be_removed = input('Digite a tarefa a ser removida: ')
        lista_tarefas_adicionadas.remove(task_to_be_removed)
        lista_tarefas_refazer.append(task_to_be_removed)

        os.system('cls')
        
        print('\nSua lista de tarefas excluídas: ')

        print('\n' + '*' * 25 + '\n')

        for list_redo in lista_tarefas_refazer:

            print(f'{id_redo} - {list_redo}')
            id_redo += 1
    
        print('\n' + '*' * 25 + '\n')

        os.system('pause')
        os.system('cls')        
        menu(op = 0)

    elif op == '5':

        print('\nSua lista de tarefas excluídas: ')

        print('\n' + '*' * 25 + '\n')

        for item_list_redo in lista_tarefas_refazer:

            print(f'{id_redo} - {item_list_redo}')
            id_redo += 1
    
        print('\n' + '*' * 25 + '\n')

        task_to_redo = input('Digite a tarefa a ser refeita: ')
        lista_tarefas_refazer.remove(task_to_redo)
        lista_tarefas_adicionadas.append(task_to_redo)

        os.system('cls')
        
        print('\nSua lista de tarefas: ')

        print('\n' + '*' * 25 + '\n')
        
        for list_print in lista_tarefas_adicionadas:

            print(f'{id_list} - {list_print}')
            id_list += 1

        print('\n' + '*' * 25 + '\n')
        
        os.system('pause')
        os.system('cls')
        menu(op = 0)

    elif op == '6':

        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')

    elif op == '' or op == ' ' or op != '1' or op != '2' or op != '3' or op != '4':

        print('\nOpção inválida, digite novamente\n')
        os.system('pause')
        os.system('cls')
        menu(op = 0)
    
    else:

        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        os.system('pause')
        os.system('cls')

menu(op = 0)