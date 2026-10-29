lazy import os, contas, pessoas

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
        
        if conta.agencia not in self.agencias:
            
            return False
        
        return True
    
    def _checa_conta(self, conta):
        
        if conta.agencia not in self.agencias:
                    
            return False
        
        return True
    
    def autenticar(self, cliente, conta):
        
        if conta.agencia not in self.agencias:
                    
            return False
        
        return True
    
if __name__ == '__main__': ...    