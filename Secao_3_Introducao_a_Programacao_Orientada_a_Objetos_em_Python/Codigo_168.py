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

class Caneta_Sem_Get:
    
    def __init__(self, cor):
        
        # private | protected | public
        self.cor = cor
        
caneta = Caneta_Sem_Get('Azul')

print(f'Cor da Caneta: {caneta.cor}')

print('\n------------------------------\n')

class Caneta_Com_Get:
    
    def __init__(self, cor):
        
        # private | protected | public
        self.cor_tinta = cor
       
    def get_cor(self):
        
        print('GET COR')
        
        return self.cor_tinta # Mesmo que mude o atributo, não vai quebrar códigos cliente

caneta = Caneta_Com_Get('Preta')
    
print(f'Cor da Caneta: {caneta.get_cor()}')

print('\n------------------------------\n')

class Caneta_Property:
    
    def __init__(self, cor):
        
        # private | protected | public
        self.cor_tinta = cor
       
    @property
    def cor(self):
        
        print('GET COR')
        
        return self.cor_tinta # Mesmo que mude o atributo, não vai quebrar códigos cliente

caneta = Caneta_Property('Preta')
    
print(f'Cor da Caneta: {caneta.get_cor()}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')