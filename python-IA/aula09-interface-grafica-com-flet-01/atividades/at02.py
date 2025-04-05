'''
Criar um Aplicativo de Lista de Tarefas

Propor aos participantes que criem um aplicativo de lista de tarefas simples utilizando Flet.
Incluir funcionalidades como adicionar, remover e marcar tarefas como concluídas.
Incentivar a utilização de eventos e interações do usuário.

'''

import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START

    lista_de_tarefas = ft.Column()
    campo_tarefa = ft.TextField(label="\nDigite sua tarefa", expand=True)

    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() != "":
            checkbox = ft.Checkbox(label=campo_tarefa.value)

            def riscar(e):
                if checkbox.value:
                    checkbox.label_style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
                else:
                    checkbox.label_style = ft.TextStyle(decoration=None)
                page.update()

            checkbox.on_change = riscar

            def remover_tarefa(e):
                lista_de_tarefas.controls.remove(linha)
                page.update()

            botao_remover = ft.IconButton(icon=ft.icons.DELETE, on_click=remover_tarefa)
            linha = ft.Row([checkbox, botao_remover])
            lista_de_tarefas.controls.append(linha)
            campo_tarefa.value = ""
            page.update()

    botao_adicionar = ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefa)

    page.add(
        ft.Row([campo_tarefa, botao_adicionar]),
        lista_de_tarefas
    )

ft.app(target=main)