'''
Update Codigo_203.py

Exercício com Abstração, Herança, Encapsulamento e Polimorfismo

Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco.

A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta¹

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:

Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)¹

Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)

Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)

Banco será responsável autenticar o cliente e as contas da seguinte maneira:

    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.

-> = Agregação

'''

lazy import os, builtins, shutil, time, sys, getpass
lazy from abc import ABC, abstractmethod

try:
    
    # Complementos do aplicativo
    
    _print_original = builtins.print

    def print_centralizado(*args, **kwargs):
    
        largura = shutil.get_terminal_size().columns
        texto = ' '.join(str(a) for a in args)
    
        for linha in texto.splitlines() or ['']:
            
            _print_original(linha.center(largura), **kwargs)
    
    builtins.print = print_centralizado
    
    def input_centralizado(prompt = ''):
        
        print('\n')
    
        largura = shutil.get_terminal_size().columns
        # Move o prompt para o centro horizontal do terminal
        espaco = (largura - len(prompt)) // 2
        return input(' ' * max(espaco, 0) + prompt)

    def barra_carregamento(total=30, atraso=0.2):
        
        print('\n')
        
        for i in range(total + 1):
            porcentagem = int((i / total) * 100)
            barra = '█' * i + '-' * (total - i)
            texto = f'Carregando: |{barra}| {porcentagem}%'
            largura = shutil.get_terminal_size().columns
            sys.stdout.write('\r' + texto.center(largura - 1))
            sys.stdout.flush()
            time.sleep(atraso)
            
    # Banco  
    class Banco:
            
        agencia = '0001'
            
        def add_cliente(self, cliente):
                
            if cliente.conta.agencia != self.agencia:
                    
                print('Está conta nõa pertence a este banco!')
                
            cliente.conta.permissao = True
        
    # Pessoa
    class Pessoa(ABC):
            
        def __init__(self, nome, idade):
                
            self._nome = nome
            self._idade = idade
        
        @property
        def nome(self):
            
            return self._nome
        
        @property
        def idade(self):
            
            return self._idade
        
        @nome.setter
        def nome(self, nome):
            
            self._nome = nome
            
        @idade.setter
        def idade(self, idade):
            
            self._idade = idade
        
    class Cliente(Pessoa):
        
        def __init__(self, nome, idade, conta):
            
            super().__init__(nome, idade)
            
            self.nome = nome
            self.idade = idade
            self.conta = conta
            
    # Conta      
    class Conta(ABC):
            
            def __init__(self, agencia, conta, saldo):
                
                self.agencia = agencia
                self.conta = conta
                self.saldo = saldo
            
            @abstractmethod
            def sacar(self):
                
                pass

            def depositar(self, valor_depositar):
                
                if valor_depositar <= 0:
                    
                    print('Valor de depósito inválido!')
                    print('Favor inserir valor correto')
                    return
                    
                self.saldo += valor_depositar
                print(f'Depósito: {valor_depositar:.2f}')
                self.consulta_saldo()
                
            def consulta_saldo(self):
                
                print(f'Saldo: R${self.saldo:.2f}')
        
    class ContaCorrente(Conta):
        
        permissao = False
        
        def __init__(self, agencia, conta, saldo, limite):
            
            super().__init__(agencia, conta, saldo)
            self.limite = limite
    
        def sacar(self, valor_sacar_cc):
            
            if valor_sacar_cc <= 0:
                
                print('Valor de saque inválido!')
                print('Favor inserir valor correto')
                return
            
            elif valor_sacar_cc <= self.saldo:
                
                self.saldo -= valor_sacar_cc
                print(f'Saque: {valor_sacar_cc:.2f}')
                self.consulta_saldo()
                print(f'Limite: R${self.limite:.2f}')
                
                return
            
            elif (self.saldo + self.limite) >= valor_sacar_cc:
                
                self.saldo -= valor_sacar_cc
                self.limite += self.saldo
                self.saldo = 0
                print(f'Saque: {valor_sacar_cc:.2f}')
                self.consulta_saldo()
                print(f'Limite: R${self.limite:.2f}')
                                                
                return

            elif self.saldo == 0 and self.limite >= valor_sacar_cc:
                
                self.limite -= valor_sacar_cc
                print(f'Saque: {valor_sacar_cc:.2f}')
                self.consulta_saldo()
                print(f'Limite: R${self.limite:.2f}')
                                
                return
            
            else:
                
                print('Não foi possível sacar o valor desejado!')
                self.consulta_saldo()
                print(f'Limite: {self.limite:.2f}')
    
    class ContaPoupanca(Conta):
        
        permissao = False
        
        def __init__(self, agencia, conta, saldo):
            
            super().__init__(agencia, conta, saldo)
            
        def sacar(self, valor_sacar_cp):
            
            if valor_sacar_cp <= 0:
                
                print('Valor de saque inválido!')
                print('Favor inserir valor correto')
                return
            
            if self.saldo >= valor_sacar_cp:
                
                self.saldo -= valor_sacar_cp
                print(f'Saque: {valor_sacar_cp:.2f}')
                self.consulta_saldo()
                return
        
            print('Não foi possível sacar o valor desejado!')
            self.consulta_saldo()
    
    if __name__ == '__main__':
           
        banco = Banco()
        
        conta_cliente1 = ContaCorrente('0001', '123450', 400.00, 100.00)
        cliente1 = Cliente('João', '28', conta_cliente1)
        banco.add_cliente(cliente1)
        
        conta_cliente2 = ContaPoupanca('0001', '543211', 500.00)
        cliente2 = Cliente('Maria', '24', conta_cliente2)
        banco.add_cliente(cliente2)
            
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('\n------------------------------')
        print('Bem Vindo ao SolarisBank')
        print('------------------------------\n')
        
        barra_carregamento()
            
        os.system('cls' if os.name == 'nt' else 'clear')

        print('\n------------------------------')
        print('SolarisBank')
        print('------------------------------\n')
        print('\n')
        
        print(f'{cliente1.nome} tem {'Conta Corrente' if conta_cliente1.__class__.__name__ == 'ContaCorrente' else 'Conta Poupança'}, com saldo de R${conta_cliente1.saldo:.2f} e limite de R${conta_cliente1.limite:.2f}\n')
        print('\n')
        cliente1.conta.depositar(100)
        print(f'Limite: {cliente1.conta.limite:.2f}')
        print('\n')
        cliente1.conta.sacar(600)
        print('\n')
        input_centralizado('Clique em qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
            
        input_centralizado('Clique em qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
            
            
except Exception as error:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\nOps! Ocorreu um erro inesperado ao processar sua solicitação.\n')
    print('Entre em contato com o suporte técnico, informando nome do erro.')
    print(f'\nErro: {error} ({type(error).__name__})\n')

    input_centralizado('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')