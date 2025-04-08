'''
Crie um classe chamada cachorro com os atributos: nome, raça, idade

'''

class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

meu_cachorro = Cachorro("Trovão", "Pastor Alemão", 3)
print(f"Nome: {meu_cachorro.nome}, Raça: {meu_cachorro.raca}, Idade: {meu_cachorro.idade} anos")