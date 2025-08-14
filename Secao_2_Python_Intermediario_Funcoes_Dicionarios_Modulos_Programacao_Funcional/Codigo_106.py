'''
Yield from

'''

import os

os.system('color 1f')

print('\n##############################\n')

def gen1():
    
    yield 1
    yield 2
    yield 3
    
def gen2():
    
    yield from gen1()
    yield 4
    yield 5
    yield 6
    
gen = gen2()

for numero in gen:
    
    print(numero) # 1 a 6

print('\n##############################\n')

def gen1():
    
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
    
    
g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    
    print(numero) 
    
for numero in g2:
    
    print(numero)
    
'''
COMEÇO GEN2
COMEÇO GEN1
1
2
3
TERMINO GEN1
4
5
6
TERMINO GEN2
COMEÇO GEN2
COMEÇO GEN3
10
20
30
TERMINO GEN3
4
5
6
TERMINO GEN2

'''

print('\n##############################\n')

def gen1():
    
    print('COMEÇO GEN1')    
    yield 1
    yield 2
    yield 3
    print('TERMINO GEN1')
    
def gen2(gen = None):
    
    print('COMEÇO GEN2')
    
    if gen is not None:
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
    
    
g1 = gen2(gen1)
g2 = gen2(gen3)
g2 = gen2()

for numero in g1:
    
    print(numero) 
    
for numero in g2:
    
    print(numero)
    
'''
COMEÇO GEN2
COMEÇO GEN1
1
2
3
TERMINO GEN1
4
5
6
TERMINO GEN2
COMEÇO GEN2
COMEÇO GEN3
10
20
30
TERMINO GEN3
4
5
6
TERMINO GEN2

'''

print('\n##############################\n')

os.system('pause')
os.system('cls')