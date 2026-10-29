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
    
    print('\n------------------------------\n')
    
    c1 = clientes.Cliente('João', 28)
    cc1 = contas.ContaCorrente(111, 222, 0.00, 0.00)
    c1.conta = cc1
    
    print('\n------------------------------\n')
    
    c2 = clientes.Cliente('Maria', 24)
    cp2 = contas.ContaPoupanca(111, 333, 0.00)
    c2.conta = cp2
    
    print('\n------------------------------\n')
    
    banco = Banco()
    print(banco)
    
    print('\n------------------------------\n')
    
    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')