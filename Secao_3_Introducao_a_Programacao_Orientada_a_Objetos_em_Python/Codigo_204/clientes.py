lazy import os, contas
lazy from pessoas import Pessoa

class Cliente(Pessoa):
    
    def __init__(self, nome: str, idade: int) -> None:
        
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None
        
if __name__ == '__main__':
    
    print('\n------------------------------\n')
    
    c1 = Cliente('João', 28)
    c1.conta = contas.ContaCorrente(111, 222, 0.00, 0.00)
    print(c1)
    print(c1.conta)
    
    print('\n------------------------------\n')
    
    c2 = Cliente('Maria', 24)
    c2.conta = contas.ContaPoupanca(111, 333, 0.00)
    print(c2)
    print(c2.conta)
        
    print('\n------------------------------\n')
    
    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')