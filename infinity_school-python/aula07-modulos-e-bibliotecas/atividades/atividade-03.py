'''
Crie um programa que permite ao usuário calcular a área e operímetro de formas geométricas simples, como quadrados, retângulos e círculos. 
Use funções matemáticas do módulo math para realizar os cálculos.

'''
import math

def calcular_quadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    return area, perimetro

def calcular_retangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def calcular_circulo(raio):
    area = math.pi * raio * raio
    perimetro = 2 * math.pi * raio
    return area, perimetro

print("Escolha uma forma geométrica:")
print("1 - Quadrado")
print("2 - Retângulo")
print("3 - Círculo")

opcao = input("\nDigite o número da forma: ")

if opcao == "1":
    lado = float(input("Digite o lado do quadrado: "))
    area, perimetro = calcular_quadrado(lado)

elif opcao == "2":
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area, perimetro = calcular_retangulo(base, altura)

elif opcao == "3":
    raio = float(input("Digite o raio do círculo: "))
    area, perimetro = calcular_circulo(raio)

else:
    print("Opção inválida!")
    exit()

print(f"\nÁrea: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")