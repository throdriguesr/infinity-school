'''
Crie uma classe chamada Fatura, a classe Fatura deve incluir os seguintes atributos: 
o nome do item; o preço unitário do item; quantidade de item a ser faturado; valor total da fatura. 
Sua classe deve ter um construtor que inicialize todos os atributos menos o valor total da fatura. 
Forneça um método chamado gerar_fatura que calcula o valor da fatura (isto é, multiplicar a quantidade pelo preço por item).

'''

class Fatura:
    def __init__(self, nome_item, preco_unitario, quantidade):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0

    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade
        return self.valor_total

fatura1 = Fatura("Teclado", 150.00, 2)
total = fatura1.gerar_fatura()

print(f"Item: {fatura1.nome_item}")
print(f"Preço Unitário: R${fatura1.preco_unitario:.2f}")
print(f"Quantidade: {fatura1.quantidade}")
print(f"Valor Total da Fatura: R${total:.2f}")