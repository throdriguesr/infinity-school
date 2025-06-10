'''
Estilizando Botões

Crie uma interface com três botões estilizados. 
Aplique diferentes cores de fundo, cores de texto e tamanhos de fonte a cada botão.

'''

import flet as ft

def main(page: ft.Page):
    page.title = "Botões Estilizados"

    botao1 = ft.ElevatedButton(
        text="Botão Vermelho",
        style=ft.ButtonStyle(
            bgcolor="red",
            color="white",
            text_style=ft.TextStyle(size=18)
        )
    )

    botao2 = ft.ElevatedButton(
        text="Botão Verde",
        style=ft.ButtonStyle(
            bgcolor="green",
            color="black",
            text_style=ft.TextStyle(size=16)
        )
    )

    botao3 = ft.ElevatedButton(
        text="Botão Azul",
        style=ft.ButtonStyle(
            bgcolor="blue",
            color="yellow",
            text_style=ft.TextStyle(size=20)
        )
    )

    page.add(
        botao1,
        botao2,
        botao3
    )

ft.app(target=main)