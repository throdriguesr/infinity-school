'''
Interface com Temas

Crie uma interface que aplica um tema personalizado com cores primária, secundária, de fundo e de texto. 
Inclua pelo menos um texto e um botão para visualizar o tema aplicado.

'''

import flet as ft

def main(page: ft.Page):
    page.title = "Interface com Tema"

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="purple",
            secondary="orange",
            background="#f0f0f0",
            on_primary="white",
            on_secondary="black"
        )
    )

    page.bgcolor = page.theme.color_scheme.background

    texto = ft.Text(
        value="Tema Personalizado Ativo",
        size=24,
        color=page.theme.color_scheme.primary
    )

    botao = ft.ElevatedButton(
        text="Clique Aqui",
        style=ft.ButtonStyle(
            bgcolor=page.theme.color_scheme.secondary,
            color=page.theme.color_scheme.on_secondary,
            text_style=ft.TextStyle(size=18)
        )
    )

    page.add(
        texto,
        botao
    )

ft.app(target=main)