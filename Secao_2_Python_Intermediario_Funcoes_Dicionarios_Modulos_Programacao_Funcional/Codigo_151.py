'''


'''

import os

tarefas = []
tarefas_refazer = []

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
    input()

while True:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\nComandos: listar desfazer e refazer')
    tarefa = input('\nDigite uma tarefa ou comando: ')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    comandos = {
                
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': refazer(tarefas, tarefas_refazer),
        'clear': os.system('cls' if os.name == 'nt' else 'clear'),
        'adicionar': adicionar(tarefa, tarefas),
        
    }
    
    comando = comandos.get(tarefa)()