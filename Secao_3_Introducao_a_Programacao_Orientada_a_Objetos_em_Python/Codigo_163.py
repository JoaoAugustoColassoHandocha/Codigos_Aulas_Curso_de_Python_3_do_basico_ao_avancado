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
    print('3 - Sair')
    print('\n' + '*' * 24 + '\n')

    op = int(input('Digite o número da opção desejada: '))
    
    os.system('cls' if os.name == 'nt' else 'clear')

    match op:
        
        case 1:
        
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
                
            if sol_genero != 'M' or sol_genero != 'm' or sol_genero != 'F' or sol_genero != 'f':
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n[AVISO] Favor inserir o dados válidos no campo "Gênero", com informações "M" (Masculino) ou "F" (Feminino).\n')
                input('Clique qualquer tecla para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
                menu(op = 0)
            
            match sol_genero:    
                
                case 'M' | 'm':
                    
                    sol_genero = 'Masculino'
                
                case 'F' | 'f':
                    
                    sol_genero = 'Feminino'
                
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

        case 2:
        
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

        case 3:

            print('\nSaindo...\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

    if op != '1' or op != '2' or op != '3':

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