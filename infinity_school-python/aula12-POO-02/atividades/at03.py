'''
Crie uma classe chamada "Calculadora" com um método "somar" que pode somar dois números inteiros ou duas strings.

Use o polimorfismo para implementar a sobrecarga do método "somar" para que ele funcione com diferentes tipos de entrada (números inteiros e strings). 

Crie exemplos de uso para demonstrar como a mesma função pode se comportar de maneira diferente com base nos tipos de entrada.

'''

class Calculadora:
    def somar(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            return "Tipos incompatíveis"

calc = Calculadora()

resultado1 = calc.somar(10, 5)
resultado2 = calc.somar("Olá, ", "mundo!")
resultado3 = calc.somar(10, "teste")

print("Soma de inteiros:", resultado1)
print("Soma de strings:", resultado2)
print("Tentativa de soma inválida:", resultado3)