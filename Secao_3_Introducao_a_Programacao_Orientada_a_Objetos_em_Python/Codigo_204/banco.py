lazy import os, contas, pessoas, clientes

class Banco:
    
    def __init__(self, agencias: list[int] | None = None, clientes: list[pessoas.Pessoa] | None = None, contas: list[contas.Conta] | None = None):
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
        
    def _checa_agencia(self, conta):
        
        if conta.agencia in self.agencias:
            
            print('_checa_agencia', True)
            
            return True
        
        print('_checa_agencia', False)
            
        return False
    
    def _checa_cliente(self, cliente):
        
        if cliente in self.clientes:
            
            print('_checa_cliente', True)
            
            return True
        
        print('_checa_cliente', False)
        
        return False
    
    def _checa_conta(self, conta):
        
        if conta in self.contas:
            
            print('_checa_conta', True)
                    
            return True
        
        print('_checa_conta', False)
        
        return False
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        
        if conta in self.contas:
                    
            print('_checa_conta', True)
                            
            return True
                
        print('_checa_conta', False)
                
        return False
    
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        
        return self._checa_agencia(conta) and self._checa_cliente(cliente) and self._checa_conta(conta) and self._checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self):
        
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        
        return f'{class_name} {attrs}'
    
if __name__ == '__main__':
    
    print('\n------------------------------\n')
    
    c1 = clientes.Cliente('João', 28)
    cc1 = contas.ContaCorrente(111, 222, 0.00, 0.00)
    c1.conta = cc1
    
    print('\n------------------------------\n')
    
    c2 = clientes.Cliente('Maria', 24)
    cp2 = contas.ContaPoupanca(112, 223, 0.00)
    c2.conta = cp2
    
    print('\n------------------------------\n')
    
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp2])
    banco.agencias.extend([111, 222])
    print(banco)
    
    print('\n------------------------------\n')
    
    print(banco.autenticar(c1, cp2)) # False (Tentando autenticar com a conta de outro cliente)
    
    print('\n------------------------------\n')
    
    print(banco.autenticar(c1, cc1)) # True (Autenticado com a conta certa)
        
    print('\n------------------------------\n')
    
    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')