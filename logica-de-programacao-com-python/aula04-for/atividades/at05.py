'''
Contagem de Números Positivos e Negativos:
Escreva um programa que solicite ao usuário 10 números e use um
laço for com uma condicional para contar quantos são positivos e
quantos são negativos.

'''

positivos = 0
negativos = 0

print("Digite 10 números (positivos ou negativos):")

for _ in range(10):
    numero = int(input("Digite um número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nVocê digitou {positivos} números positivos e {negativos} números negativos.")