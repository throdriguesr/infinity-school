'''
Algoritmo de Conversão de Temperatura:
Crie um algoritmo que converta uma temperatura de Celsius
para Fahrenheit. Solicite ao usuário a temperatura em Celsius
e exiba o resultado em Fahrenheit.

'''

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"\n{celsius}°C equivalem a {fahrenheit:.2f}°F")