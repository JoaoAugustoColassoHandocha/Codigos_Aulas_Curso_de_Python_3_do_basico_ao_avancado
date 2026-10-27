lazy import os
lazy from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia, conta, saldo):
        
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abstractmethod
    def sacar(self, valor): pass
    
    def depositar(self, valor):
        
        self.saldo += valor
        self.detalhes(f'(Depósito: R${valor:.2f})')
        
    def detalhes(self, msg = ''):
        
        print(f'Saldo: R${self.saldo:.2f} {msg}')
    
class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0.00:
            
            self.saldo -= valor
            self.detalhes(f'(Saque: R${valor:.2f})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado!')
        self.detalhes(f'(Saque Negado: R${valor:.2f})')

class ContaCorrente(Conta):
    
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)
        
    def sacar(self, valor):
        
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0.00:
            
            self.saldo -= valor
            self.detalhes(f'(Saque: R${valor:.2f})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado!')
        self.detalhes(f'(Saque Negado: R${valor:.2f})')

# Teste do código dentro do módulo, evitando a execução diretamente no main.py
if __name__ == '__main__':    
    
    print('\n------------------------------\n')

    cp1 = ContaPoupanca(111, 222, 0.00)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)

    print('\n------------------------------\n')

    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')