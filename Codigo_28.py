'''
Flag (Bandeira) - Marcar um local
None = Não Valor
is e is not = É ou não é (tipo, valor, identidade)
id = Identidade (local na memória)

'''

import os

os.system('color 1f')

v1 = 'a'

print(id(v1))

os.system('pause')
os.system('cls')

condicao = False
passou_no_if = None

if condicao == True:
    
    passou_no_if = True
    print('\nVerdadeiro\n')
    
elif condicao == False:
    
    print('\nFalso\n')
    
else:
    
    print('\nErro no processamento!\n')
    
if passou_no_if is not None:
    
    print('Passou no if\n')
    
elif passou_no_if is None:
    
    print('Não passou no if\n')
    
else:
    
    print('Erro no processamento!\n')

os.system('pause')
os.system('cls')