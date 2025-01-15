'''
Tabuada de um Número:
Faça um programa que solicite um número ao usuário e use
um laço for para exibir a tabuada desse número (de 1 a 10).

'''

numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")