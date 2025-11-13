'''
Problema dos parâmetros mutáveis em funções Python

'''

import os

os.system('color 1f')

# Utiliza a mesma lista

def adiciona_clientes(nome, lista = []):
    
    lista.append(nome)
    return lista

while True:

    clientes = adiciona_clientes(input('\nNome: '))

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

os.system('pause')
os.system('cls')