'''
Dado um dicionário que representa as vendas de produtos, encontre o produto mais vendido (ou os produtos mais vendidos, se houver um empate).

'''

vendas = {
    "maçã": 10,
    "banana": 25,
    "laranja": 25,
    "uva": 15
}

maior_venda = max(vendas.values())

mais_vendidos = []
for produto, quantidade in vendas.items():
    if quantidade == maior_venda:
        mais_vendidos.append(produto)

print("\nProduto(s) mais vendido(s):", mais_vendidos)