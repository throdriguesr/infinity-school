'''
[PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.

'''

produtos = {}
contador = 0

while contador < 5: 
    produto = input("\nDigite o nome do produto: ")
    valor = float(input("Digite o preço do produto: R$ "))

    produtos[produto] = valor

    contador += 1

total = sum(produtos.values())

print(f"\nValor total da compra: R$ {total:.2f}")