import flet as ft
import uuid
from datetime import datetime

class Pessoa:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)
        self.id = str(uuid.uuid4())

    def exibir_informacoes(self):
        return f"ID: {self.id}, Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.__disponivel = True

    def esta_disponivel(self):
        return self.__disponivel

    def reservar(self):
        self.__disponivel = False

    def liberar(self):
        self.__disponivel = True

    def info(self):
        status = "Disponível" if self.__disponivel else "Ocupado"
        return f"Quarto {self.numero} - {self.tipo} - R${self.preco}/dia - {status}"

class Reserva:
    def __init__(self, cliente, quarto, checkin, checkout):
        self.cliente = cliente
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout
        self.status = "Ativa"

    def cancelar(self):
        self.status = "Cancelada"
        self.quarto.liberar()

    def info(self):
        return f"Reserva de {self.cliente.nome} no quarto {self.quarto.numero} de {self.checkin} a {self.checkout} - {self.status}"

class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def criar_reserva(self, cliente_id, numero_quarto, checkin, checkout):
        cliente = next((c for c in self.clientes if c.id == cliente_id), None)
        quarto = next((q for q in self.quartos if q.numero == numero_quarto), None)
        if cliente and quarto and quarto.esta_disponivel():
            reserva = Reserva(cliente, quarto, checkin, checkout)
            quarto.reservar()
            self.reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        reserva.cancelar()

    def listar_reservas(self):
        return self.reservas

    def listar_clientes(self):
        return self.clientes

gerenciador = GerenciadorDeReservas()
gerenciador.adicionar_quarto(Quarto(101, "Single", 150))
gerenciador.adicionar_quarto(Quarto(102, "Double", 200))
gerenciador.adicionar_quarto(Quarto(103, "Suite", 300))

def main(pagina: ft.Page):
    pagina.title = "Sistema de Reservas - Refúgio dos Sonhos"
    reserva_list = ft.Column()
    cliente_list = ft.Column()
    quarto_list = ft.Column([ft.Text(q.info()) for q in gerenciador.quartos])

    def atualizar_reservas():
        reserva_list.controls = []
        for reserva in gerenciador.reservas:
            texto = ft.Text(reserva.info())
            if reserva.status == "Ativa":
                botao_cancelar = ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, r=reserva: cancelar_reserva(r))
                reserva_list.controls.append(ft.Row([texto, botao_cancelar]))
            else:
                reserva_list.controls.append(texto)
        pagina.update()

    def atualizar_clientes():
        cliente_list.controls = []
        for cliente in gerenciador.clientes:
            texto = ft.Text(cliente.exibir_informacoes())
            botao_editar = ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, c=cliente: editar_cliente(c))
            cliente_list.controls.append(ft.Row([texto, botao_editar]))
        pagina.update()

    def cancelar_reserva(reserva):
        gerenciador.cancelar_reserva(reserva)
        atualizar_reservas()

    def abrir_formulario_cliente(e):
        nome = ft.TextField(label="Nome")
        telefone = ft.TextField(label="Telefone")
        email = ft.TextField(label="Email")
        def salvar_cliente(x):
            cliente = Cliente(nome.value, telefone.value, email.value)
            gerenciador.adicionar_cliente(cliente)
            atualizar_clientes()
            pagina.dialog.open = False
            pagina.update()
        pagina.dialog = ft.AlertDialog(title=ft.Text("Novo Cliente"), content=ft.Column([nome, telefone, email]),
                                       actions=[ft.ElevatedButton("Salvar", on_click=salvar_cliente)])
        pagina.dialog.open = True
        pagina.update()

    def editar_cliente(cliente):
        nome = ft.TextField(label="Nome", value=cliente.nome)
        telefone = ft.TextField(label="Telefone", value=cliente.telefone)
        email = ft.TextField(label="Email", value=cliente.email)
        def salvar_edicao(x):
            cliente.nome = nome.value
            cliente.telefone = telefone.value
            cliente.email = email.value
            atualizar_clientes()
            pagina.dialog.open = False
            pagina.update()
        pagina.dialog = ft.AlertDialog(title=ft.Text("Editar Cliente"), content=ft.Column([nome, telefone, email]),
                                       actions=[ft.ElevatedButton("Salvar", on_click=salvar_edicao)])
        pagina.dialog.open = True
        pagina.update()

    def abrir_formulario_reserva(e):
        cliente_id = ft.TextField(label="ID do Cliente")
        numero_quarto = ft.TextField(label="Número do Quarto")
        checkin = ft.TextField(label="Data Check-in (YYYY-MM-DD)")
        checkout = ft.TextField(label="Data Check-out (YYYY-MM-DD)")
        def salvar_reserva(x):
            gerenciador.criar_reserva(cliente_id.value, int(numero_quarto.value), checkin.value, checkout.value)
            atualizar_reservas()
            pagina.dialog.open = False
            pagina.update()
        pagina.dialog = ft.AlertDialog(title=ft.Text("Nova Reserva"), content=ft.Column([cliente_id, numero_quarto, checkin, checkout]),
                                       actions=[ft.ElevatedButton("Reservar", on_click=salvar_reserva)])
        pagina.dialog.open = True
        pagina.update()

    pagina.add(ft.Text("Quartos Disponíveis"), quarto_list)
    pagina.add(ft.ElevatedButton("Novo Cliente", on_click=abrir_formulario_cliente))
    pagina.add(ft.Text("Clientes"), cliente_list)
    pagina.add(ft.ElevatedButton("Nova Reserva", on_click=abrir_formulario_reserva))
    pagina.add(ft.Text("Reservas"), reserva_list)

    atualizar_clientes()
    atualizar_reservas()

ft.app(target=main)