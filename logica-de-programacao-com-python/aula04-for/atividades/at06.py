'''
Soma de Números Pares:
Escreva um programa que use um laço for para somar
todos os números pares de 1 a 50 e exiba o resultado final.

'''

soma = 0

for numero in range(2, 51, 2):
    soma += numero

print(f"A soma de todos os números pares de 1 a 50 é: {soma}")