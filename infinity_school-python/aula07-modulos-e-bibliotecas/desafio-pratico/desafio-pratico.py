'''

Gerenciador de Livros de Biblioteca

Crie um programa que permita aos usuários:

- Adicionar novos livros à biblioteca, com informações como título, autor e número de cópias disponíveis.
- Listar todos os livros disponíveis na biblioteca.
- Permitir aos usuários fazer empréstimos de livros, reduzindo o número de cópias disponíveis quando um livro é emprestado.
- Permitir aos usuários devolver livros, aumentando o número de cópias disponíveis quando um livro é devolvido.
- Verificar a disponibilidade de um livro específico na biblioteca.
- Mostrar a lista de livros emprestados a um usuário específico.

'''

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.emprestimos = {}

    def adicionar_livro(self):
        titulo = input("\nDigite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        copias = int(input("Digite o número de cópias disponíveis: "))
        if titulo in self.livros:
            self.livros[titulo]['copias'] += copias
        else:
            self.livros[titulo] = {'autor': autor, 'copias': copias}
        print("\nLivro adicionado!")

    def listar_livros(self):
        if not self.livros:
            print("\nNenhum livro disponível.")
        else:
            for titulo, info in self.livros.items():
                print(f"\n{titulo} - {info['autor']} ({info['copias']} cópias)")

    def emprestar_livro(self):
        usuario = input("\nDigite seu nome: ")
        titulo = input("Digite o título do livro que deseja emprestar: ")
        if titulo in self.livros and self.livros[titulo]['copias'] > 0:
            self.livros[titulo]['copias'] -= 1
            if usuario not in self.emprestimos:
                self.emprestimos[usuario] = []
            self.emprestimos[usuario].append(titulo)
            print("\nLivro emprestado!")
        else:
            print("\nLivro indisponível!")

    def devolver_livro(self):
        usuario = input("\nDigite seu nome: ")
        titulo = input("Digite o título do livro que deseja devolver: ")
        if usuario in self.emprestimos and titulo in self.emprestimos[usuario]:
            self.emprestimos[usuario].remove(titulo)
            self.livros[titulo]['copias'] += 1
            print("\nLivro devolvido!")
        else:
            print("\nUsuário não tem esse livro!")

    def verificar_disponibilidade(self):
        titulo = input("\nDigite o título do livro: ")
        if titulo in self.livros and self.livros[titulo]['copias'] > 0:
            print("\nDisponível!")
        else:
            print("\nIndisponível!")

    def livros_emprestados(self):
        usuario = input("\nDigite seu nome: ")
        if usuario in self.emprestimos:
            print(f"\nLivros emprestados: {self.emprestimos[usuario]}")
        else:
            print("\nNenhum livro emprestado!")

bib = Biblioteca()

while True:
    print("\nGerenciador de Biblioteca")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Verificar Disponibilidade")
    print("6. Ver Livros Emprestados")
    print("7. Sair")
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        bib.adicionar_livro()
    elif opcao == "2":
        bib.listar_livros()
    elif opcao == "3":
        bib.emprestar_livro()
    elif opcao == "4":
        bib.devolver_livro()
    elif opcao == "5":
        bib.verificar_disponibilidade()
    elif opcao == "6":
        bib.livros_emprestados()
    elif opcao == "7":
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida! Tente novamente.")