'''
[PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

'''

def media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

mediaAritmetica = media(numero1, numero2, numero3)

print(f"\nA media aritmética dos números é {mediaAritmetica:.2f}.")