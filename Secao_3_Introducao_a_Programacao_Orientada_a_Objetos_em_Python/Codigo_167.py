'''
method vs @classmethod vs @staticmethod

method - self, método de instância

@classmethod - cls, método de classe

@staticmethod - método estático (❌self, ❌cls)

'''

import os

print('\n------------------------------\n')

class Connection:
    
    def __init__(self, host = 'localhost'):
        
        self.host = host
        
    # setter
    def set_user(self, user):
        
        self.user = user
        
    # setter
    def set_password(self, password):
            
        self.password = password
        
c1 = Connection()
c1.set_user('Luiz')
print(c1.user)
c1.set_password('123')
print(c1.password)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')