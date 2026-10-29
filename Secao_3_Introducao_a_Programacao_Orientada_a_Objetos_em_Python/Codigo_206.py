'''
Update Codigo_206.py

dataclasses - O que são dataclasses?

O módulo dataclasses fornece um decorador e funções para criar métodos como
__init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
usuário.

Em resumo: dataclasses são syntax sugar para criar classes normais.

Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.

doc: https://docs.python.org/3/library/dataclasses.html

'''

lazy import os
lazy from dataclasses import dataclass

@dataclass
class Pessoa:
    
    nome: str
    sobrenome: str
    
    @property
    def nome_completo(self):
        
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        
        nome, sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = sobrenome

print('\n------------------------------\n')

if __name__ == '__main__':
    
    p1 = Pessoa('João', 'Augusto')
    p2 = Pessoa.nome_completo = 'Maria Helena'
    
    print(p1)
    print()
    print(p1.nome_completo)
    
    print()
    
    print(p1)
    print()
    print(p1.nome_completo)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')