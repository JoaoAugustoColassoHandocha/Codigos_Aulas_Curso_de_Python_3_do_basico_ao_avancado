# ... ou pass: Não executa nada, funcionando para situações onde não se quer fazer nada no momento naquela parte do código

import os

os.system('color 1f')

condicao1 = True
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    
    print('A condição 1 é verdadeira')
    
elif condicao2:
    
    print('A condição 2 é verdadeira')
    
elif condicao3:
    
    print('A condição 3 é verdadeira')
    
elif condicao4:
    
    print('A condição 4 é verdadeira')
    
else:
    
    print('Nenhuma condição é verdadeira')
    
print('Fora do if')

os.system('pause')