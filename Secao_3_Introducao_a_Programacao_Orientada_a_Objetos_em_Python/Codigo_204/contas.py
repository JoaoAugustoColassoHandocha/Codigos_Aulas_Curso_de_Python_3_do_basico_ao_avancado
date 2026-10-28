lazy import os
lazy from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia: int, conta: int, saldo: float = 0.00) -> None:
        
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abstractmethod
    def sacar(self, valor: float) -> float: pass
    
    def depositar(self, valor: float) -> float:
        
        self.saldo += valor
        self.detalhes(f'(Depósito: R${valor:.2f})')
        return self.saldo  
        
    def detalhes(self, msg: str = '') -> None:
        
        print(f'Saldo: R${self.saldo:.2f} {msg}')
        
    def __repr__(self):
                
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r:.2f})' 
        return f'{class_name} {attrs}'
    
class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0.00:
            
            self.saldo -= valor
            self.detalhes(f'(Saque: R${valor:.2f})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado!')
        self.detalhes(f'(Saque Negado: R${valor:.2f})')
        return self.saldo

class ContaCorrente(Conta):
    
    def __init__(self, agencia: int, conta: int, saldo: float = 0.00, limite: float = 0.00) -> None:
        
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        
    def sacar(self, valor: float) -> float:
        
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        
        if valor_pos_saque >= limite_maximo:
            
            self.saldo -= valor
            self.detalhes(f'(Saque: R${valor:.2f})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado!')
        print(f'Seu limite é R${-self.limite:.2f}')
        self.detalhes(f'(Saque Negado: R${valor:.2f})')
        return self.saldo
    
    def __repr__(self):
                
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})' 
        return f'{class_name} {attrs}'

# Teste do código dentro do módulo, evitando a execução diretamente no main.py
if __name__ == '__main__':    
    
    print('\n------------------------------\n')

    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    # Saldo: R$0.00

    print('\n------------------------------\n')

    cc1 = ContaCorrente(111, 222, 0.00, 100.00)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(99)
    cc1.sacar(1)
    # Saldo: R$-100.00 (Usando o limite)

    print('\n------------------------------\n')

    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')