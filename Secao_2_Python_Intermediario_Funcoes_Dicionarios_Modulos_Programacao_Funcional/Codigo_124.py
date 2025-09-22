'''
Decoradores com parâmetros

'''

import os

os.system('color 1f')

print('\n******************************\n')

def fabrica_de_decoradores(a, b, c):
    
    print(a, b, c)

    def fabrica_de_funcoes(func):
        
        print('Decoradora 1')
        
        def aninhada(*args, **kwargs):
            
            print('Aninhada')
            
            res = func(*args, **kwargs) # soma(*args, **kwargs)
            
            return res
        
        return aninhada
    
    return fabrica_de_funcoes

@fabrica_de_decoradores()
def soma(x, y):
    
    return x + y

# Nome da Função = Nome do Decorador(Parâmetro do Decorador)(Conteúdo da Função)
multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)

print(dez_mais_cinco)
print(dez_vezes_cinco)

print('\n******************************\n')

os.system('pause')
os.system('cls')