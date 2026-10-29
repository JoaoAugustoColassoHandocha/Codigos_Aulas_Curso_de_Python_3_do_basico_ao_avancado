lazy import os, contas, pessoas, clientes

class Banco:
    
    def __init__(self, agencias: list[int] | None = None, clientes: list[pessoas.Pessoa] | None = None, contas: list[contas.Conta] | None = None):
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
        
    def _checa_agencia(self, conta):
        
        if conta.agencia not in self.agencias:
            
            return False
            
        return True
    
    def _checa_cliente(self, cliente):
        
        if cliente not in self.clientes:
            
            return False
        
        return True
    
    def _checa_conta(self, conta):
        
        if conta not in self.contas:
                    
            return False
        
        return True
    
    def autenticar(self, cliente, conta):
        
        return self._checa_agencia(conta) and self._checa_cliente(cliente) and self._checa_conta(conta)
    
if __name__ == '__main__':
    
    c1 = clientes.Cliente('João', 28)
    c1.conta = contas.ContaCorrente(111, 222, 0.00, 0.00)
    
    print('\n------------------------------\n')
    
    c2 = clientes.Cliente('Maria', 24)
    c2.conta = contas.ContaPoupanca(111, 333, 0.00)