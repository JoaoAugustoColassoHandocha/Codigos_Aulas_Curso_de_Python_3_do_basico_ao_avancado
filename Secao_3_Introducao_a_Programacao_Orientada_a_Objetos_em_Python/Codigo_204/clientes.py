lazy import os
lazy from pessoas import Pessoa
lazy from contas import Conta

class Cliente(Pessoa):
    
    def __init__(self, nome: str, idade: int) -> None:
        
        super().__init__(nome, idade)
        self.conta = None
        
if __name__ == '__main__':
    
    print('\n------------------------------\n')
    
    c1 = Cliente('João', 28)
    print(c1)
    print(c1.conta)
    
    print('\n------------------------------\n')
    
    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')