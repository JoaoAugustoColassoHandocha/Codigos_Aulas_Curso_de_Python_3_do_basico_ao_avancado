'''
# @property - um getter no modo Pythônico

# getter - um método para obter um atributo

# cor -> get_cor()

# modo pythônico - modo do Python de fazer coisas

@property é uma propriedade do objeto, ela é um método que se comporta como um atributo 🤯 🤯 🤯

Geralmente é usada nas seguintes situações:

- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo

Código cliente - é o código que usa seu código

'''

import os

print('\n------------------------------\n')

class Caneta:
    
    def __init__(self, cor):
        
        # private | protected | public
        self.cor = cor

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')