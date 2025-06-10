'''
Aplicativo de hotelaria

Crie uma classe Hotel que permita gerenciar funcionários, reservas e quartos de hotel. 
Os funcionários devem ter informações como nome, função e salário. 
O hotel deve ser capaz de receber reservas, atribuí-las a quartos e calcular a conta final.

'''

class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario


class Quarto:
    def __init__(self, numero, preco_diaria):
        self.numero = numero
        self.preco_diaria = preco_diaria
        self.ocupado = False


class Reserva:
    def __init__(self, nome_cliente, dias, quarto: Quarto):
        self.nome_cliente = nome_cliente
        self.dias = dias
        self.quarto = quarto
        self.valor_total = 0

    def calcular_valor(self):
        self.valor_total = self.dias * self.quarto.preco_diaria
        return self.valor_total


class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def listar_quartos_disponiveis(self):
        return [q for q in self.quartos if not q.ocupado]

    def fazer_reserva(self, nome_cliente, dias):
        quartos_disponiveis = self.listar_quartos_disponiveis()
        if not quartos_disponiveis:
            print("Nenhum quarto disponível.")
            return None

        quarto = quartos_disponiveis[0]
        quarto.ocupado = True
        reserva = Reserva(nome_cliente, dias, quarto)
        reserva.calcular_valor()
        self.reservas.append(reserva)
        print(f"Reserva feita para {nome_cliente} no quarto {quarto.numero} por {dias} dias.")
        return reserva

    def listar_reservas(self):
        for r in self.reservas:
            print(f"Cliente: {r.nome_cliente} | Quarto: {r.quarto.numero} | Total: R${r.valor_total:.2f}")


hotel = Hotel("Hotel Paraíso")

hotel.adicionar_funcionario(Funcionario("Carlos", "Recepcionista", 2500))
hotel.adicionar_funcionario(Funcionario("Ana", "Camareira", 2000))

hotel.adicionar_quarto(Quarto(101, 150))
hotel.adicionar_quarto(Quarto(102, 200))

hotel.fazer_reserva("Thiago", 3)
hotel.fazer_reserva("Fernanda", 2)

hotel.listar_reservas()