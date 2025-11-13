'''
Problema dos parâmetros mutáveis em funções Python

'''

import os

os.system('color 1f')

escolha = input('\n1 - Mesma lista | 2 - Multiplas listas: ')

os.system('cls')

if escolha == '1':

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

elif escolha == '2':
   
    # Cria uma nova lista
    def adiciona_clientes_2(nome, lista = None):

        if lista is None:
            
            lista = []
        
        lista.append(nome)
        return lista

    clientes_sp = adiciona_clientes_2(None)
    clientes_sp.append('João')
    clientes_sp.append('Maria')
    clientes_sp.append('José')

    clientes_rj = adiciona_clientes_2(None)
    clientes_rj.append('João')
    clientes_rj.append('Maria')
    clientes_rj.append('José')

    clientes_pr = adiciona_clientes_2(None)
    clientes_pr.append('João')
    clientes_pr.append('Maria')
    clientes_pr.append('José')


    print('\n******************************\n')

    print('Clientes de São Paulo:')

    for sp in clientes_sp:
        
        print(sp)
        
    print('\nClientes do Rio de Janeiro:')

    for rj in clientes_rj:
        
        print(rj)
        
    print('\nClientes do Paraná:')

    for pr in clientes_pr:
        
        print(pr)

    print('\n******************************\n')

    os.system('pause')
    os.system('cls')
    
else:
    
    print('\nErro no Sistema!!!\n')
    os.system('pause')
    os.system('cls')