'''
Desenvolva um aplicativo de gerenciamento de tarefas em python. 
Crie duas classes, Tarefa e Projeto, com uma associação unidirecional. 
Permita que as tarefas sejam associadas a projetos e que você possa listar as tarefas de um projeto em particular.

'''

class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def marcar_como_concluida(self):
        self.concluida = True

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.lista_de_tarefas.append(tarefa)

    def mostrar_tarefas(self):
        print("Tarefas do projeto:", self.nome)
        for tarefa in self.lista_de_tarefas:
            print("Título:", tarefa.titulo)
            print("Descrição:", tarefa.descricao)
            if tarefa.concluida:
                print("Status: Concluída")
            else:
                print("Status: Pendente")
            print("-----")

meu_projeto = Projeto("Estudos de Python")

tarefa1 = Tarefa("Aprender classes", "Estudar como funcionam as classes em Python")
tarefa2 = Tarefa("Fazer exercícios", "Praticar criando objetos e listas")

meu_projeto.adicionar_tarefa(tarefa1)
meu_projeto.adicionar_tarefa(tarefa2)

tarefa1.marcar_como_concluida()

meu_projeto.mostrar_tarefas()