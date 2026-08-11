'''
Exercício:

Salve os dados da sua classe em JSON, e depois crie novamente as instâncias da classe com os dados salvos.

Faça em arquivos separados.

'''

import os, json, sys

BASE_DIR = os.path.dirname(__file__)
JSON_ADD_DADOS = os.path.join(BASE_DIR, 'Codigo_163_lista_dados.json')
JSON_FILE_DADOS = os.path.join(BASE_DIR, 'Codigo_163_lista_dados.json')
JSON_FILE_LIXEIRA = os.path.join(BASE_DIR, 'Codigo_163_lixeira_dados.json')


def carregar_dados(caminho_arquivo):
    
    if not os.path.exists(caminho_arquivo) or os.stat(caminho_arquivo).st_size == 0:
        
        return []
    
    try:
        
        with open(caminho_arquivo, 'r+', encoding='utf-8') as f:
            
            return json.load(f)
        
    except json.JSONDecodeError:
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'\n[AVISO] O arquivo {caminho_arquivo} está corrompido. Iniciando nova lista.\n')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        
        return []

def mover_dados(dados_mover, arquivo_origem, arquivo_destino):
    
    with open(arquivo_origem, 'r+', encoding='utf-8') as f_origem:
        
        dados_origem = json.load(f_origem)

    conteudo_movido = None

    novos_dados_origem = []
    
    for item in dados_origem:
    
        if item == dados_mover:
            
            conteudo_movido = item
        
        else:
        
            novos_dados_origem.append(item)

    if conteudo_movido is None:

        print(f"\nO dado {dados_mover} não encontrado.\n")
        
        return

    if os.path.exists(arquivo_destino) and os.path.getsize(arquivo_destino) > 0:
        
        with open(arquivo_destino, 'r+', encoding='utf-8') as f_destino:
        
            dados_destino = json.load(f_destino)
        
            if isinstance(dados_destino, list):
                
                dados_destino.append(conteudo_movido)
        
            else:
        
                print("\n[AVISO] Arquivo de destino não é uma lista, sobrescrevendo como nova lista.\n")
                
                dados_destino = [conteudo_movido]
                
    else:
        
        dados_destino = [conteudo_movido]

    with open(arquivo_destino, 'w+', encoding='utf-8') as f_destino:
        
        json.dump(dados_destino, f_destino, indent = 2, ensure_ascii = False)
    
    with open(arquivo_origem, 'w+', encoding='utf-8') as f_origem:
    
        json.dump(novos_dados_origem, f_origem, indent = 2, ensure_ascii = False)

    print(f"\nO dado {dados_mover} movido com sucesso.\n")
    
def contar_ids(dados_id):
    
    total_id = 0
    
    if isinstance(dados_id, dict):
        
        for chave_id, valor_id in dados_id.items():
            
            if chave_id == 'id':
                
                total_id += 1
                
            total_id += contar_ids(valor_id)
            
    elif isinstance(dados_id, list):
        
        for item in dados_id:
            
            total_id += contar_ids(item)
            
    return total_id

def menu(op = 0):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    global lista_dados_atual
    lista_dados_atual = carregar_dados(JSON_ADD_DADOS)
    
    print('\n' + '*' * 9 + '|MENU|' + '*' * 9 + '\n')
    print('1 - Incluir Dados')
    print('2 - Lista de Dados')
    print('3 - Lixeira')
    print('4 - Desfazer Dados')
    print('5 - Refazer Dados')
    print('6 - Sair')
    print('\n' + '*' * 24 + '\n')

    op = input('Digite o número da opção desejada: ')
    
    os.system('cls' if os.name == 'nt' else 'clear')

    if op == '1':
        
        dados = []
        novos_dados = []

        id_dados = contar_ids(lista_dados_atual)
        
        class Pessoa:
            
            def __init__(self, id, nome, idade, genero):
                
                self.id = id
                self.nome = nome
                self.idade = idade
                self.genero = genero
                
        sol_id = (id_dados + 1)
        sol_nome = input('\nNome: ')
        sol_idade = int(input('\nIdade (Somente Números = 00): '))
        sol_genero = input('\nGênero (M/F): ')
        
        if sol_nome == '' or sol_nome == ' ' or sol_idade == '' or sol_idade == ' ' or sol_genero == '' or sol_genero == ' ':
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n[AVISO] Favor inserir o dados válidos!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)
            
        dados = Pessoa(sol_id, sol_nome, sol_idade, sol_genero)
        
        novos_dados = [dados.__dict__]
        lista_dados_atual.extend(novos_dados)
        
        try:
            
            with open(JSON_ADD_DADOS, 'w+', encoding='utf-8') as dados_add:
                
                json.dump(lista_dados_atual, dados_add, ensure_ascii=False, indent=2)
        
        except Exception as e:
            
            os.system('cls' if os.name == 'nt' else 'clear')
    
            print(f'\n[AVISO] Não foi possível salvar o arquivo JSON: {e}\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)
            
        os.system('cls' if os.name == 'nt' else 'clear')
            
        print(f'\nOs dados "ID: {dados.__dict__['id']} - Nome: {dados.__dict__['nome']} - Idade: {dados.__dict__['idade']} - Gênero: {dados.__dict__['genero']}" adicionados com sucesso!\n')
        
        input('Clique qualquer tecla para continuar...')       
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)

    elif op == '2':
        
        try:
                
            with open(JSON_FILE_DADOS, 'r+', encoding = 'utf-8') as dados_lista:
                
                    lista_dados = json.load(dados_lista)
                    
            if lista_dados == []:
                
                os.system('cls' if os.name == 'nt' else 'clear')
        
                print('\n[AVISO] Não há dados cadastrados!\n')
                input('Clique qualquer tecla para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                menu(op = 0)
                
    
            print('\n' + '*' * 10 + '|Dados|' + '*' * 10 + '\n')
                
            for lista in lista_dados:
                        
                print(f'ID: {lista['id']}\nNome: {lista['nome']}\nIdade: {lista['idade']}\nGênero: {lista['genero']}\n')

            print('*' * 29 + '\n')
            
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            
        except Exception as e:
            
            os.system('cls' if os.name == 'nt' else 'clear')
    
            print('\n[AVISO] Não há dados cadastrados!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
        
        menu(op = 0)
        
    elif op == '3':
        
        try:
            
            with open(JSON_FILE_LIXEIRA, 'r+', encoding = 'utf-8') as excluidos_lista:
                
                lista_excluidos = json.load(excluidos_lista)
                
            if lista_excluidos == []:
                
                os.system('cls' if os.name == 'nt' else 'clear')
        
                print('\n[AVISO] Não há dados excluídos!\n')
                input('Clique qualquer tecla para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                menu(op = 0)
                
    
            print('\n' + '*' * 10 + '|Dados Excluídos|' + '*' * 10 + '\n')
            
            for lista in lista_excluidos:
                                    
                print(f'ID: {lista['id']}\nNome: {lista['nome']}\nIdade: {lista['idade']}\nGênero: {lista['genero']}\n')
    
            print('\n' + '*' * 39 + '\n')

            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            
        except Exception as e:
            
            os.system('cls' if os.name == 'nt' else 'clear')
    
            print('\n[AVISO] Não há dados excluídos!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
        
        menu(op = 0)
        
    elif op == '4':

        dados_to_be_removed = input('\nDigite o ID dos dados a ser removido: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        
        if dados_to_be_removed == '' or dados_to_be_removed == ' ':
            
            os.system('cls' if os.name == 'nt' else 'clear')
    
            print('\n[AVISO] Favor inserir um ID válido!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)

        mover_dados(dados_to_be_removed, JSON_FILE_DADOS, JSON_FILE_LIXEIRA)
        
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')       
        menu(op = 0)

    elif op == '5':

        task_to_redo = input('\nDigite a tarefa a ser refeita: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        
        if task_to_redo == '' or task_to_redo == ' ':
            
            os.system('cls' if os.name == 'nt' else 'clear')
    
            print('\n[AVISO] Favor inserir uma tarefa válida!\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            menu(op = 0)

        mover_dados(task_to_redo, JSON_FILE_LIXEIRA, JSON_FILE_DADOS)
        
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')        
        menu(op = 0)

    elif op == '6':

        print('\nSaindo...\n')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

    elif op != '1' or op != '2' or op != '3' or op != '4' or op != '5' or op != '6':

        print('\n[AVISO] Opção inválida, digite novamente\n')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)
    
    else:

        print('\n[AVISO] Favor entrar em contato com o suporte!\n')
        input('Clique qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        menu(op = 0)

menu(op = 0)