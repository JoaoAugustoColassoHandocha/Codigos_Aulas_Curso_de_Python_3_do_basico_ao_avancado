lazy import os
lazy from pessoas import Pessoa
lazy from contas import Conta

class Cliente(Pessoa):
    
    def __init__(self, nome: str, idade: int) -> None:
        
        super().__init__(nome, idade)
        self.conta = None