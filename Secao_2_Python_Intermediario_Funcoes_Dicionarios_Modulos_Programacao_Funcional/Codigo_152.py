'''
Exercício - salvando a lista de tarefas em JSON

'''

import os, json, sys

task_add = []
time_add = []
lista_tarefas_adicionadas = []
lista_tarefas_adicionadas_dict = dict(lista_tarefas_adicionadas)

lista_tarefas_refazer = []

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'Codigo_152_lista_tarefas.json')
JSON_FILE = os.path.join(BASE_DIR, 'Codigo_152_lista_tarefas.json')

def menu(op = 0):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
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
    
    os.system('cls' if os.name == 'nt' else 'clear')

    if op == '1':

        task = input('\nDigite a tarefa a ser adicionada: ')
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        time = input('\nDigite a hora da tarefa: ')
        
        if task == '' or task == ' ' or time == '' or time == ' ':
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nFavor inserir uma tarefa a ser adicionada!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)
            
        task_add.append(task)
        time_add.append(time)
            
        with open(SAVE_TO, 'a+', encoding = 'utf-8') as tarefas_add:
                
            json.dump(lista_tarefas_adicionadas_dict, tarefas_add, ensure_ascii = False, indent = 2)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)

    elif op == '2':
                
        with open(JSON_FILE, 'r+', encoding = 'utf-8') as tarefas_lista:
            
                lista_tarefas = json.load(tarefas_lista)
        
        if lista_tarefas == []:
            
            print('\nNão há tarefas a realizar!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)
            
        print('\nSua lista de tarefas: ')

        print('\n' + '*' * 25 + '\n')
            
        for lista in lista_tarefas:
                
            print(lista)

        print('\n' + '*' * 25 + '\n')
        
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)
        
    elif op == '3':
        
        if lista_tarefas_refazer == []:
            
            print('\nNão há tarefas excluídas!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)

        print('\nSua lista de tarefas excluídas:')

        print('\n' + '*' * 25 + '\n')

        with open('Codigo_152_lixeira.json', 'r+', encoding = 'utf-8') as tarefas_lixeira:
            
            lista_lixeira = json.load(tarefas_lixeira)
            
            for lixeira in lista_lixeira:
                
                print(lixeira)
    
        print('\n' + '*' * 25 + '\n')

        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
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

        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('\nSua lista de tarefas excluídas: ')

        print('\n' + '*' * 25 + '\n')

        for list_redo in lista_tarefas_refazer:

            print(f'{id_redo} - {list_redo}')
            id_redo += 1
    
        print('\n' + '*' * 25 + '\n')

        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')        
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

        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('\nSua lista de tarefas: ')

        print('\n' + '*' * 25 + '\n')
        
        for list_print in lista_tarefas_adicionadas:

            print(f'{id_list} - {list_print}')
            id_list += 1

        print('\n' + '*' * 25 + '\n')
        
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)

    elif op == '6':

        print('\nSaindo...\n')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

    elif op != '1' or op != '2' or op != '3' or op != '4' or op != '5' or op != '6':

        print('\nOpção inválida, digite novamente\n')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)
    
    else:

        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')

menu(op = 0)