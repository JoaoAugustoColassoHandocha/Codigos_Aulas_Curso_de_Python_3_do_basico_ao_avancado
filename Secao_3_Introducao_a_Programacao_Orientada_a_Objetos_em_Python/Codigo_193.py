'''
Update Codigo_193.py

Context Manager com classes - Criando e Usando gerenciadores de contexto

Você pode implementar seus próprios protocolos apenas implementando os dunder methods que o Python vai usar.

Isso é chamado de Duck typing.

Um conceito relacionado com tipagem dinâmica onde o Python não está interessado no tipo, mas se alguns métodos existem no seu objeto para que ele funcione de forma adequada.

Duck Typing:

Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato.

Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados.

O método __exit__ receberá a classe de exceção, a exceção e o traceback.

Se ele retornar True, exceção no with será suprimidas.

Ex:

with open('aula149.txt', 'w') as arquivo:

    ...

'''

import os

class MyOpen:
    
    def __init__(self, caminho_arquivo, modo):
        
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        
        print('Executando arquivo!\n')
              
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding = 'UTF8')
        
        return self._arquivo
        
    def __exit__(self, class_exception, exception_, traceback_):
        
        print('\nFechando arquivo!')
        
        self._arquivo.close()
        

print('\n------------------------------\n')

with MyOpen('Codigo_193.txt', 'w') as arquivo:
    
    print('WITH', arquivo)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')