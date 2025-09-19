'''
Funções decoradoras e decoradores

Decorar = Adicionar / Remover / Restringir / Alterar

Funções decoradoras são funções que decoram outras funções

Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.

Decoradores são "Syntax Sugar" (Açúcar sintático)

'''

import os

os.system('color 1f')

print('\n******************************\n')

def criar_funcao(func):
    
    def interna(*args, **kwargs):
        
        print('Vou te Decorar')
        
        for arg in args:
            
            e_string(arg)
        
        resultado = func(*args, **kwargs)
        
        print(f'Seu resultado foi {resultado}')        
        print('Ok, agora você foi decorada')
        
        return resultado
    
    return interna

def inverte_string(string):
    
    return string[::-1]

def e_string(param):
    
    if not isinstance(param, str):
        
        raise TypeError('Parâmetro deve ser uma string')
    
invertida_string_checando_parametro = criar_funcao(inverte_string)

invertida1 = invertida_string_checando_parametro('Joao') # oaoJ
invertida2 = invertida_string_checando_parametro(123) # Apresenta erro TypeError

print(invertida1)

print('\n******************************\n')

print(invertida2)

print('\n******************************\n')

os.system('pause')
os.system('cls')