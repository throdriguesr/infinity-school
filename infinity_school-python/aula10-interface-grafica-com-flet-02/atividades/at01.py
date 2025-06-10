'''
Personalização de Texto

Crie uma interface com três textos estilizados de maneiras diferentes. 
Aplique cores, tamanhos de fonte e pesos de fonte diferentes a cada texto.

'''

import flet as ft

def main(page: ft.Page):
    page.title = "Textos Estilizados"

    texto1 = ft.Text(
        value="Texto Vermelho e Grande",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="red"
    )

    texto2 = ft.Text(
        value="Texto Azul e Médio",
        size=20,
        weight=ft.FontWeight.W500,
        color="blue"
    )

    texto3 = ft.Text(
        value="Texto Verde e Pequeno",
        size=16,
        weight=ft.FontWeight.NORMAL,
        color="green"
    )

    page.add(
        texto1,
        texto2,
        texto3
    )

ft.app(target=main)