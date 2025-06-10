'''
Crie um Aplicativo de Calculadora Simples

O aplicativo deve ser capaz de realizar operações básicas de matemática, como adição, subtração, multiplicação e divisão.
Implemente uma interface limpa e intuitiva, com botões para os números e operações, além de uma área para exibir o resultado das operações.

'''

import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"

    campo_resultado = ft.TextField(value="", read_only=True, text_align="right", expand=True)
    expressao = ""

    def adicionar(e):
        nonlocal expressao
        expressao += e.control.text
        campo_resultado.value = expressao
        page.update()

    def limpar(e):
        nonlocal expressao
        expressao = ""
        campo_resultado.value = ""
        page.update()

    def calcular(e):
        nonlocal expressao
        try:
            expressao = str(eval(expressao.replace("×", "*").replace("÷", "/")))
        except:
            expressao = "Erro"
        campo_resultado.value = expressao
        page.update()

    botoes = [
        ["7", "8", "9", "÷"],
        ["4", "5", "6", "×"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"]
    ]

    linhas = []

    for linha in botoes:
        botoes_linha = []
        for texto in linha:
            if texto == "=":
                botao = ft.ElevatedButton(text=texto, on_click=calcular, expand=True)
            else:
                botao = ft.ElevatedButton(text=texto, on_click=adicionar, expand=True)
            botoes_linha.append(botao)
        linhas.append(ft.Row(botoes_linha, expand=True))

    botao_limpar = ft.Row([
        ft.ElevatedButton(text="Limpar", on_click=limpar, expand=True)
    ])

    page.add(
        ft.Column([campo_resultado] + linhas + [botao_limpar])
    )

ft.app(target=main)