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

    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.

-> = Agregação

'''

lazy import os, builtins, shutil
lazy from abc import ABC, abstractmethod

try:
    
    _print_original = builtins.print

    def print_centralizado(*args, **kwargs):
    
        largura = shutil.get_terminal_size().columns
        texto = " ".join(str(a) for a in args)
    
        for linha in texto.splitlines() or [""]:
            
            _print_original(linha.center(largura), **kwargs)

    builtins.print = print_centralizado
    builtins.input = print_centralizado
    
    class Conta(ABC):
        
        @abstractmethod
        def sacar(self): ...

        @abstractmethod
        def depositar(self): ...
        
    class ContaCorrente(Conta): 
    
        def sacar(self): ...
        
        def depositar(self): ...
    
    class ContaPoupanca(Conta):
        
        def sacar(self): ...
        
        def depositar(self): ...
    
    class Pessoa(ABC):
        
        def __init__(self, nome, idade):
            
            self.nome = nome
            self.idade = idade
            
        @property
        def pessoa_nome(self):
            
            return self.nome
        
        @property
        def pessoa_idade(self):
            
            return self.idade
    
    class Cliente(Pessoa): ...
    
    class Banco: ...
    
    print('\n------------------------------')
    print('Bem Vindo ao SolarisBank')
    print('------------------------------\n')
    
    print(2/0)
    
    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

except Exception as error:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\nOps! Ocorreu um erro inesperado ao processar sua solicitação.\n')
    print('Entre em contato com o suporte técnico, informando nome do erro.')
    print(f'\nErro: {error} ({type(error).__name__})\n')

    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')