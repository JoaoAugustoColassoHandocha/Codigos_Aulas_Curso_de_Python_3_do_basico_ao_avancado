lazy import os

class Pessoa:
    
    def __init__(self, nome: str, idade: int) -> None:
        
        self.nome = nome
        self.idade = idade
        
    @property
    def nome(self):
        
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        
        self._nome = nome
    
    @property
    def idade(self):
        
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        
        self._idade = idade
    
    # Sempre definir __repr__ quando o print apresenta <__main__.Cliente object at 0x000001CB9C64C6E0>, por exemplo  
    def __repr__(self):
        
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        
        return f'{class_name} {attrs}'