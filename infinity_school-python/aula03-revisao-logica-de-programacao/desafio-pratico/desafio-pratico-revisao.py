'''
DESAFIO PRÁTICO

Gerenciamento de Compras de Produtos

Você foi contratado para desenvolver um programa simples para
auxiliar em um processo de compra de produtos. O programa deve
permitir ao usuário inserir o nome e o preço de vários produtos,
perguntando se deseja continuar inserindo mais produtos após cada
entrada. Ao final, o programa deve fornecer um resumo da compra,

incluindo:

A) O total gasto na compra.

B) A quantidade de produtos que custam mais de R$1000.

C) O nome do produto mais barato.

Desenvolva o programa em Python utilizando conceitos de
entrada/saída de dados, condicionais e laços de repetição.

'''

compra_do_cliente = {}

while True: 
    produto = input("\nDigite o nome do produto: ")
    valor = float(input("Digite o preço do produto: R$ "))

    compra_do_cliente[produto] = valor

    continuar = input("\nTecle 1 para continuar ou 2 para sair: ")

    if continuar == '2':
        break

total = sum(compra_do_cliente.values())
produto_mais_barato = min(compra_do_cliente, key=compra_do_cliente.get)

produtos_acima_1000 = {produto: preco for produto, preco in compra_do_cliente.items() if preco > 1000}

print("\n===== RESUMO DA COMPRA =====")
print(f"Total de produtos comprados: {len(compra_do_cliente)}")
print(f"Total gasto: R$ {total:.2f}")

print("\nLista de produtos:")
for produto, preco in compra_do_cliente.items():
    print(f"- {produto}: R$ {preco:.2f}")

print("\nDestaques:")
print(f"✔ Produto mais barato: {produto_mais_barato} - R$ {compra_do_cliente[produto_mais_barato]:.2f}")

print(f"✔ Produtos acima de R$1000: {len(produtos_acima_1000)}")
for produto, preco in produtos_acima_1000.items():
    print(f"   - {produto}: R$ {preco:.2f}")

print("============================")