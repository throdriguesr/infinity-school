'''
[PYIA-A10] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato. 
O formulário deve incluir três campos: um campo de texto para o nome, um campo de texto para o email e um campo de texto para a mensagem. 
Após o usuário preencher esses campos, deve haver um botão de envio.
Quando o usuário clicar no botão de envio, os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela, indicando que o formulário foi enviado com sucesso.

'''

import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"

    campo_nome = ft.TextField(label="Nome", expand=True)
    campo_email = ft.TextField(label="Email", expand=True)
    campo_mensagem = ft.TextField(label="Mensagem", multiline=True, min_lines=4, expand=True)

    texto_confirmacao = ft.Text(value="", color="green")

    def enviar(e):
        if campo_nome.value and campo_email.value and campo_mensagem.value:
            texto_confirmacao.value = "Formulário enviado com sucesso!"
            campo_nome.value = ""
            campo_email.value = ""
            campo_mensagem.value = ""
        else:
            texto_confirmacao.value = "Por favor, preencha todos os campos."
            texto_confirmacao.color = "red"
        page.update()

    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar)

    page.add(
        campo_nome,
        campo_email,
        campo_mensagem,
        botao_enviar,
        texto_confirmacao
    )

ft.app(target=main)