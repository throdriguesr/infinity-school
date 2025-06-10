'''
Entrada Válida:
Crie um programa que solicite ao usuário um número entre 1 e 10.
Continue pedindo até que o usuário forneça um valor válido.

'''

while True:
    numero = int(input("Digite um número entre 1 e 10: "))

    if 1 <= numero <= 10:
        print(f"Você digitou um número válido: {numero}")
        break

    else:
        print("Número inválido. Tente novamente.")