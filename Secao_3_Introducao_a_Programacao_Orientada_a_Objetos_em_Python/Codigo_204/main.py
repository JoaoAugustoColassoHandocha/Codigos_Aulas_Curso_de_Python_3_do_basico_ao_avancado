'''
Update Codigo_204.py

Solução do exercício com Abstração, Herança, Encapsulamento e Polimorfismo

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

'''

lazy import os, contas, pessoas, clientes, banco

c1 = clientes.Cliente('João', 28)
cc1 = contas.ContaCorrente(111, 222, 0.00, 0.00)
c1.conta = cc1

c2 = clientes.Cliente('Maria', 24)
cp2 = contas.ContaPoupanca(112, 223, 0.00)
c2.conta = cp2

print('\n------------------------------\n')

print(c1.conta)

print('\n------------------------------\n')

print(c2.conta)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')