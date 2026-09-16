'''


'''

import os
from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

print('\n------------------------------\n')

galaxy_s.ligar()
iphone.desligar()

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')