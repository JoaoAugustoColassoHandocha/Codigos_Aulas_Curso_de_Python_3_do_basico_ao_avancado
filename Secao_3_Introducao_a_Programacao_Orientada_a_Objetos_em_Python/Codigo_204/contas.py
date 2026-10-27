lazy import os
from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia, conta, saldo):
        
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    def depositar(self, valor):
        
        self.saldo += valor