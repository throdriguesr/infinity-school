'''
Cálculo de IMC:
Crie um programa que calcule o Índice de Massa Corporal (IMC).
Peça ao usuário para digitar seu peso e altura, armazene em variáveis e calcule o IMC.

'''

peso = float(input("Digite o seu peso (em kg): "))

altura = float(input("Digite a sua altura (em metros): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é {imc:.2f}")