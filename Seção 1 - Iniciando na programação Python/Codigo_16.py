# if |   elif   | else
# se | Se não se| se não

import os

os.system('color 1f')

ent = input('Você quer "entrar" ou "sair"? ')

if ent == 'entrar':
    
    print('Você entrou no sistema!')
    os.system('pause')
    
elif ent == 'sair':
    
    print('Você saiu do sistema!')
    os.system('pause')
    
else:
    
    print('Você não digitou nem entrar e nem sair!')
    os.system('pause')