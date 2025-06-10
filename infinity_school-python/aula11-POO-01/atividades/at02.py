'''
Crie um classe chamada pessoa com os atributos: nome, idade, peso, gênero.

'''

class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

pessoa1 = Pessoa("Thiago", 30, 85.5, "Masculino")
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso} kg, Gênero: {pessoa1.genero}")