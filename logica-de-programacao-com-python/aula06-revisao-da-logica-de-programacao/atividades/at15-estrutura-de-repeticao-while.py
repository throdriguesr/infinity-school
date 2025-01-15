'''
Soma de Números Pares:
Crie um programa que use um laço while para somar
todos os números pares de 1 a 100 e exiba o resultado.

'''

soma = 0
numero = 2

while numero <= 100:
    soma += numero
    numero += 2

print(f"\nA soma de todos os números pares de 1 a 100 é: {soma}")