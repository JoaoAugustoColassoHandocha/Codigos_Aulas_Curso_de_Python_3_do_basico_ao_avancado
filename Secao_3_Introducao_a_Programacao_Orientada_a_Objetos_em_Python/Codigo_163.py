'''
Exercício:

Salve os dados da sua classe em JSON, e depois crie novamente as instâncias da classe com os dados salvos.

Faça em arquivos separados.

'''

import os, json, sys

ASE_DIR = os.path.dirname(__file__)
JSON_ADD_TAREFAS = os.path.join(BASE_DIR, 'Codigo_163_lista_tarefas.json')
JSON_FILE_TASK = os.path.join(BASE_DIR, 'Codigo_163_lista_tarefas.json')
JSON_FILE_LIXEIRA = os.path.join(BASE_DIR, 'Codigo_163_lixeira_tarefas.json')


def carregar_tarefas(caminho_arquivo):
    
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

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')