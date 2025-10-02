'''
Count é um iterador sem fim (itertools)

* É igual ao range, mas é utilizado quando não se sabe o fim.

range = (início, final, mutiplicador)

count = (início, multiplicador)

'''

import os
from itertools import count

os.system('color 1f')

print('\n******************************\n')

c1 = count(step = 8, start = 8)
r1 = range(0, 10, 2)

print(next(c1)) # 0
print(next(c1)) # 1

print('\n******************************\n')

# É um interável e um interator
print('c1', hasattr(c1, '__iter__')) # C1 True
print('c1', hasattr(c1, '__next__')) # C1 True

# É um interável, mas não é um interator
print('r1', hasattr(r1, '__iter__')) # R1 True
print('r1', hasattr(r1, '__next__')) # R1 False

print('\n******************************\n')

print('COUNT')

for i in c1:
    
    if i > 30:
        
        break
    
    print(i)

print('\n******************************\n')

print('RANGE')

for i in r1:
    
    print(i)

print('\n******************************\n')

os.system('pause')
os.system('cls')