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
        
    # Principal do aplicativo

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
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\n------------------------------')
    print('Bem Vindo ao SolarisBank')
    print('------------------------------\n')
    
    barra_carregamento()
    
    def menu(op = 0):
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print('\n------------------------------')
        print('SolarisBank')
        print('------------------------------\n')
        print('\n')
        
        nome_cliente = input('Nome Completo: ')
        agencia_cliente = int(input('Agência: '))
        conta_cliente = int(input('Conta: '))
        digito_conta_cliente = int(input('Dígito: '))
        senha_cliente = int(input('Senha: '))
    
        input_centralizado('Clique em qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        
    
    menu(op = 0)

except Exception as error:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\nOps! Ocorreu um erro inesperado ao processar sua solicitação.\n')
    print('Entre em contato com o suporte técnico, informando nome do erro.')
    print(f'\nErro: {error} ({type(error).__name__})\n')

    input_centralizado('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')