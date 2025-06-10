'''
Tabuada de um Número:
Faça um programa que solicite um número ao usuário e use
um laço while para exibir a tabuada desse número (de 1 a 10).

'''

numero = int(input("Digite um número para vermos a tabuada: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1