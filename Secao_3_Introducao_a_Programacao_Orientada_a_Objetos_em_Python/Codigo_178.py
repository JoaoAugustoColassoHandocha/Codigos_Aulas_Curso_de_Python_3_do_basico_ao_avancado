'''
super() e a sobreposição de membros - Python Orientado a Objetos

Classe principal (Pessoa) -> super class, base class, parent class

Classes filhas (Cliente) -> sub class, child class, derived class

classe.mro() - serve para retornar a Method Resolution Order (Ordem de Resolução de Métodos) de uma classe

'''

import os

class MinhaString(str):
    
    def upper(self):
        
        print('Chamou Upper!')
        retorno =  super().upper()
        print('Depois do Upper!')
        return retorno
    
string = MinhaString('Luiz')

print('\n------------------------------\n')

print(string.upper())

print('\n------------------------------\n')

class A:
    
    atributo_a = 'valor A'
    
    def __init__(self, atributo):
        
        self.atributo = atributo
    
    def metodo(self):
        
        print('A')
        
class B(A):
    
    atributo_b = 'valor B'
    
    def metodo(self):
        
        print('B')
        
class C(B):
    
    atributo_c = 'valor C'
    
    def metodo(self):
        
        super().metodo() # B
        super(B, self).metodo() # A
        # super(A, self).metodo() # Object
        print('C')
        
        
# c = C()

# print(c.atributo_a) # valor A
# print(c.atributo_b) # valor B
# print(c.atributo_c) # valor C
# c.metodo() # B A C

c = C('Atributo')
        
print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')