'''
Exercício - salvando a lista de tarefas em JSON

'''

import os, json, sys

task_add = []
time_add = []

lista_tarefas_refazer = []

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'Codigo_152_lista_tarefas.json')
JSON_FILE_TASK = os.path.join(BASE_DIR, 'Codigo_152_lista_tarefas.json')

def carregar_tarefas(caminho_arquivo):
    
    if not os.path.exists(caminho_arquivo) or os.stat(caminho_arquivo).st_size == 0:
        
        return []
    
    try:
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            
            return json.load(f)
        
    except json.JSONDecodeError:
        
        print(f'\n[AVISO] O arquivo {caminho_arquivo} está corrompido. Iniciando nova lista.')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        
        return []
    
lista_tarefas_atual = carregar_tarefas(SAVE_TO)

def menu(op = 0):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    id_redo = 1
    id_list = 1
    
    print('\n' + '*' * 9 + '|' + 'MENU' + '|' + '*' * 9 + '\n')
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
        
        if task == '' or task == ' ':
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nFavor inserir uma tarefa e hora válidas!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)
        
        nova_tarefa = [task]
        lista_tarefas_atual.extend(nova_tarefa)
        
        try:
            
            with open(SAVE_TO, 'w', encoding='utf-8') as tarefas_add:
                
                json.dump(lista_tarefas_atual, tarefas_add, ensure_ascii=False, indent=2)
        
        except Exception as e:
            
            print(f'\n[ERRO] Não foi possível salvar o arquivo JSON: {e}\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)
            
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f'\nTarefa "{task}" adicionada com sucesso!')
        
        input('Clique qualquer tecla para continuar...')       
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)

    elif op == '2':
        
        try:
                
            with open(JSON_FILE_TASK, 'r+', encoding = 'utf-8') as tarefa_lista:
                
                    lista_tarefa = json.load(tarefa_lista)

            print('\n' + '*' * 10 + '|Lista de Tarefas|' + '*' * 10 + '\n')
                
            for lista in lista_tarefa:
                    
                print(lista)

            print('\n' + '*' * 38 + '\n')
            
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            
        except Exception as e:
            
            print('\nNão há tarefas a realizar!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
        
        menu(op = 0)
        
    elif op == '3':
        
        try:
            
            with open(JSON_FILE_TASK, 'r+', encoding = 'utf-8') as excluidos_lista:
                
                lista_excluidos = json.load(excluidos_lista)
        
            if lista_tarefas_refazer == []:
                
                print('\nNão há tarefas excluídas!\n')
                input('Clique qualquer tecla para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                menu(op = 0)

            print('\nSua lista de tarefas excluídas:')

            print('\n' + '*' * 25 + '\n')
            
            for lixeira in lista_excluidos:
                
                print(lixeira)
    
            print('\n' + '*' * 25 + '\n')

            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            
        except Exception as e:
            
            print('\nNão há tarefas a realizar!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
        
        menu(op = 0)
        
    elif op == '4':
        
        print('\nSua lista de tarefas: ')

        print('\n' + '*' * 25 + '\n')

        for item_list_delete in lista_tarefas_atual:

            print(f'{id_list} - {item_list_delete}')
            id_list += 1

        print('\n' + '*' * 25 + '\n')

        task_to_be_removed = input('Digite a tarefa a ser removida: ')
        lista_tarefas_atual.remove(task_to_be_removed)
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
        lista_tarefas_atual.append(task_to_redo)

        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('\nSua lista de tarefas: ')

        print('\n' + '*' * 25 + '\n')
        
        for list_print in lista_tarefas_atual:

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