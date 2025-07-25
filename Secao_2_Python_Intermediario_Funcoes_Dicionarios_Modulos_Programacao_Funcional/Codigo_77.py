'''
Closure e funções  que retornam outras funções

'''

import os

os.system('color 1f')

def criar_saudacao(saudacao):

    def saudar(nome):
        
        return f'{saudacao}, {nome}!'
    
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_tarde = criar_saudacao('Boa tarde')
falar_boa_noite = criar_saudacao('Boa noite')

print('\n')

for nome in ['Maria', 'João', 'Davi']:
    
    print('---')
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))
    print('---')

print('\n')

os.system('pause')
os.system('cls')