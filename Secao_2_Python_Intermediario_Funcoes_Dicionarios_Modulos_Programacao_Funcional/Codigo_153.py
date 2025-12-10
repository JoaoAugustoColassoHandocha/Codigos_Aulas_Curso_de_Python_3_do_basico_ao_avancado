'''


'''

import os, json


def listar(tarefas):
    
    if not tarefas:
        
        print('\nNenhuma tarefa para listar\n')
        return
    
    print('\nTarefas:\n')
    
    for tarefa in tarefas:
        
        print(f'\t{tarefa}')
        
    print('\n')
    
def desfazer(tarefas, tarefas_refazer):
    
    if not tarefas:
        
        print('\nNenhuma tarefa para desfazer\n')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    
    print(f'\nTarefa "{tarefa}" desfeita\n')
    
def refazer(tarefas, tarefas_refazer):
    
    if not tarefas_refazer:
        
        print('\nNenhuma tarefa para refazer\n')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    
    print(f'\nTarefa "{tarefa}" refeita\n')
    
def adicionar(tarefa, tarefas):
    
    tarefa = tarefa.strip()
    
    if not tarefa:
        
        print('\nVocê não digitou uma tarefa.\n')
        return
    
    tarefas.append(tarefa)
    
    print(f'\nTarefa "{tarefa}" adicionada\n')
    
def ler(caminho_arquivo):
    
    dados = []
    
    try:
    
        with open(caminho_arquivo, 'r+', encoding = 'utf-8') as arquivo:
            
            dados = json.load(arquivo)
            
    except Exception as e:
            
            print(f'\n[AVISO] Arquivo não encontrado\n{e}\n')
            input('Clique em qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')            
            
    return dados
    
def salvar(tarefas, caminho_arquivo):
    
    with open(caminho_arquivo, 'r+', encoding = 'utf-8') as arquivo:
            
        dados = json.load(arquivo)

CAMINHO_ARQUIVO = 'Codigo_153.json'

tarefas = ler(CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\nComandos: listar, desfazer e refazer')
    tarefa = input('\nDigite uma tarefa ou comando: ')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    comandos = {
                
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls' if os.name == 'nt' else 'clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
        
    }
    
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    
    comando()
    input('Clique em qualquer tecla para continuar...')