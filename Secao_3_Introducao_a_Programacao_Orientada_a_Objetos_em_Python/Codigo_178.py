'''
super() e a sobreposição de membros - Python Orientado a Objetos

Classe principal (Pessoa) -> super class, base class, parent class

Classes filhas (Cliente) -> sub class, child class, derived class

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
    
    def metodo(self):
        
        print('A')
        
class B(A):
    
    def metodo(self):
        
        print('B')
        
class C(B):
    
    def metodo(self):
        
        print('C')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')