'''
Classificação de Notas:
Crie um programa que solicite uma nota de 0 a 100
e informe o conceito (A, B, C, D, F) com base na nota.

'''

nota = int(input("Digite uma nota de 0 a 100: "))

if 90 <= nota <= 100:
    conceito = "A"
elif 80 <= nota < 90:
    conceito = "B"
elif 70 <= nota < 80:
    conceito = "C"
elif 60 <= nota < 70:
    conceito = "D"
else:
    conceito = "F"

print(f"\nA nota {nota} corresponde ao conceito: {conceito}")