'''
@property + @setter - getter e setter no modo Pythônico

- como getter -> Obtendo valor
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo

Atributos que começar com um ou dois underlines não devem ser usados fora da classe.

_ ou __ = Não utilizar o atributo

'''

import os
class Caneta:
    
    def __init__(self, cor):
        
        # private | protected
        self._cor = cor
        self._cor_tampa = None
        
    @property
    def cor(self):
        
        return self._cor
    
    @property
    def cor_tampa(self):
        
        return self._cor_tampa
    
    @cor.setter
    def cor(self, valor):
        
        if valor == 'Rosa':
            
            raise ValueError('[AVISO] Cor não aceita!')
        
        self._cor = valor
        
    @cor_tampa.setter
    def cor_tampa(self, valor):
        
        self._cor_tampa = valor
    
caneta = Caneta('')
caneta.cor = input('\nCor da Caneta: ')
caneta.cor_tampa = input('\nCor da Tampa: ')
os.system('cls' if os.name == 'nt' else 'clear')

print('\n------------------------------\n')

print(f'Cor da Caneta: {caneta.cor} | Cor da Tampa: {caneta.cor_tampa}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')