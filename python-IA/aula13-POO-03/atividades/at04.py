'''
Desenvolva uma classe Produto em python que contenha atributos privados, como nome, preço e quantidade em estoque. 
Forneça métodos públicos para acessar e modificar esses atributos e garantir que o preço e a quantidade não sejam definidos como valores negativos.

'''

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco if preco >= 0 else 0
        self.__quantidade = quantidade if quantidade >= 0 else 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade

produto1 = Produto("Fone de Ouvido", 150.0, 10)

print("Produto:", produto1.get_nome())
print("Preço: R$", produto1.get_preco())
print("Quantidade em estoque:", produto1.get_quantidade())

produto1.set_preco(180.0)
produto1.set_quantidade(15)

print("Novo preço: R$", produto1.get_preco())
print("Nova quantidade em estoque:", produto1.get_quantidade())

produto1.set_preco(-50)
produto1.set_quantidade(-10)

print("Tentando valores negativos:")
print("Preço: R$", produto1.get_preco())
print("Quantidade em estoque:", produto1.get_quantidade())