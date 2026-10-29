lazy import os, contas, pessoas

class Banco:
    
    def __init__(self, agencias: list[int] | None = None, clientes: list[pessoas.Pessoa] | None = None, contas: list[contas.Conta] | None = None):
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
        
    def _checa_agencia(self, conta): ...
    
    def _checa_cliente(self, conta): ...
    
    def _checa_conta(self, conta): ...
    
    def autenticar(self, cliente, conta): ...
    
if __name__ == '__main__': ...    