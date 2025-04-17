'''
DESAFIO PRÁTICO

Sistema de Biblioteca

Imagine um sistema de biblioteca em Python que gerencia livros e usuários. 
As classes envolvidas são Livro, Usuario, Biblioteca e Emprestimo.

A classe Livro deve ter atributos privados, como título e autor, e métodos públicos para obter esses atributos.

A classe Usuario deve ter atributos privados, como nome e ID, e métodos públicos para obter e modificar esses atributos.

A classe Biblioteca deve conter uma lista de livros disponíveis e métodos para adicionar e remover livros.

A classe Empréstimo deve representar um empréstimo de um livro por um usuário e deve estar associada a um Livro e a um Usuário.
O exercício é criar essas classes, estabelecer a associação entre elas (um usuário pode pegar emprestado um livro da biblioteca), aplicar encapsulamento para proteger os atributos privados e implementar métodos para:

Adicionar e remover livros da biblioteca.

Registrar um empréstimo de livro por um usuário, verificando se o livro está disponível.

Exibir informações sobre os empréstimo, como qual livro foi emprestado para qual usuário.

'''

class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor


class Usuario:
    def __init__(self, nome, id_usuario):
        self.__nome = nome
        self.__id_usuario = id_usuario

    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id_usuario

    def set_nome(self, novo_nome):
        self.__nome = novo_nome


class Biblioteca:
    def __init__(self):
        self.__livros_disponiveis = []

    def adicionar_livro(self, livro):
        self.__livros_disponiveis.append(livro)

    def remover_livro(self, livro):
        if livro in self.__livros_disponiveis:
            self.__livros_disponiveis.remove(livro)

    def listar_livros(self):
        if not self.__livros_disponiveis:
            print("Nenhum livro disponível.")
        else:
            print("Livros disponíveis:")
            for i, livro in enumerate(self.__livros_disponiveis):
                print(f"{i+1}. {livro.get_titulo()} - {livro.get_autor()}")

    def verificar_disponibilidade(self, livro):
        return livro in self.__livros_disponiveis

    def get_livros(self):
        return self.__livros_disponiveis


class Emprestimo:
    def __init__(self, usuario, livro):
        self.__usuario = usuario
        self.__livro = livro

    def info_emprestimo(self):
        return f"{self.__livro.get_titulo()} ({self.__livro.get_autor()}) → {self.__usuario.get_nome()} (ID: {self.__usuario.get_id()})"


usuarios = []
emprestimos = []
biblioteca = Biblioteca()


def cadastrar_usuario():
    nome = input("Nome do usuário: ")
    id_usuario = input("ID do usuário: ")
    usuario = Usuario(nome, id_usuario)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!\n")


def adicionar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    livro = Livro(titulo, autor)
    biblioteca.adicionar_livro(livro)
    print("Livro adicionado com sucesso!\n")


def listar_livros():
    biblioteca.listar_livros()
    print()


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
    else:
        print("Usuários cadastrados:")
        for i, u in enumerate(usuarios):
            print(f"{i+1}. {u.get_nome()} (ID: {u.get_id()})")
        print()


def realizar_emprestimo():
    if not usuarios or not biblioteca.get_livros():
        print("É necessário ter pelo menos um usuário e um livro disponível para fazer um empréstimo.\n")
        return

    listar_usuarios()
    usuario_index = int(input("Escolha o número do usuário: ")) - 1
    usuario = usuarios[usuario_index]

    listar_livros()
    livro_index = int(input("Escolha o número do livro: ")) - 1
    livro = biblioteca.get_livros()[livro_index]

    if biblioteca.verificar_disponibilidade(livro):
        emprestimo = Emprestimo(usuario, livro)
        emprestimos.append(emprestimo)
        biblioteca.remover_livro(livro)
        print("Empréstimo realizado com sucesso!\n")
    else:
        print("Livro indisponível!\n")


def listar_emprestimos():
    if not emprestimos:
        print("Nenhum empréstimo registrado.\n")
    else:
        print("Empréstimos realizados:")
        for e in emprestimos:
            print("-", e.info_emprestimo())
        print()


def menu():
    while True:
        print("====== Sistema de Biblioteca ======")
        print("1. Cadastrar Usuário")
        print("2. Adicionar Livro")
        print("3. Listar Livros")
        print("4. Listar Usuários")
        print("5. Realizar Empréstimo")
        print("6. Listar Empréstimos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            adicionar_livro()
        elif opcao == "3":
            listar_livros()
        elif opcao == "4":
            listar_usuarios()
        elif opcao == "5":
            realizar_emprestimo()
        elif opcao == "6":
            listar_emprestimos()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida!\n")


menu()