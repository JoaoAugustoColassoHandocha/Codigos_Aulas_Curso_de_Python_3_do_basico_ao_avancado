'''


'''

import os

print('\n------------------------------\n')

class Animal:
    
    def __init__(self, nome):
        
        self.nome = nome
        
        variavel = 'valor'
        print(variavel)
        
    def comendo(self, alimento):
        
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        
        return self.comendo(*args, **kwargs)
    


print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')