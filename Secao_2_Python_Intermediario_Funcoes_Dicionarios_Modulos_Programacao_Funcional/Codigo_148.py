'''
Problema dos parâmetros mutáveis em funções Python

'''

import os

os.system('color 1f')

# Utiliza a mesma lista
def adiciona_clientes_1(nome, lista = []):
    
    lista.append(nome)
    return lista

while True:

    clientes = adiciona_clientes_1(input('\nNome: '))

    parar_execução = input('\nGostaria de inserir mais um nome? (S - Sim | N - Não): ')

    os.system('cls')

    if parar_execução == 'N':
        
        print('\n******************************\n')

        for nomes in clientes:
                    
            print(nomes)

        print('\n******************************\n')

        os.system('pause')
        os.system('cls')
        
        break
    
    elif parar_execução == 'S':
        
        True
        
    else:
        
        print('\nErro no Sistema!!!\n')
        os.system('pause')
        os.system('cls')
        break
    
#####################################
    
# Cria uma nova lista
def adiciona_clientes_1(nome, lista = None):

    if lista is None:
        
        lista = []
    
    lista.append(nome)
    return lista

os.system('pause')
os.system('cls')