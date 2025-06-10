'''
Desenvolva uma aplicação de loja online em. 
Crie as classes Cliente e Pedido com uma associação bidirecional. 
Os clientes podem fazer pedidos, e os pedidos devem estar associados aos clientes que os
fizeram. 
Implemente a capacidade de listar todos os pedidos de um cliente específico.

'''

class Pedido:
    def __init__(self, descricao, valor, cliente):
        self.descricao = descricao
        self.valor = valor
        self.cliente = cliente
        cliente.adicionar_pedido(self)

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        print("Pedidos do cliente:", self.nome)
        for pedido in self.pedidos:
            print("Descrição:", pedido.descricao)
            print("Valor: R$", pedido.valor)
            print("-----")

cliente1 = Cliente("Thiago")
pedido1 = Pedido("Teclado Mecânico", 250.00, cliente1)
pedido2 = Pedido("Mouse Gamer", 120.00, cliente1)

cliente1.listar_pedidos()