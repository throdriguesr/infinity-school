'''
Escreva um programa que solicite números ao usuário até
que ele digite um número negativo, somando apenas os
números positivos inseridos.

'''

soma = 0

while True:
    numero = int(input("Digite um número positivo (ou negativo caso deseje sair): "))

    if numero < 0:
        break

    soma += numero

print(f"A soma dos números positivos é: {soma}")