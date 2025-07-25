'''
EXERCÍCIO

Crie uma função que encontra o primeiro duplicado considerando o segundo número como a duplicação.

Retorne a duplicação considerada.

Requisitos:

    A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja, o número duplicado em si.
    
    Exemplo:
    
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    
    Se não encontrar duplicados na lista, retorne -1

'''

import os

os.system('color 1f')

lista_de_listas_de_inteiros = [
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # S1
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8], # S2
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7], # S3
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9], # S4
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7], # S5
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9], # S6
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1], # S7
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3], # S8
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7], # S9
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1], # S10
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7], # S11
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], #S12
    
]

def prim_dupla(listas):
    
    print('\n')
    
    if listas == list(set(listas)):
        
        print('-1')
    
    lista_elemento_unico = []
    
    for elemento in listas:
        
        verificar = elemento in lista_elemento_unico
        
        if verificar:
            
            print(f'{elemento}')
            
        else:
            
            lista_elemento_unico.append(elemento)

for listas in lista_de_listas_de_inteiros:
    
    prim_dupla(listas)

os.system('pause')
os.system('cls')