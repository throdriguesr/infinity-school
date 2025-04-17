'''
Desenvolva uma classe ContaBancaria em Python com atributos privados, como saldo e número da conta. 
Forneça métodos públicos para depositar dinheiro, sacar dinheiro e verificar o saldo. 
Garanta que o saldo não seja definido como negativo e que as transações sejam  registradas.

'''

class ContaBancaria:
    def __init__(self, numero_conta):
        self.__numero_conta = numero_conta
        self.__saldo = 0.0
        self.__transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__transacoes.append(f"Depósito: R$ {valor}")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.__transacoes.append(f"Saque: R$ {valor}")
    
    def verificar_saldo(self):
        return self.__saldo

    def mostrar_transacoes(self):
        for t in self.__transacoes:
            print(t)

conta1 = ContaBancaria("123456")

conta1.depositar(1000)
conta1.sacar(300)
conta1.depositar(500)
conta1.sacar(2000)

print("Saldo atual: R$", conta1.verificar_saldo())
print("Transações:")
conta1.mostrar_transacoes()