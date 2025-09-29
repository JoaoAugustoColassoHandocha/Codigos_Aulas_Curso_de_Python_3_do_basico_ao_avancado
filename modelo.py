'''


'''

import os

os.system('color 1f')

print('\n******************************\n')



print('\n******************************\n')

os.system('pause')
os.system('cls')

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado  = ['BA', 'SP', 'MG', 'RJ']

combinados = zip(cidade, estado)

lista_combinados = list(combinados)

for cidade_estado in lista_combinados:
           
    print(f'{cidade_estado[0]} - {cidade_estado[1]}')