'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

'''

n = int(input("Quantos números deseja inserir? "))

contador = 0
soma = 0

while contador < n:
    num = int(input("Digite um número: "))

    if contador == 0:
        menor = maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

    soma += num
    contador += 1

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")