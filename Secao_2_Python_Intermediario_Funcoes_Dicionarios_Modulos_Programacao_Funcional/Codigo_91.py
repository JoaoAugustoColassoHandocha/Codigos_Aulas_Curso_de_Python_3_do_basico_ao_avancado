'''
SOLUÇÂO

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

def encontra_primeiro_duplicado(lista_de_inteiros):
    
    numero_checados = set()
    primeiro_duplicado = -1
    
    for numero in lista_de_inteiros:
        
        if numero in numero_checados:
            
            primeiro_duplicado = numero
            
            break
        
        numero_checados.add(numero)
        
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    
    encontra_primeiro_duplicado(lista)

os.system('pause')
os.system('cls')