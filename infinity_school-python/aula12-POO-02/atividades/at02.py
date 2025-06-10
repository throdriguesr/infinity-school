'''
Crie uma hierarquia de classes que represente veículos.
Comece com uma classe base "Veículo" e, em seguida, crie classes derivadas como "Carro" e "Bicicleta". 
Adicione métodos para definir atributos, como "cor" e "modelo", e permita a chamada de métodos em cadeia para configurar esses atributos.

'''

class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None

    def set_cor(self, cor):
        self.cor = cor
        return self

    def set_modelo(self, modelo):
        self.modelo = modelo
        return self

    def mostrar_dados(self):
        print("Modelo:", self.modelo)
        print("Cor:", self.cor)

class Carro(Veiculo):
    pass

class Bicicleta(Veiculo):
    pass

carro1 = Carro().set_cor("Vermelho").set_modelo("Sedan")
bicicleta1 = Bicicleta().set_cor("Azul").set_modelo("Mountain Bike")

print("Dados do carro:")
carro1.mostrar_dados()

print("\nDados da bicicleta:")
bicicleta1.mostrar_dados()