'''
Exercício - Salvando a lista de tarefas em JSON

'''

import os, json, sys

lista_tarefas_refazer = []

BASE_DIR = os.path.dirname(__file__)
JSON_ADD_TAREFAS = os.path.join(BASE_DIR, 'Codigo_152_lista_tarefas.json')
JSON_FILE_TASK = os.path.join(BASE_DIR, 'Codigo_152_lista_tarefas.json')
JSON_FILE_LIXEIRA = os.path.join(BASE_DIR, 'Codigo_152_lixeira_tarefas.json')

def carregar_tarefas(caminho_arquivo):
    
    if not os.path.exists(caminho_arquivo) or os.stat(caminho_arquivo).st_size == 0:
        
        return []
    
    try:
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            
            return json.load(f)
        
    except json.JSONDecodeError:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n[AVISO] O arquivo {caminho_arquivo} está corrompido. Iniciando nova lista.\n')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        
        return []

def mover_tarefa_para_lixeira(tarefa_exluida, arquivo_origem, arquivo_destino):
    
    with open(arquivo_origem, 'r+', encoding='utf-8') as f_origem:
        
        dados_origem = json.load(f_origem)

    conteudo_movido = None

    novos_dados_origem = []
    
    for item in dados_origem:
    
        if item == tarefa_exluida:
            
            conteudo_movido = item
        
        else:
        
            novos_dados_origem.append(item)

    if conteudo_movido is None:
        
        print(f"\nA tarefa {tarefa_exluida} não encontrado.\n")
        
        return

    if os.path.exists(arquivo_destino) and os.path.getsize(arquivo_destino) > 0:
        
        with open(arquivo_destino, 'r+', encoding='utf-8') as f_destino:
        
            dados_destino = json.load(f_destino)
        
            if isinstance(dados_destino, list):
                
                dados_destino.append(conteudo_movido)
        
            else:
                
                print("\nArquivo de destino não é uma lista, sobrescrevendo como nova lista.\n")
                
                dados_destino = [conteudo_movido]
    else:
        
        dados_destino = [conteudo_movido]

    with open(arquivo_destino, 'w+', encoding='utf-8') as f_destino:
        
        json.dump(dados_destino, f_destino, indent = 2, ensure_ascii = False)
    
    with open(arquivo_origem, 'w', encoding='utf-8') as f_origem:
    
        json.dump(novos_dados_origem, f_origem, indent = 2, ensure_ascii = False)

    print(f"\nA tarefa {tarefa_exluida} excluída com sucesso.\n")

def menu(op = 0):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    global lista_tarefas_atual
    lista_tarefas_atual = carregar_tarefas(JSON_ADD_TAREFAS)
    
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
        
        task = []
        nova_tarefa = []

        task = input('\nDigite a tarefa a ser adicionada: ')
        
        if task == '' or task == ' ':
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nFavor inserir uma tarefa válidas!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)
        
        nova_tarefa = [task]
        lista_tarefas_atual.extend(nova_tarefa)
        
        try:
            
            with open(JSON_ADD_TAREFAS, 'w', encoding='utf-8') as tarefas_add:
                
                json.dump(lista_tarefas_atual, tarefas_add, ensure_ascii=False, indent=2)
        
        except Exception as e:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'\n[ERRO] Não foi possível salvar o arquivo JSON: {e}\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)
            
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f'\nTarefa "{task}" adicionada com sucesso!\n')
        
        input('Clique qualquer tecla para continuar...')       
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)

    elif op == '2':
        
        try:
                
            with open(JSON_FILE_TASK, 'r+', encoding = 'utf-8') as tarefa_lista:
                
                    lista_tarefa = json.load(tarefa_lista)
                    
            if lista_tarefa == []:
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\nNão há tarefas a realizar!\n')
                input('Clique qualquer tecla para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                menu(op = 0)

            print('\n' + '*' * 10 + '|Tarefas|' + '*' * 10 + '\n')
                
            for lista in lista_tarefa:
                    
                print(lista)

            print('\n' + '*' * 29 + '\n')
            
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            
        except Exception as e:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nNão há tarefas a realizar!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
        
        menu(op = 0)
        
    elif op == '3':
        
        try:
            
            with open(JSON_FILE_LIXEIRA, 'r+', encoding = 'utf-8') as excluidos_lista:
                
                lista_excluidos = json.load(excluidos_lista)
                
            if lista_excluidos == []:
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\nNão há tarefas excluídas!\n')
                input('Clique qualquer tecla para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                menu(op = 0)

            print('\n' + '*' * 10 + '|Tarefas Excluídas|' + '*' * 10 + '\n')
            
            for lixeira in lista_excluidos:
                
                print(lixeira)
    
            print('\n' + '*' * 39 + '\n')

            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            
        except Exception as e:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nNão há tarefas excluídas!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
        
        menu(op = 0)
        
    elif op == '4':

        task_to_be_removed = input('Digite a tarefa a ser removida: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        
        if task_to_be_removed == '' or task_to_be_removed == ' ':
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nFavor inserir uma tarefa válida!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)

        mover_tarefa_para_lixeira(task_to_be_removed, JSON_FILE_TASK, JSON_FILE_LIXEIRA)
        
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