'''
Closure e funções  que retornam outras funções

'''

import os

os.system('color 1f')

def criar_saudacao(saudacao):

    def saudar(nome):
        
        return f'{saudacao}, {nome}!'
    
    return saudar



os.system('pause')
os.system('cls')