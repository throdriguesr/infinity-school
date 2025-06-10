'''
Desenvolver um programa de linha de comando que permite
aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
prioridades e categorias. O projeto será organizado em várias
partes e usará funções, listas, tuplas, dicionários, conjuntos e
um ambiente virtual.

'''

tarefas = []

def exibir_menu():
    while True:  
        print("\n    Menu de Comandos    ")
        print("\n1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir tarefas por filtro")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            concluir_tarefa()
        elif opcao == '4':
            exibir_por_filtro()
        elif opcao == '5':
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida. Tente novamente.") 

def adicionar_tarefa():
    nome = input("\nDigite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
    categoria = input("Digite a categoria da tarefa: ")

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "status": "Não Concluída"
    }

    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.")
    else:
        print("\nLista de Tarefas:")
        for tarefa in tarefas:
            print(f"\nNome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Categoria: {tarefa['categoria']}")
            print(f"Status: {tarefa['status']}")

def concluir_tarefa():
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\nTarefas disponíveis:")
    for i in range(len(tarefas)):
        print(f"{i + 1}. {tarefas[i]['nome']} - Status: {tarefas[i]['status']}")

    escolha = input("\nDigite o número da tarefa que deseja marcar como concluída: ")

    if not escolha.isdigit():
        print("\nPor favor, digite um número válido.")
        return

    escolha = int(escolha)
    if escolha < 1 or escolha > len(tarefas):
        print("\nNúmero inválido. Tente novamente.")
        return

    tarefas[escolha - 1]["status"] = "Concluída"
    print(f"\nTarefa '{tarefas[escolha - 1]['nome']}' marcada como concluída!")

def exibir_por_filtro():
    print("\nComo deseja filtrar as tarefas?")
    print("1. Por prioridade")
    print("2. Por categoria")
    escolha = input("Digite 1 ou 2 para escolher: ")

    if escolha == '1':
        prioridade_filtro = input("\nDigite a prioridade (Alta, Média, Baixa): ")
        print(f"\nTarefas com prioridade {prioridade_filtro}:")
        for tarefa in tarefas:
            if tarefa["prioridade"].lower() == prioridade_filtro.lower():
                print(f"- {tarefa['nome']} | {tarefa['descricao']} | Status: {tarefa['status']}")

    elif escolha == '2':
        categoria_filtro = input("\nDigite a categoria: ")
        print(f"\nTarefas na categoria {categoria_filtro}:")
        for tarefa in tarefas:
            if tarefa["categoria"].lower() == categoria_filtro.lower():
                print(f"- {tarefa['nome']} | {tarefa['descricao']} | Status: {tarefa['status']}")
    else:
        print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    exibir_menu()