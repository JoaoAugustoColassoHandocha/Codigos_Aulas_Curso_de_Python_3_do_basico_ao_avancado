'''
Polimorfismo em Python Orientado a Objetos

Polimorfismo é o princípio que permite que classes deridavas de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.

Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)

Opinião + princípios que contam:

Assinatura do método:
nome, parâmetros e retorno iguais
SO"L"ID
Princípio da substituição de liskov
Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.
Sobrecarga de métodos (overload)  🐍 = ❌
Sobreposição de métodos (override) 🐍 = ✅

'''

import os
from abc import ABC, abstractmethod

class Notificacao(ABC):
    
    def __init__(self, mensagem) -> None:
        
        self.mensagem = mensagem
    
    @abstractmethod    
    def enviar(self): ...

print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')