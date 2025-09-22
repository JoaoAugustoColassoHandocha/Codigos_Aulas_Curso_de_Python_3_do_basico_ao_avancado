'''
Ordem dos decoradores

'''

import os

os.system('color 1f')

print('\n******************************\n')

def parametros_decorador(nome):
    
    def decorador(func):
        
        print(f'Decorador: {nome}')
        
        def sua_nova_funcao(*args, **kwargs):
            
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            
            return final
        
        return sua_nova_funcao
    
    return decorador

@parametros_decorador(nome = 'primeiro')
def soma(x, y):
    
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

print('\n******************************\n')

os.system('pause')
os.system('cls')