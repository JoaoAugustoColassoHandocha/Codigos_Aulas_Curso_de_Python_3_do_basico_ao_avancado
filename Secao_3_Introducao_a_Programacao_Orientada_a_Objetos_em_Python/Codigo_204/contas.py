lazy import os
from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia, conta, saldo):
        
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abstractmethod
    def sacar(self, valor): pass
    
    def depositar(self, valor):
        
        self.saldo += valor
        self.detalhes(f'(Depósito: {valor})')
        
    def detalhes(self, msg = ''):
        
        print(f'Saldo: {self.saldo:.2f} {msg}')
    
class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            
            self.saldo -= valor
            self.detalhes(f'(Saque: {valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado!')
        self.detalhes(f'(Saque Negado: {valor})')