'''
Yield from

'''

import os

os.system('color 1f')

print('\n##############################\n')

def ge1():
    
    yield 1
    yield 2
    yield 3
    
def gen2():
    
    yield from ge1()
    yield 4
    yield 5
    yield 6
    
gen = gen2()

for numero in gen:
    
    print(numero) # 1 a 6

print('\n##############################\n')

os.system('pause')
os.system('cls')