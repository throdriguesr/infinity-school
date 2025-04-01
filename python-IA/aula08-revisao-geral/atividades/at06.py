'''
Receba uma lista de números e use funções agregadoras para contar quantos valores são ímpares e quantos são pares.

'''

numeros = list(map(int, input("Digite números separados por espaço: ").split()))

pares = sum(1 for num in numeros if num % 2 == 0)
impares = sum(1 for num in numeros if num % 2 != 0)

print("\nQuantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)