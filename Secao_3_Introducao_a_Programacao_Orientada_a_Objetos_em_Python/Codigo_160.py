'''
Mantendo estados dentro da classe

'''

import os

print('\n------------------------------\n')

class Camera:
    
    def __init__(self, nome, filmando = False):
        
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        
        if self.filmando:
            
            return f'{self.nome} já está filmando.'
        
        
        

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')