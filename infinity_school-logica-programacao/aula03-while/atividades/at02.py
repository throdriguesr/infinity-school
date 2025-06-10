'''
Soma de Números de 1 a 100:
Escreva um programa que use um laço while para
somar os números de 1 a 100 e exiba o resultado.

'''

soma = 0
numero = 1

while numero <= 100:
    soma += numero
    print(f"\nNúmero atual: {numero}, soma acumulada: {soma}")
    numero += 1

print("\nA soma dos números de 1 a 100 é: ", soma)