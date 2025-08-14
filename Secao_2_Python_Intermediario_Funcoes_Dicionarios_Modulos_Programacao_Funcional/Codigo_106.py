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

def ge1():
    
    print('COMEÇO GEN1')    
    yield 1
    yield 2
    yield 3
    print('TERMINO GEN1')
    
def gen2(gen):
    
    print('COMEÇO GEN2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('TERMINO GEN2')
    
def gen3():
    
    print('COMEÇO GEN3')
    yield 10
    yield 20
    yield 30
    print('TERMINO GEN3')
    
    
g1 = gen2()

for numero in gen:
    
    print(numero) # 1 a 6

print('\n##############################\n')

os.system('pause')
os.system('cls')