'''
Desenvolvendo um Bloco de Notas Básico

Crie um bloco de notas básico usando Flet.
O bloco de notas deve permitir aos usuários digitar, editar e salvar texto.
A interface deve ser clara e direta, com menus ou botões para acessar as funcionalidades principais, como abrir, salvar e editar o texto.
Opcional:Implemente funcionalidades adicionais simples, como opções de formatação de texto (negrito, itálico, etc.) ou contagem de palavras.

'''

import flet as ft
from flet import FilePicker, FilePickerResultEvent

def main(page: ft.Page):
    page.title = "Bloco de Notas"

    area_texto = ft.TextField(multiline=True, expand=True, min_lines=20)
    seletor_arquivo = FilePicker()

    def salvar(e):
        def escrever_arquivo(result: FilePickerResultEvent):
            if result.path:
                with open(result.path, "w", encoding="utf-8") as f:
                    f.write(area_texto.value)

        page.dialog = seletor_arquivo
        seletor_arquivo.save_file(on_result=escrever_arquivo)

    def abrir(e):
        def ler_arquivo(result: FilePickerResultEvent):
            if result.path:
                with open(result.path, "r", encoding="utf-8") as f:
                    area_texto.value = f.read()
                page.update()

        page.dialog = seletor_arquivo
        seletor_arquivo.pick_files(allow_multiple=False, on_result=ler_arquivo)

    botao_abrir = ft.ElevatedButton(text="Abrir", on_click=abrir)
    botao_salvar = ft.ElevatedButton(text="Salvar", on_click=salvar)

    page.overlay.append(seletor_arquivo)

    page.add(
        ft.Row([botao_abrir, botao_salvar]),
        area_texto
    )

ft.app(target=main)