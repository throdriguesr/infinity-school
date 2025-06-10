'''
[PYIA-A13] Crie uma classe chamada ContaBancaria que tenha dois atributos privados, _saldo e _titular. 
O atributo _saldo deve armazenar o saldo da conta, enquanto o atributo _titular deve armazenar o nome do titular da conta. 
Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. 
Crie um método depositar que permita adicionar um valor ao saldo, um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), e um método exibir_saldo que exiba o saldo atual da conta. 
Utilize métodos para encapsular o acesso ao saldo, garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque.

'''

class ContaBancaria:
    def __init__(self, titular):
        self._titular = titular
        self._saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Você depositou R${valor:.2f}.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Você sacou R${valor:.2f}.")
            else:
                print("Você não tem saldo suficiente.")
        else:
            print("Valor inválido para saque.")

    def exibir_saldo(self):
        print(f"Seu saldo atual é: R${self._saldo:.2f}")


print("Bem-vindo ao Banco do Thiago!")
nome = input("Digite o seu nome: ")
conta = ContaBancaria(nome)

while True:
    print("\nO que você deseja fazer?")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao == "1":
        valor = float(input("\nDigite o valor para depositar: "))
        conta.depositar(valor)

    elif opcao == "2":
        valor = float(input("\nDigite o valor para sacar: "))
        conta.sacar(valor)

    elif opcao == "3":
        conta.exibir_saldo()

    elif opcao == "4":
        print("\nObrigado por usar o Banco do Thiago. Até a próxima!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
