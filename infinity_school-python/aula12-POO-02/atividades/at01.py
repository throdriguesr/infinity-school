'''
Crie uma hierarquia de classes representando formas geométricas. 
Comece com uma classe base chamada "Forma" e, em seguida, crie classes derivadas como "Círculo" e "Retângulo" que herdem da classe base.
Adicione métodos para calcular área e perímetro em cada classe derivada.

'''

class Forma:
    def area(self):
        pass

    def perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

circulo = Circulo(5)
retangulo = Retangulo(4, 7)

print("Área do círculo:", circulo.area())
print("Perímetro do círculo:", circulo.perimetro())

print("Área do retângulo:", retangulo.area())
print("Perímetro do retângulo:", retangulo.perimetro())