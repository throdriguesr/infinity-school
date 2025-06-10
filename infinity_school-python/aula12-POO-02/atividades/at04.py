'''
Crie uma interface chamada "Veículo" com métodos "acelerar" e "frear".

Em seguida, crie classes concretas como "Carro" e "Bicicleta" que implementem a interface "Veículo" e forneçam suas próprias implementações dos métodos "acelerar" e "frear". 

Demonstre como o polimorfismo pode ser usado para tratar diferentes tipos de veículos de maneira uniforme, chamando os métodos da interface.

'''

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando...")

    def frear(self):
        print("Carro freando...")

class Bicicleta(Veiculo):
    def acelerar(self):
        print("Bicicleta ganhando velocidade...")

    def frear(self):
        print("Bicicleta reduzindo velocidade...")

def testar_veiculo(veiculo):
    veiculo.acelerar()
    veiculo.frear()

carro = Carro()
bicicleta = Bicicleta()

print("Teste com o carro:")
testar_veiculo(carro)

print("\nTeste com a bicicleta:")
testar_veiculo(bicicleta)