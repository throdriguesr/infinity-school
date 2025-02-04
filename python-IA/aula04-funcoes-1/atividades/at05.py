'''
Crie uma função que receba dois números e retorne a multiplicação deles.

'''

def multiplicar(numero1, numero2):
    return numero1 * numero2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = multiplicar(num1, num2)
print(f"\nA multiplicação de {num1} e {num2} é {resultado}.")