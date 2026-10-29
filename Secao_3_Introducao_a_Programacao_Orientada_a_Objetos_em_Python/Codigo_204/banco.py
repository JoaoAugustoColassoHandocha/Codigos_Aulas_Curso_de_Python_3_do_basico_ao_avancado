lazy import os, contas, pessoas

class Banco:
    
    def __init__(self, agencias: list[int] | None = None, clientes = None, contas = None):
        
        self.agencias = agencias
        self.clientes = clientes
        self.contas = contas
    
if __name__ == '__main__': ...    