'''
Crie uma função que aceite dois números e uma operação (por exemplo, adição, subtração, multiplicação, divisão) como argumentos e use funções lambda para realizar a operação especificada. A função deve retornar o resultado da operação.

'''

def calcular(num1, num2, operacao):
    if operacao == "adição":
        return num1 + num2
    elif operacao == "subtração":
        return num1 - num2
    elif operacao == "multiplicação":
        return num1 * num2
    elif operacao == "divisão":
        return num1 / num2 if num2 != 0 else "Erro: divisão por zero"
    else:
        return "Operação inválida"

print(calcular(10, 5, "adição"))
print(calcular(10, 5, "subtração"))
print(calcular(10, 5, "multiplicação"))
print(calcular(10, 5, "divisão"))
print(calcular(10, 0, "divisão"))
print(calcular(10, 5, "potência"))