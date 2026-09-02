'''
Relações entre classes: associação, agregação e composição

Agregação é uma forma mais especializada de associação entre dois ou mais objetos. 

Cada objeto terá seu ciclo de vida independente.

Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.

Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa. (existem controvérsias sobre as definições de agregação).

'''

import os

class Carrinho:
    
    def __init__(self):
        
        self._produtos = []
        
    def total(self):
        
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
            
            self._produtos.extend(produtos)
    
    def listar_produtos(self):
        
        for produto in self._produtos:
            
            print(f'{produto.nome} - R${produto.preco:.2f}')
            
class Produto:
    
    def __init__(self, nome, preco):
        
        self.nome = nome
        self.preco = preco
        
carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)

print('\n------------------------------\n')

carrinho.listar_produtos()
print(f'\nTotal: R${carrinho.total():.2f}')

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')