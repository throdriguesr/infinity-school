'''
Formulário Estilizado

Crie uma interface de formulário com campos de entrada para nome e e-mail, e um botão de envio. 
Estilize os campos de entrada e o botão.

'''

import flet as ft

def main(page: ft.Page):
    page.title = "Formulário Estilizado"

    campo_nome = ft.TextField(
        label="Nome",
        border_color="blue",
        border_radius=10,
        text_style=ft.TextStyle(size=16)
    )

    campo_email = ft.TextField(
        label="Email",
        border_color="green",
        border_radius=10,
        text_style=ft.TextStyle(size=16)
    )

    texto_confirmacao = ft.Text(value="", color="green")

    def enviar(e):
        if campo_nome.value and campo_email.value:
            texto_confirmacao.value = "Enviado com sucesso!"
        else:
            texto_confirmacao.value = "Preencha todos os campos!"
            texto_confirmacao.color = "red"
        page.update()

    botao_enviar = ft.ElevatedButton(
        text="Enviar",
        style=ft.ButtonStyle(
            bgcolor="purple",
            color="white",
            text_style=ft.TextStyle(size=18),
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        on_click=enviar
    )

    page.add(
        campo_nome,
        campo_email,
        botao_enviar,
        texto_confirmacao
    )

ft.app(target=main)