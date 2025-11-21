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

while True:
    
    os.system('cls')
    
    print('\nComandos: listar desfazer e refazer')
    tarefa = input('\nDigite uma tarefa ou comando: ')
    
    os.system('cls')
    
    if tarefa == 'listar':
        
        listar(tarefas)
        os.system('pause')       
        continue
    
    elif tarefa == 'desfazer':
        
        desfazer(tarefas, tarefas_refazer)
        os.system('pause')
        continue    
    
    elif tarefa == 'refazer':
        
        refazer(tarefas, tarefas_refazer)
        os.system('pause')
        continue
    
    else:
        
        adicionar(tarefa, tarefas)
        continue