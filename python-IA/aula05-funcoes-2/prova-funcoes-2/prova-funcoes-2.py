'''
[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. 
Esta função deve comparar os três números e identificar qual deles é o maior. 
Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. 
A função deve então retornar o maior número encontrado.

'''

def maior_numero(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado = maior_numero(num1, num2, num3)
print(f"\nO maior número é: {resultado}")