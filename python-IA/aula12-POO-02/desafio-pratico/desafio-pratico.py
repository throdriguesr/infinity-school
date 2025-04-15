'''
Sistema de gerenciamento de contas bancárias em Python

Crie um sistema de gerenciamento de contas bancárias em Python usando herança e polimorfismo. 
O sistema deve incluir as seguintes classes:

Classe Conta:

-A classe base "Conta" deve ter atributos para o número da conta, o titular da conta e o saldo.

-Ela deve incluir métodos para depósitos, saques e exibição do saldo atual.

Classe ContaCorrente:

-A classe "ContaCorrente" herda de "Conta" e inclui atributos específicos, como taxa de manutenção e limite de cheque especial.

-Deve sobrescrever o método de saque para considerar o limite de cheque especial, se necessário.

Classe ContaPoupanca:

-A classe "ContaPoupanca" também herda de "Conta" e inclui atributos específicos, como taxa de juros.

-Ela deve ter um método para calcular e adicionar juros ao saldo.

-Crie um método chamado resumo que pode ser chamado em qualquer objeto de conta (ContaCorrente ou ContaPoupanca).

Esse método resumo irá exibir um resumo das informações da conta, incluindo o tipo de conta (corrente ou poupança), o número da conta, o titular da conta e o saldo atual.

Teste de Funcionalidade:

Crie um programa principal que demonstre o uso dessas classes. Crie instâncias de contas correntes e poupanças, realize depósitos, saques, adicione juros e chame o método resumo para cada conta.

'''

class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f}')
        else:
            print('Saldo insuficiente.')

    def exibir_saldo(self):
        print(f'Saldo: R${self.saldo:.2f}')

    def resumo(self):
        print(f'Conta: {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}')


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, taxa=10, limite=500):
        super().__init__(numero, titular, saldo)
        self.taxa = taxa
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f}')
        else:
            print('Limite do cheque especial excedido.')

    def resumo(self):
        print(f'[Conta Corrente] {self.numero} | {self.titular} | Saldo: R${self.saldo:.2f}')


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, juros=0.01):
        super().__init__(numero, titular, saldo)
        self.juros = juros

    def adicionar_juros(self):
        valor_juros = self.saldo * self.juros
        self.saldo += valor_juros
        print(f'Juros de R${valor_juros:.2f}')

    def resumo(self):
        print(f'[Conta Poupança] {self.numero} | {self.titular} | Saldo: R${self.saldo:.2f}')


cc = ContaCorrente("123", "Thiago", 100)
cp = ContaPoupanca("456", "Helena", 500)

cc.depositar(200)
cc.sacar(350)
cc.resumo()

print("------")

cp.sacar(100)
cp.adicionar_juros()
cp.resumo()