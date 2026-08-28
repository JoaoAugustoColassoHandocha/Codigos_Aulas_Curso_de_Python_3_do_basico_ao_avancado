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
        
    @classmethod
    def create_with_auth(cls, user, password):
        
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        
        return msg
        
c1 = Connection()
c1.set_user('Luiz')
print(f'Usuário: {c1.user}')
c1.set_password('123')
print(f'Senha: {c1.password}')

print('\n')

c2 = Connection.create_with_auth('João', '1234')
print(f'Usuário: {c2.user}')
print(f'Senha: {c2.password}')

print(f'\n{Connection.log('Mensagem de Log')}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')