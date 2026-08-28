'''
@staticmethod (métodos estáticos) são inúteis em Python =)

Métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls.

Em resumo, são funções que existem dentro da sua classe.

'''

import os

print('\n------------------------------\n')

class Classe:
    
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        
        print('Oi', args, kwargs)
        
def funcao(*args, **kwargs):
        
        print('Oi', args, kwargs)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')