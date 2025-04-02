'''
Criar um Formulário de Cadastro

Propor aos participantes que criem um formulário de cadastro utilizando Flet.
Incluir campos como nome, sobrenome, email, etc.
Encorajar a aplicação de diferentes widgets e layouts para organizar o formulário.

'''

import flet as ft

def main(page):
    page.title = "Formulário de Cadastro"
    
    nome = ft.TextField(label="Nome")
    sobrenome = ft.TextField(label="Sobrenome")
    email = ft.TextField(label="Email")
    senha = ft.TextField(label="Senha", password=True)
    confirmar_senha = ft.TextField(label="Confirmar Senha", password=True)
    resultado = ft.Text()
    
    def cadastrar(e):
        if senha.value != confirmar_senha.value:
            resultado.value = "As senhas não são iguais!"
        else:
            resultado.value = f"Cadastro feito! Bem-vindo, {nome.value} {sobrenome.value}."
        page.update()
    
    botao_cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar)
    
    page.add(
        nome,
        sobrenome,
        email,
        senha,
        confirmar_senha,
        botao_cadastrar,
        resultado
    )

ft.app(target=main)