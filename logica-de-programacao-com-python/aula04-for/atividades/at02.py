'''
Soma de Números de 1 a 100:
Crie um programa que use um laço for para somar
todos os números de 1 a 100 e exiba o resultado.

'''

soma = 0

for numero in range(1, 101):
    soma += numero

print(f"A soma dos números de 1 a 100 é: {soma}")