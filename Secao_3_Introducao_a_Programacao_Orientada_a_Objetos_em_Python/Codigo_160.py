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
        
        print(f'{self.nome} está filmando.')
        self.filmando = True
        
    
        
c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
print(c1.filmar())
        

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')