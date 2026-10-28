lazy import os

class Pessoa:
    
    def __init__(self, nome: str, idade: int) -> None:
        
        self.nome = nome
        self.idade = idade
        
    @property
    def nome(self):
        
        return self._nome
    
    @nome.setter
    def nome(self):
        
        ...
    
    
    @property
    def idade(self):
        
        return self._idade
    
    @idade.setter
    def idade(self):
        
        ...