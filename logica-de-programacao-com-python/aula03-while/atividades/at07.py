'''
Tabuada com Condicional:
Faça um programa que solicite um número ao usuário e use
um laço while para exibir a tabuada desse número (de 1 a 10),
mas apenas para os resultados que forem múltiplos de 3.

'''

numero = int(input("Digite um número para ver a tabuada: "))
contador = 1

print("\nResultados multiplos de 3: ")
while contador <= 10:
    resultado = numero * contador

    if resultado % 3 == 0:
        print(f"{numero} x {contador} = {resultado}")
    
    contador += 1