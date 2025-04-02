'''
[PYIA-A09] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. 
A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. 
Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. 
A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.

'''

import flet as ft

def main(page):
    page.title = "Lista de Tarefas"
    
    entrada_tarefa = ft.TextField(label="Digite a tarefa")
    
    lista_tarefas = ft.Column()
    
    def adicionar_tarefa(e):
        if entrada_tarefa.value.strip():
            lista_tarefas.controls.append(ft.Text(entrada_tarefa.value))
            entrada_tarefa.value = ""
            page.update()
    
    botao_adicionar = ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefa)
    
    page.add(
        entrada_tarefa,
        botao_adicionar,
        lista_tarefas
    )

ft.app(target=main)