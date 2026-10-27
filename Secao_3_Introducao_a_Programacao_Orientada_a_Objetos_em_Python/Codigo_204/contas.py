lazy import os
from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia, conta, saldo):
        
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abstractmethod
    def sacar(self, valor): ...
    
    def depositar(self, valor):
        
        self.saldo += valor
        self.detalhes(f'(Depósito: {valor})')
        
    def detalhes(self, msg = ''):
        
        print(f'Saldo: {self.saldo:.2f} {msg}')
    
class ContaPoupanca(Conta): ...