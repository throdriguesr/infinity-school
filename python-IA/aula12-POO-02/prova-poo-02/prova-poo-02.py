'''
[PYIA-A12] Crie uma classe base chamada Veiculo que tenha um método chamado movimentar. 
Este método deve imprimir a mensagem "Veículo está em movimento." para indicar que qualquer veículo está em movimento. 
Em seguida, crie duas subclasses chamadas Carro e Moto que herdem de Veiculo. 
Dentro de cada uma dessas subclasses, sobrescreva o método movimentar para imprimir mensagens específicas para cada tipo de veículo. 
Na classe Carro, o método movimentar deve imprimir "Carro está dirigindo.", enquanto na classe Moto, o método deve imprimir "Moto está acelerando."

'''

class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")


class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")


class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")


v1 = Veiculo()
v2 = Carro()
v3 = Moto()

v1.movimentar()
v2.movimentar()
v3.movimentar()