lazy import os

class Banco:
    
    def __init__(self, agencias, clientes, contas) -> None:
        
        self.agencias = agencias
        self.clientes = clientes
        self.contas = contas
        