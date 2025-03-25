'''
Crie um dicionário com informações de produtos, incluindo nome, preço e quantidade em estoque. 
Implemente funções para adicionar, remover e atualizar produtos no dicionário.

'''

produtos = {}

def adicionar_produto():
    nome = input("Nome do produto: ")
    if nome in produtos:
        print("Produto já existe. Use a opção de atualizar.")
        return
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produtos[nome] = {"preço": preco, "quantidade": quantidade}
    print(f"Produto '{nome}' adicionado.")

def remover_produto():
    nome = input("Nome do produto a remover: ")
    if nome in produtos:
        del produtos[nome]
        print(f"Produto '{nome}' removido.")
    else:
        print("Produto não encontrado.")

def atualizar_produto():
    nome = input("Nome do produto a atualizar: ")
    if nome in produtos:
        preco = input("Novo preço (deixe em branco para manter): ")
        quantidade = input("Nova quantidade (deixe em branco para manter): ")
        if preco:
            produtos[nome]["preço"] = float(preco)
        if quantidade:
            produtos[nome]["quantidade"] = int(quantidade)
        print(f"Produto '{nome}' atualizado.")
    else:
        print("Produto não encontrado.")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for nome, info in produtos.items():
            print(f"{nome} - R${info['preço']:.2f} - {info['quantidade']} em estoque")

while True:
    print("\n1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Atualizar Produto")
    print("4. Listar Produtos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        remover_produto()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        listar_produtos()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")